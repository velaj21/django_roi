from django.shortcuts import redirect, render, get_object_or_404

from base.serializers import CountrySerializer

from .forms import CountryForm, CurrencyForm
from .models import Country, Currency
from django.http import JsonResponse
# from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from django.views.decorators.csrf import csrf_exempt

# import requests

from rest_framework.response import Response
from rest_framework import status
# import json

from rest_framework import viewsets

# Create your views here.

# def get_countries(request):
#     countries_objs = Country.objects.all()
#     return render(request, 'base/countries_list.html', {'countries': countries_objs})


# def create_country(request):
#     if request.method == 'POST':
#         form = CountryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('countries_list') 
#     else:
#         form = CountryForm()
#     return render(request, 'base/countries_create.html', {'form': form})


# def edit_country(request, country_id):
#     # country = get_object_or_404(Country, pk=country_id)
#     country = Country.objects.get(pk=country_id)
#     if request.method == 'POST':
#         form = CountryForm(request.POST, instance=country)
#         if form.is_valid():
#             form.save()
#             return redirect('countries_list')
#     else:
#         form = CountryForm(instance=country)
#     return render(request, 'base/countries_edit.html', {'form': form})


# def delete_country(request, country_id):
#     rec = Country.objects.filter(id=country_id)
#     print(str(rec.query))
#     country = get_object_or_404(Country, pk=country_id)
#     country.delete()
#     return redirect('countries_list')


# # ---------------------------------------------------------------------------

# def create_currency(request):
#     if request.method == 'POST':
#         form = CurrencyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('countries_list') 
#     else:
#         form = CurrencyForm()
#     return render(request, 'base/currency_create.html', {'form': form})


# # do zihet nje dhome hoteli
# # shtypet butoni njekohesisht nga 2 veta
# # kush ka internet me te mire ka perparesi
# # futet ne tranzaksion

# # 1 write
# # 2 write
# # 3 create

# @csrf_exempt
# def get_countries_http(request):
#     url = "https://random-word-api.herokuapp.com/word?number=10"
#     print(request)
#     return JsonResponse({'ok': 200}, status=200)
#     # try:
#     #     resp = requests.get(url, verify=False)
#     #     resp.raise_for_status() # 200 ok # 400 404 # 500
#     #     return render(request, 'base/test_list.html', {'words': resp.json()})
#     # except Exception as exc:
#     #     return JsonResponse({'error': str(exc)}, status=200)

from rest_framework.generics import ListAPIView


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    pagination_class = PageNumberPagination
    
    