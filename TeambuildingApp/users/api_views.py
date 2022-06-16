from rest_framework.generics import *
from django.contrib.auth.views import LoginView
from TeambuildingApp.users.serializers import *
from TeambuildingApp.users.models import *
from TeambuildingApp.users.models import Team

class TeamList(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamCreate(CreateAPIView):
    serializer_class = CreateTeamSerializer

    def create(self, request, *args, **kwargs):
        #activity_name = request.data.get()
        return super().create(request, *args, **kwargs)

class TeamRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    lookup_field = 'id'
    serializer_class = TeamSerializer

    def delete(self, request, *args, **kwargs):
        product_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))

        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            product = response.data
            cache.set('product_data_{}'.format(product['id']),{
                'name' : product['name']
            })

        return response



class ActivityList(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityCreate(CreateAPIView):
    serializer_class = ActivitySerializer

    #def create(self, request, *args, **kwargs):
    #    #activity_name = request.data.get()
    #    return super().create(request, *args, **kwargs)

class DetailsList(ListAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

class DetailsRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Details.objects.all()
    lookup_field = 'user_id'
    serializer_class = DetailsSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            details = response.data
            cache.set('details_data_{}'.format(details['user_id']),{
                'company_name' : details['company_name'],
                'is_staff' : details['is_staff']
            })

        return response

class UsersFilteredByCompanyList(ListAPIView):
    #queryset = Details.objects.filter()
    serializer_class = DetailsSerializer


