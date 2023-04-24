from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Agent, Contract

# Register your models here.


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
