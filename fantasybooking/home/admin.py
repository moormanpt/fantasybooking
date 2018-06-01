from django.contrib import admin
from fantasybooking.home.models import WeeklyStat, Wrestler, Stable, Match

# class YourModelAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(<your model here>, YourModelAdmin)

class WrestlerInline(admin.TabularInline):
    model = Wrestler

class StableAdmin(admin.ModelAdmin):
    inlines = [
        WrestlerInline,
    ]

class WeeklyStatInline(admin.TabularInline):
    model = WeeklyStat

class WrestlerAdmin(admin.ModelAdmin):
    inlines = [
        WeeklyStatInline,
    ]

admin.site.register(WeeklyStat)
admin.site.register(Wrestler, WrestlerAdmin)
admin.site.register(Stable, StableAdmin)
admin.site.register(Match)
