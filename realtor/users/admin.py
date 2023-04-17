from django.contrib import admin
from rangefilter.filter import DateRangeFilter

from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "upper_case_name", "date_joined", "last_login"]
    list_editable = ["username"]
    list_per_page = 5
    list_filter = ("username", ("date_joined", DateRangeFilter))
    exclude = ["password"]
    search_fields = ["username", "first_name", "last_name"]

    @admin.display(description="Name")
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name)).upper()
