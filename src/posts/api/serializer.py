from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
)
from accounts.api.serializers import UserDetailSerializer
from comments.api.serializer import CommentListSerializer
from comments.models import Comment
from posts.models import Post

post_detail_url = HyperlinkedIdentityField(
		view_name='posts-api:detail',
		lookup_field='slug'
	)

class PostListSerializer(ModelSerializer):
	url = post_detail_url
	user = UserDetailSerializer(read_only=True)
	image = SerializerMethodField()

	class Meta: 
		model = Post 
		fields = [
			'url',
			'user',
			'title',
			'content',
			'publish',
			'image',
#go to models.py for detail
		]



	def get_image(self,obj):
		try:
			image = obj.image.url
		except:
			image = None

		return image


class PostCreateUpdateSerializer(ModelSerializer):
	class Meta: 
		model = Post 
		fields = [
		#	'id',
			'title',
		#	'slug',
			'content',
			'publish',
#go to models.py for detail
		]




class PostDetailSerializer(ModelSerializer):
	url = post_detail_url
	user = UserDetailSerializer(read_only=True)
	image = SerializerMethodField()
	html = SerializerMethodField()
	comments = SerializerMethodField()

	class Meta:
		model = Post 
		fields = [
			'url',
			'id',
			'user',
			'title',
			'slug',
			'content',
			'html',
			'publish',
			'image',
			'comments',
		]
	def get_html(self,obj):
		return obj.get_markdown()


	def get_image(self,obj):
		try:
			image = obj.image.url
		except:
			image = None

		return image

	def get_comments(self, obj):
		content_type = obj.get_content_type
		object_id = obj.id
		c_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentListSerializer(c_qs, many=True).data
		return comments


#go to models.py for detail


'''
for shell commands
from posts.models import Post
from posts.api.serializer import PostDetailSerializer

obj = Post.objects.get(id=2)

data = {

	"title": "sup",
	"content": "New content",
	"publish": "2016-2-14",
	"slug": "yeah",

}

new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)



'''

