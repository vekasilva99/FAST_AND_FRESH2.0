from django.urls import path
from .views import ProductListView, ProductDetailView, ProductViewSet
from .views import ClientListView, ClientDetailView, ClientViewSet
from .views import MemberListView, MemberDetailView, MemberViewSet
from .views import ZonaListView, ZonaDetailView, ZonaViewSet
from .views import CityListView, CityDetailView, CityViewSet
from .views import StateListView, StateDetailView, StateViewSet
from .views import PaymentListView, PaymentDetailView, PaymentViewSet
from .views import Product_TypeListView, Product_TypeDetailView, Product_TypeViewSet
from .views import Type_Of_ProductListView, Type_Of_ProductDetailView, Type_Of_ProductViewSet
from .views import BatchListView, BatchDetailView, BatchViewSet
from .views import StoreListView, StoreDetailView, StoreViewSet
from .views import DeliveryListView, DeliveryDetailView, DeliveryViewSet
from .views import PickUpListView, PickUpDetailView, PickUpViewSet
from .views import BillListView, BillDetailView, BillViewSet
from .views import BillDetailsListView, BillDetailsDetailView, BillDetailsViewSet
from .views import CurrencyListView, CurrencyDetailView, CurrencyViewSet
from .views import ExchangeRateListView, ExchangeRateDetailView, ExchangeRateViewSet
from .views import CashRegisterListView, CashRegisterDetailView, CashRegisterViewSet
from .views import CashRegisterIncomeListView, CashRegisterIncomeDetailView, CashRegisterIncomeViewSet
from .views import PaymentMethodListView, PaymentMethodDetailView, PaymentMethodViewSet
from .views import EmployeeListView, EmployeeDetailView, EmployeeViewSet
from .views import JobListView, JobDetailView, JobViewSet
from .views import IVAListView, IVADetailView, IVAViewSet


urlpatterns = [
    path('product', ProductListView.as_view()),
    path('product/<pk>', ProductDetailView.as_view()),

    path('client', ClientListView.as_view()),
    path('client/<pk>', ClientDetailView.as_view()),

    path('member', MemberListView.as_view()),
    path('member/<pk>', MemberDetailView.as_view()),

    path('zona', ZonaListView.as_view()),
    path('zona/<pk>', ZonaDetailView.as_view()),

    path('city', CityListView.as_view()),
    path('city/<pk>', CityDetailView.as_view()),

    path('state', StateListView.as_view()),
    path('state/<pk>', StateDetailView.as_view()),

    path('payment', PaymentListView.as_view()),
    path('payment/<pk>', PaymentDetailView.as_view()),

    path('product_type', Product_TypeListView.as_view()),
    path('product_type/<pk>', Product_TypeDetailView.as_view()),

    path('type_of_product', Type_Of_ProductListView.as_view()),
    path('type_of_product/<pk>', Type_Of_ProductDetailView.as_view()),

    path('batch', BatchListView.as_view()),
    path('batch/<pk>', BatchDetailView.as_view()),

    path('store', StoreListView.as_view()),
    path('store/<pk>', StoreDetailView.as_view()),

    path('delivery', DeliveryListView.as_view()),
    path('delivery/<pk>', DeliveryDetailView.as_view()),

    path('pickup', PickUpListView.as_view()),
    path('pickup/<pk>', PickUpDetailView.as_view()),

    path('bill', BillListView.as_view()),
    path('bill/<pk>', BillDetailView.as_view()),

    path('billdetails', BillDetailsListView.as_view()),
    path('billdetails/<pk>', BillDetailsDetailView.as_view()),

    path('currency', CurrencyListView.as_view()),
    path('currency/<pk>', CurrencyDetailView.as_view()),

    path('exchangerate', ExchangeRateListView.as_view()),
    path('exchangerate/<pk>', ExchangeRateDetailView.as_view()),

    path('cashregister', CashRegisterListView.as_view()),
    path('cashregister/<pk>', CashRegisterDetailView.as_view()),

    path('cashregisterincome', CashRegisterIncomeListView.as_view()),
    path('cashregisterincome/<pk>', CashRegisterIncomeDetailView.as_view()),

    path('paymentmethod', PaymentMethodListView.as_view()),
    path('paymentmethod/<pk>', PaymentMethodDetailView.as_view()),

    path('employee', EmployeeListView.as_view()),
    path('employee/<pk>', EmployeeDetailView.as_view()),

    path('job', JobListView.as_view()),
    path('job/<pk>', JobDetailView.as_view()),

    path('iva', IVAListView.as_view()),
    path('iva/<pk>', IVADetailView.as_view()),
]
