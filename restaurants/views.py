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
            "dishes": [
                {
                    "id": d.id,
                    "name": d.name,
                    "description": d.description,
                    "price": str(d.price),
                    "is_available": d.is_available
                }
                for d in r.dishes.all()
            ]
        }
        for r in restaurants
    ]

    return JsonResponse(data, safe=False)


