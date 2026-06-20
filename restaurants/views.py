from django.shortcuts import render
from django.http import JsonResponse
from .models import Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.filter(is_active=True)

    data = [
        {
            "id": r.id,
            "name": r.name,
            "address": r.address,
            "phone": r.phone,
        }
        for r in restaurants
    ]

    return JsonResponse(data, safe=False)


