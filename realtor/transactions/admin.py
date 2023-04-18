from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import Agent, Contract

# Register your models here.


# @admin.register(Agent)
# class AgentAdmin(admin.ModelAdmin):

#     list_display = ["id", "username", "upper_case_name", "date_joined", "last_login", "rating"]
#     list_editable = ["username"]
#     list_per_page = 5
#     list_filter = ("username", ("date_joined", DateRangeFilter), "rating")
#     exclude = ["password"]
#     search_fields = ["username", "first_name", "last_name"]

#     @admin.display(description="Name")
#     def upper_case_name(self, obj):
#         return ("%s %s" % (obj.first_name, obj.last_name)).upper()


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):

    list_display = ["id", "start_date", "end_date", "mortgage_ratio"]
    list_per_page = 5
    list_filter = ("start_date", "end_date")
    exclude = ["agreements"]
    search_fields = ["start_date", "end_date", "mortgage_ratio"]
