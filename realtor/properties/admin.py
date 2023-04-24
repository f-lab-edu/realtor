from django.contrib import admin

from .models import Property

# Register your models here.


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):

    list_display = ["id", "full_address", "property_type", "detailed_type", "status"]
    list_filter = ("city", "district", "zone", "property_type", "detailed_type", "status")
    list_per_page = 5
    search_fields = ["property_type", "detailed_type", "status"]

    @admin.display(description="Address")
    def full_address(self, obj):
        return obj.city + " " + obj.district + " " + obj.zone
