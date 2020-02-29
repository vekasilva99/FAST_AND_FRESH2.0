from django.contrib import admin
from .models import Product, Client, Provider, ProviderPhone, Member, Zona, City, State, Payment, EmployeeStore, Product_Type, Type_Of_Product, Batch, Store, StoreBoss, Delivery, PickUp, Bill, BillDetails, Currency, ExchangeRate, CashRegister, PaymentMethod, Employee, Job, IVA, ProviderPhone

# Register your models here.


class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_price',
                    'employee', 'bill_id', 'delivery_status', 'zona', 'address')


class PickUpAdmin(admin.ModelAdmin):
    list_display = ('id', 'pickup_status', 'bill_id')


class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'bill_sub_total',
                    'bill_iva', 'bill_date', 'bill_time', 'bill_earned_points', 'bill_delivery')


class BillDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill_id', 'product_batch', 'product_quantity')


class CashRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_id', 'is_active')


class CashRegisterBillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cash_register', 'bill')


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_method', 'is_active')


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency_name', 'is_active')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_name', 'employee_last_name', 'employee_cedula', 'employee_gender',
                    'employee_birth_date', 'employee_phone',  'employee_job', 'salary_bonus', 'employee_email')


class EmployeeStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_store', 'employee',
                    'hired_date')


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_name', 'job_salary')


class IVAAdmin(admin.ModelAdmin):
    list_display = ('id', 'iva_porcentaje', 'iva_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'is_special',
                    'is_active', 'provider')


class Type_of_Product_Admin(admin.ModelAdmin):
    list_display = ('id', 'type')


class Product_Type_Admin(admin.ModelAdmin):
    list_display = ('product_id', 'type_of_product_id')


class BatchAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'units', 'elaboration_date',
                    'expiration_date', 'price_dolars_u', 'units_sold', 'units_lost', 'discount', 'price_points', 'store')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_last_name',
                    'client_cedula', 'client_phone', 'client_gender', 'zona')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'member_email', 'member_points', 'client',
                    'member_start_date', 'member_pay_date', 'member_birth_date', 'is_active')


class ZonaAdmin(admin.ModelAdmin):
    list_display = ('id', 'zona_name', 'city', 'is_active')


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'state', 'is_active')


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_name', 'is_active')


class StoreAdmin (admin.ModelAdmin):
    list_display = ('id', 'store_name', 'open_time',
                    'closing_time', 'store_phone', 'zona', 'is_active')


class StoreBossAdmin (admin.ModelAdmin):
    list_display = ('boss', 'store', 'start_date', 'is_active')


class ExchangeRateAdmin (admin.ModelAdmin):
    list_display = ('id', 'origin_currency', 'exchange_rate',
                    'date')


class ProviderAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider_name', 'provider_email',
                    'provider_address', 'is_active')


class ProviderPhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'provider', 'provider_phone_number')
# Registrar los modelos


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Zona, ZonaAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Product_Type, Product_Type_Admin)
admin.site.register(Type_Of_Product, Type_of_Product_Admin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(PickUp, PickUpAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(BillDetails, BillDetailsAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ExchangeRate)
admin.site.register(CashRegister, CashRegisterAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(IVA, IVAAdmin)
admin.site.register(Payment)
admin.site.register(StoreBoss, StoreBossAdmin)
admin.site.register(EmployeeStore, EmployeeStoreAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(ProviderPhone, ProviderPhoneAdmin)
