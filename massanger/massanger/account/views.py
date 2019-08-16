import django_filters
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from rest_framework import viewsets, permissions, generics
from rest_framework import filters
from rest_framework.response import Response

from account.serializer import Massangerserializer, Searchserializer
from massage.models import Massanger
from massage.serializers import UserSerializer, ProfileSerializer, SsSerializer
import django_filters.rest_framework
import django_filters.rest_framework
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import filters

class LoginViewSet(viewsets.ModelViewSet):

    queryset = Massanger.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Massangerserializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

class SearchhView(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = Searchserializer
    def post(self, request, *args, **kwargs):
        # return Response({
        #     'SS':request.data['username']
        # })
        r=HttpResponseRedirect('/search?search=%s'%(request.data['username']))
        # data = r
        # # if r.status_code==200:
        # #     data = r.json();
        # #     # def post(self, request, *args):
        # #     #     serializer = ProfileSerializer(request.user, data=request.data)
        # #     #     serializer.is_valid(raise_exception=True)
        # #     #     user = serializer.save()
        # #     #     return Response({
        # #     #         "user": Massangerserializer(user).data
        # #     #     })
        return r