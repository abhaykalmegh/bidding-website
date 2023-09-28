from django.contrib import admin
from .models import Painting, Bid


# Register your models here.


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    list_display = ('title', 'painter', 'base_price', 'created_at')
    list_filter = ('painter', 'created_at')
    search_fields = ('title', 'painter__username')
    ordering = ('-created_at',)


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('painting', 'buyer', 'bid_amount', 'approved', 'created_at')
    list_filter = ('painting', 'buyer', 'approved', 'created_at')
    search_fields = ('painting__title', 'buyer__username')
    ordering = ('-created_at',)
