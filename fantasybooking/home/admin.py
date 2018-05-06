from django.contrib import admin
from fantasybooking.home.models import WeeklyStat, Wrestler, Stable

# class YourModelAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(<your model here>, YourModelAdmin)

admin.site.register(WeeklyStat)
admin.site.register(Wrestler)
admin.site.register(Stable)

