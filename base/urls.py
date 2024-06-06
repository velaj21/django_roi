from django.urls import path, include
from . import views  # make sure to import your views
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'djrf', views.CountryViewSet.as_view())

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    # path('create_country/', views.create_country, name='create_country'),
    # path('edit_country/<int:country_id>', views.edit_country, name='edit_country'),
    # path('delete_country/<int:country_id>/', views.delete_country, name='delete_country'),
    
    # path('create_currency/', views.create_currency, name='create_currency'),

    
    # path('get_countries_http/', views.get_countries_http, name='get_countries_http'),
    # path('djrf/', views.CountryViewSet.as_view(), name='country-list'),
    # path('djrf/<int:pk>/', views.CountryViewSet.as_view(), name='country-detail'),    
    # path('djrf/', views.CountryViewSet.as_view()),
    
    # path('', views.get_countries, name='countries_list'),
    
    path('countries/', views.CountryListAPIView.as_view(), name='country-list'),
    path('countries/<int:pk>/', views.CountryListAPIView.as_view(), name='country-detail'),
]


# urlpatterns = [
#     path('djrf/', views.CountryViewSet.as_view(), name='country-list'),
#     path('djrf/<int:pk>/', views.CountryViewSet.as_view(), name='country-detail'),
# ]
# # 
urlpatterns = format_suffix_patterns(urlpatterns)