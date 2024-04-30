from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers 
from .views import *
  

router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')
router.register(r'student', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # this line is used for only login & logout feature in DRF window
    path('api-token-auth/', views.obtain_auth_token)  # 3rd method to generate the token = api endpoint se 

     #1st method to create token = admin panel se 
     #2nd method terminal se  command =drf_create_token  (username )
]