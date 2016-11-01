from django.db.models import Q
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView





from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,


)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin


from rest_framework.generics import\
	( ListAPIView,
      RetrieveAPIView,
      UpdateAPIView,
      DestroyAPIView,
      CreateAPIView,
      RetrieveUpdateAPIView)

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


from posts.api.pagination import PostLimitOffsetPagination,PostPageNumberPagination
from posts.api.permission import  IsOwnerOrReadOnly
User = get_user_model()
from .serializers import \
    (
    UserCreateSerializer,
    UserLoginSerializer,
)






class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permissions_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permissions_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serialzer = UserLoginSerializer(data=data)
        if serialzer.is_valid(raise_exception=True):
            new_data = serialzer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serialzer.error, status=HTTP_400_BAD_REQUEST)


