from django.contrib import admin
from accounts.models import User
from .models import House, Tenant, Plot

# register models in admin panel and create filters based on plots, tenants and house information
@admin.register(House)
class HouseModelAdmin(admin.ModelAdmin):
    list_display = ('house_number', 'plot_number', 'electricity_number', 'water_number', 'rent_amount','is_vacant')
    list_filter = ('is_vacant',)

@admin.register(Tenant)
class TenantModelAdmin(admin.ModelAdmin):
    list_display = ('house_number',)

@admin.register(Plot)
class PlotModelAdmin(admin.ModelAdmin):
    list_display = ('plot_number', 'plot_owner')

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_number', 'is_owner', 'is_tenant')
    list_filter = ('is_owner','is_tenant')

# @admin.register(MpesaTransaction)
# class MpesaTransactionModelAdmin(admin.ModelAdmin):
#     list_display = ('tenant_name','phone_number','amount','mpesa_transaction_id','date_joined','date_updated')