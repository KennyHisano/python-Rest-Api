from django.db.models import Q
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,


)


from rest_framework.generics import\
	( ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView)

from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,

)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
)


from posts.models import Post
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination
from .permission import  IsOwnerOrReadOnly



from .serializer import \
	(PostDetailSerializer,
	 PostListSerializer,
	 PostCreateUpdateSerializer)







class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	#permission_classes = [IsAuthenticated]
#here takes each user for list
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		''',title='my title'''
		#u can override content here






class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	permission_classes = [AllowAny]
	#lookup_url_kwarg = "abc"





class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'
	permission_classes = [IsOwnerOrReadOnly]
	#lookup_url_kwarg = "abc"
	def perform_update(self,serializer):
		serializer.save(user=self.request.user)




class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	#lookup_url_kwarg = "abc"
	permission_classes = [IsOwnerOrReadOnly]




class PostListAPIView(ListAPIView):
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title','content', 'user__first_name']
	permission_classes = [AllowAny]
	pagination_class = PostPageNumberPagination# PageNumberPagination
	def get_queryset(self, *args, **kwargs):
		#queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
		queryset_list = Post.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(title__icontains=query)|
					Q(content__icontains=query)|
					Q(user__first_name__icontains=query) |
					Q(user__last_name__icontains=query)
					).distinct()
		return queryset_list

