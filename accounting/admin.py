from django.contrib import admin

from accounting.models import Account, Booking

# Register your models here.
admin.site.register(Account)
admin.site.register(Booking)
