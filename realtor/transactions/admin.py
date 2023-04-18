from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Agent, Contract

# Register your models here.


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):

    list_display = ["id", "user", "rating"]
    list_filter = ["rating"]


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = ["id", "start_date", "end_date", "mortgage_ratio"]
    list_per_page = 5
    list_filter = (("start_date", DateRangeFilter), ("end_date", DateRangeFilter), "mortgage_ratio")
    exclude = ["agreements"]
    search_fields = ["start_date", "end_date", "mortgage_ratio"]
