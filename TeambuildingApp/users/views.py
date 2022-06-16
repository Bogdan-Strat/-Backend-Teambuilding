from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from TeambuildingApp.users.serializers import *
from TeambuildingApp.users.models import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request):
       #request.data['is_staff'] = True 
       #print(request.data.get('is_staff'))
       response = super().create(request)
       user = User.objects.filter(id = response.data.get("id")).first()
       user.is_staff = True
       print(user.is_staff)
       details = Details.objects.create(user = user)
       print(details.user.is_staff)
       details.save() 
       return response
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



