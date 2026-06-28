from django.contrib import admin
from .models import Restaurant, Dish

class DishInline(admin.TabularInline):
    """this class is used to display the related Dish model in the Restaurant admin page. TabularInline is a compact way to show related objects in a tabular format."""
    model = Dish
    extra = 1  # Number of extra empty forms to display in the inline

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "phone", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("name", "address")
    inlines = [DishInline]  # You can add inlines for related models if needed

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant", "price", "is_available")
    list_filter = ("is_available", "restaurant")
    search_fields = ("name",)  # Allows searching by dish name and restaurant name
