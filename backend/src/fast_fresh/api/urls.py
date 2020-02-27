from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductViewSet, ProductCreateView, ProductUpdateView
from .views import ClientListView, ClientDetailView, ClientViewSet, ClientCreateView, ClientUpdateView
from .views import MemberListView, MemberDetailView, MemberViewSet, MemberCreateView, MemberUpdateView
from .views import ZonaListView, ZonaDetailView, ZonaViewSet, ZonaCreateView, ZonaUpdateView
from .views import CityListView, CityDetailView, CityViewSet, CityCreateView, CityUpdateView
from .views import StateListView, StateDetailView, StateViewSet, StateCreateView, StateUpdateView
from .views import PaymentListView, PaymentDetailView, PaymentViewSet, PaymentCreateView, PaymentUpdateView
from .views import Product_TypeListView, Product_TypeDetailView, Product_TypeViewSet, Product_TypeCreateView, Product_TypeUpdateView
from .views import Type_Of_ProductListView, Type_Of_ProductDetailView, Type_Of_ProductViewSet, Type_Of_ProductCreateView, Type_Of_ProductUpdateView
from .views import BatchListView, BatchDetailView, BatchViewSet, BatchCreateView, BatchUpdateView
from .views import StoreListView, StoreDetailView, StoreViewSet, StoreCreateView, StoreUpdateView
from .views import DeliveryListView, DeliveryDetailView, DeliveryViewSet, DeliveryCreateView, DeliveryUpdateView
from .views import PickUpListView, PickUpDetailView, PickUpViewSet, PickUpCreateView, PickUpUpdateView
from .views import BillListView, BillDetailView, BillViewSet, BillCreateView, BillUpdateView
from .views import BillDetailsListView, BillDetailsDetailView, BillDetailsViewSet, BillDetailsCreateView, BillDetailsUpdateView
from .views import CurrencyListView, CurrencyDetailView, CurrencyViewSet, CurrencyCreateView, CurrencyUpdateView
from .views import ExchangeRateListView, ExchangeRateDetailView, ExchangeRateViewSet, ExchangeRateCreateView, ExchangeRateUpdateView
from .views import CashRegisterListView, CashRegisterDetailView, CashRegisterViewSet, CashRegisterCreateView, CashRegisterUpdateView
from .views import CashRegisterIncomeListView, CashRegisterIncomeDetailView, CashRegisterIncomeViewSet, CashRegisterIncomeCreateView, CashRegisterIncomeUpdateView
from .views import PaymentMethodListView, PaymentMethodDetailView, PaymentMethodViewSet, PaymentMethodCreateView, PaymentMethodUpdateView
from .views import EmployeeListView, EmployeeDetailView, EmployeeViewSet, EmployeeCreateView, EmployeeUpdateView
from .views import JobListView, JobDetailView, JobViewSet, JobCreateView, JobUpdateView
from .views import IVAListView, IVADetailView, IVAViewSet, IVACreateView, IVAUpdateView


urlpatterns = [
    path('product', ProductListView.as_view()),
    path('product/create/', ProductCreateView.as_view()),
    path('product/<pk>', ProductDetailView.as_view()),
    path('product/<pk>/update/', ProductUpdateView.as_view()),


    path('client', ClientListView.as_view()),
    path('client/create/', ClientCreateView.as_view()),
    path('client/<pk>', ClientDetailView.as_view()),
    path('client/<pk>/update/', ClientUpdateView.as_view()),

    path('member', MemberListView.as_view()),
    path('member/create/', MemberCreateView.as_view()),
    path('member/<pk>', MemberDetailView.as_view()),
    path('member/<pk>/update/', MemberUpdateView.as_view()),

    path('zona', ZonaListView.as_view()),
    path('zona/create/', ZonaCreateView.as_view()),
    path('zona/<pk>', ZonaDetailView.as_view()),
    path('zona/<pk>/update/', ZonaUpdateView.as_view()),

    path('city', CityListView.as_view()),
    path('city/create/', CityCreateView.as_view()),
    path('city/<pk>', CityDetailView.as_view()),
    path('city/<pk>/update/', CityUpdateView.as_view()),

    path('state', StateListView.as_view()),
    path('state/create/', StateCreateView.as_view()),
    path('state/<pk>', StateDetailView.as_view()),
    path('state/<pk>/update/', StateUpdateView.as_view()),


    path('payment', PaymentListView.as_view()),
    path('payment/create/', PaymentCreateView.as_view()),
    path('payment/<pk>', PaymentDetailView.as_view()),
    path('payment/<pk>/update/', PaymentUpdateView.as_view()),

    path('product_type', Product_TypeListView.as_view()),
    path('product_type/create/', Product_TypeCreateView.as_view()),
    path('product_type/<pk>', Product_TypeDetailView.as_view()),
    path('product_type/<pk>/update/', Product_TypeUpdateView.as_view()),


    path('type_of_product', Type_Of_ProductListView.as_view()),
    path('type_of_product/create/', Type_Of_ProductCreateView.as_view()),
    path('type_of_product/<pk>', Type_Of_ProductDetailView.as_view()),
    path('type_of_product/<pk>/update/', Type_Of_ProductUpdateView.as_view()),

    path('batch', BatchListView.as_view()),
    path('batch/create/', BatchCreateView.as_view()),
    path('batch/<pk>', BatchDetailView.as_view()),
    path('batch/<pk>/update/', BatchUpdateView.as_view()),


    path('store', StoreListView.as_view()),
    path('store/create/', StoreCreateView.as_view()),
    path('store/<pk>', StoreDetailView.as_view()),
    path('store/<pk>/update/', StoreUpdateView.as_view()),


    path('delivery', DeliveryListView.as_view()),
    path('delivery/create/', DeliveryCreateView.as_view()),
    path('delivery/<pk>', DeliveryDetailView.as_view()),
    path('delivery/<pk>/update/', DeliveryUpdateView.as_view()),

    path('pickup', PickUpListView.as_view()),
    path('pickup/create/', PickUpCreateView.as_view()),
    path('pickup/<pk>', PickUpDetailView.as_view()),
    path('pickup/<pk>/update/', PickUpUpdateView.as_view()),


    path('bill', BillListView.as_view()),
    path('bill/create/', BillCreateView.as_view()),
    path('bill/<pk>', BillDetailView.as_view()),
    path('bill/<pk>/update/', BillUpdateView.as_view()),

    path('billdetails', BillDetailsListView.as_view()),
    path('billdetails/create/', BillDetailsCreateView.as_view()),
    path('billdetails/<pk>', BillDetailsDetailView.as_view()),
    path('billdetails/<pk>/update/', BillDetailsUpdateView.as_view()),

    path('currency', CurrencyListView.as_view()),
    path('currency/create/', CurrencyCreateView.as_view()),
    path('currency/<pk>', CurrencyDetailView.as_view()),
    path('currency/<pk>/update/', CurrencyUpdateView.as_view()),

    path('exchangerate', ExchangeRateListView.as_view()),
    path('exchangerate/create/', ExchangeRateCreateView.as_view()),
    path('exchangerate/<pk>', ExchangeRateDetailView.as_view()),
    path('exchangerate/<pk>/update/', ExchangeRateUpdateView.as_view()),

    path('cashregister', CashRegisterListView.as_view()),
    path('cashregister/create/', CashRegisterCreateView.as_view()),
    path('cashregister/<pk>', CashRegisterDetailView.as_view()),
    path('cashregister/<pk>/update/', CashRegisterUpdateView.as_view()),

    path('cashregisterincome', CashRegisterIncomeListView.as_view()),
    path('cashregisterincome/create/', CashRegisterIncomeCreateView.as_view()),
    path('cashregisterincome/<pk>', CashRegisterIncomeDetailView.as_view()),
    path('cashregisterincome/<pk>/update/',
         CashRegisterIncomeUpdateView.as_view()),

    path('paymentmethod', PaymentMethodListView.as_view()),
    path('paymentmethod/create/', PaymentMethodCreateView.as_view()),
    path('paymentmethod/<pk>', PaymentMethodDetailView.as_view()),
    path('paymentmethod/<pk>/update/', PaymentMethodUpdateView.as_view()),

    path('employee', EmployeeListView.as_view()),
    path('employee/create/', EmployeeCreateView.as_view()),
    path('employee/<pk>', EmployeeDetailView.as_view()),
    path('employee/<pk>/update/', EmployeeUpdateView.as_view()),

    path('job', JobListView.as_view()),
    path('job/create/', JobCreateView.as_view()),
    path('job/<pk>', JobDetailView.as_view()),
    path('job/<pk>/update/', JobUpdateView.as_view()),

    path('iva', IVAListView.as_view()),
    path('iva/create/', IVACreateView.as_view()),
    path('iva/<pk>', IVADetailView.as_view()),
    path('iva/<pk>/update/', IVAUpdateView.as_view()),
]


# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
# urlpatterns = router.urls
