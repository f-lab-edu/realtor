from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Agent, Application, Contract, PreferredProperty, User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "upper_case_name", "date_joined", "last_login"]
    list_editable = ["username"]
    list_per_page = 5
    list_display_links = ["upper_case_name"]
    list_filter = ("username", ("date_joined", DateRangeFilter))
    exclude = ["password"]
    search_fields = ["username", "first_name", "last_name"]

    @admin.display(description="Name")
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).upper()


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "created_at", "updated_at"]
    list_per_page = 5
    list_filter = ["status"]
    search_fields = ["status"]


@admin.register(PreferredProperty)
class PreferredPropertyAdmin(admin.ModelAdmin):

    list_display = ["id", "full_address", "property_type", "detailed_type", "budget_from", "budget_to"]
    list_filter = ("city", "district", "zone", "property_type", "detailed_type")
    list_per_page = 5
    search_fields = ["property_type", "detailed_type"]

    @admin.display(description="Address")
    def full_address(self, obj):
        return obj.city + " " + obj.district + " " + obj.zone


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "rating"]
    list_per_page = 5
    list_filter = ["rating"]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "mortgage_ratio",
        "short_agreements",
        "start_date",
        "end_date",
    ]
    list_per_page = 5
    list_filter = (("start_date", DateRangeFilter), ("end_date", DateRangeFilter), "mortgage_ratio")
    search_fields = ["mortgage_ratio"]

    @admin.display(description="brief agreements")
    def short_agreements(self, obj):
        return obj.agreements[:20]
