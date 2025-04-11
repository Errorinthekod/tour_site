from django.contrib import admin

from .models import Tour, TourImage


# Register your models here.




class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1
    max_num = 32  # Ограничение для админки

class TourAdmin(admin.ModelAdmin):
    inlines = [TourImageInline]


admin.site.register(Tour, TourAdmin)


"""Келечекте бул файл өзгөрүш мүмкүн"""