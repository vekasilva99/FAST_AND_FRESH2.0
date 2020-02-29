from rest_framework.routers import DefaultRouter
from django.urls import path
# from .views import ProductListView, ProductDetailView, ProductViewSet, ProductCreateView, ProductUpdateView
# from .views import ClientListView, ClientDetailView, ClientViewSet, ClientCreateView, ClientUpdateView
# from .views import MemberListView, MemberDetailView, MemberViewSet, MemberCreateView, MemberUpdateView
# from .views import ZonaListView, ZonaDetailView, ZonaViewSet, ZonaCreateView, ZonaUpdateView
# from .views import CityListView, CityDetailView, CityViewSet, CityCreateView, CityUpdateView
# from .views import StateListView, StateDetailView, StateViewSet, StateCreateView, StateUpdateView
# from .views import PaymentListView, PaymentDetailView, PaymentViewSet, PaymentCreateView, PaymentUpdateView
# from .views import Product_TypeListView, Product_TypeDetailView, Product_TypeViewSet, Product_TypeCreateView, Product_TypeUpdateView
# from .views import Type_Of_ProductListView, Type_Of_ProductDetailView, Type_Of_ProductViewSet, Type_Of_ProductCreateView, Type_Of_ProductUpdateView
# from .views import BatchListView, BatchDetailView, BatchViewSet, BatchCreateView, BatchUpdateView
# from .views import StoreListView, StoreDetailView, StoreViewSet, StoreCreateView, StoreUpdateView
# from .views import DeliveryListView, DeliveryDetailView, DeliveryViewSet, DeliveryCreateView, DeliveryUpdateView
# from .views import PickUpListView, PickUpDetailView, PickUpViewSet, PickUpCreateView, PickUpUpdateView
# from .views import BillListView, BillDetailView, BillViewSet, BillCreateView, BillUpdateView
# from .views import BillDetailsListView, BillDetailsDetailView, BillDetailsViewSet, BillDetailsCreateView, BillDetailsUpdateView
# from .views import CurrencyListView, CurrencyDetailView, CurrencyViewSet, CurrencyCreateView, CurrencyUpdateView
# from .views import ExchangeRateListView, ExchangeRateDetailView, ExchangeRateViewSet, ExchangeRateCreateView, ExchangeRateUpdateView
# from .views import CashRegisterListView, CashRegisterDetailView, CashRegisterViewSet, CashRegisterCreateView, CashRegisterUpdateView
# from .views import PaymentMethodListView, PaymentMethodDetailView, PaymentMethodViewSet, PaymentMethodCreateView, PaymentMethodUpdateView
# from .views import EmployeeListView, EmployeeDetailView, EmployeeViewSet, EmployeeCreateView, EmployeeUpdateView
# from .views import JobListView, JobDetailView, JobViewSet, JobCreateView, JobUpdateView
# from .views import IVAListView, IVADetailView, IVAViewSet, IVACreateView, IVAUpdateView
# from .views import StoreBossListView, StoreBossDetailView, StoreBossViewSet, StoreBossCreateView, StoreBossUpdateView
# from .views import CashRegisterBillsListView, CashRegisterBillsDetailView, CashRegisterBillsViewSet, CashRegisterBillsCreateView, CashRegisterBillsUpdateView
# from .views import EmployeeStoreListView, EmployeeStoreDetailView, EmployeeStoreViewSet, EmployeeStoreCreateView, EmployeeStoreUpdateView
# from .views import ProviderListView, ProviderDetailView, ProviderViewSet, ProviderCreateView, ProviderUpdateView
# from .views import ProviderPhoneListView, ProviderPhoneDetailView, ProviderPhoneViewSet, ProviderPhoneCreateView, ProviderUpdateView

from .views import ProductViewSet
from .views import ClientViewSet
from .views import MemberViewSet
from .views import ZonaViewSet
from .views import CityViewSet
from .views import StateViewSet
from .views import PaymentViewSet
from .views import Product_TypeViewSet
from .views import Type_Of_ProductViewSet
from .views import BatchViewSet
from .views import StoreViewSet
from .views import DeliveryViewSet
from .views import PickUpViewSet
from .views import BillViewSet
from .views import BillDetailsViewSet
from .views import CurrencyViewSet
from .views import ExchangeRateViewSet
from .views import CashRegisterViewSet
from .views import PaymentMethodViewSet
from .views import EmployeeViewSet
from .views import JobViewSet
from .views import IVAViewSet
from .views import StoreBossViewSet
from .views import CashRegisterBillsViewSet
from .views import EmployeeStoreViewSet
from .views import ProviderViewSet
from .views import ProviderPhoneViewSet

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='products')
router.register(r'client', ClientViewSet, basename='client')
router.register(r'member', MemberViewSet, basename='member')
router.register(r'zona', ZonaViewSet, basename='zona')
router.register(r'city', CityViewSet, basename='city')
router.register(r'state', StateViewSet, basename='state')
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'product_type', Product_TypeViewSet, basename='product_type')
router.register(r'type_of_product', Type_Of_ProductViewSet,
                basename='type_of_product')
router.register(r'batch', ProductViewSet, basename='batch')
router.register(r'store', ProductViewSet, basename='store')
router.register(r'delivery', ProductViewSet, basename='delivery')
router.register(r'pickup', ProductViewSet, basename='pickup')
router.register(r'bill', ProductViewSet, basename='bill')
router.register(r'billdetails', ProductViewSet, basename='billdetails')
router.register(r'currency', ProductViewSet, basename='currency')
router.register(r'exchangerate', ProductViewSet, basename='exchangerate')
router.register(r'cashregister', ProductViewSet, basename='cashregister')
router.register(r'paymentmethod', ProductViewSet, basename='paymentmethod')
router.register(r'employee', ProductViewSet, basename='employee')
router.register(r'job', ProductViewSet, basename='job')
router.register(r'iva', ProductViewSet, basename='iva')
router.register(r'storeboss', ProductViewSet, basename='storeboss')
router.register(r'cashregisterbills', ProductViewSet,
                basename='cashregisterbills')
router.register(r'employeestore', ProductViewSet, basename='employeestore')
router.register(r'provider', ProviderViewSet, basename='provider')
router.register(r'providerphone', ProductViewSet, basename='providerphone')
urlpatterns = router.urls

# urlpatterns = [
#     path('product', ProductListView.as_view()),
#     path('product/create/', ProductCreateView.as_view()),
#     path('product/<pk>', ProductDetailView.as_view()),
#     path('product/<pk>/update/', ProductUpdateView.as_view()),


#     path('client', ClientListView.as_view()),
#     path('client/create/', ClientCreateView.as_view()),
#     path('client/<pk>', ClientDetailView.as_view()),
#     path('client/<pk>/update/', ClientUpdateView.as_view()),

#     path('member', MemberListView.as_view()),
#     path('member/create/', MemberCreateView.as_view()),
#     path('member/<pk>', MemberDetailView.as_view()),
#     path('member/<pk>/update/', MemberUpdateView.as_view()),

#     path('zona', ZonaListView.as_view()),
#     path('zona/create/', ZonaCreateView.as_view()),
#     path('zona/<pk>', ZonaDetailView.as_view()),
#     path('zona/<pk>/update/', ZonaUpdateView.as_view()),

#     path('city', CityListView.as_view()),
#     path('city/create/', CityCreateView.as_view()),
#     path('city/<pk>', CityDetailView.as_view()),
#     path('city/<pk>/update/', CityUpdateView.as_view()),

#     path('state', StateListView.as_view()),
#     path('state/create/', StateCreateView.as_view()),
#     path('state/<pk>', StateDetailView.as_view()),
#     path('state/<pk>/update/', StateUpdateView.as_view()),


#     path('payment', PaymentListView.as_view()),
#     path('payment/create/', PaymentCreateView.as_view()),
#     path('payment/<pk>', PaymentDetailView.as_view()),
#     path('payment/<pk>/update/', PaymentUpdateView.as_view()),

#     path('product_type', Product_TypeListView.as_view()),
#     path('product_type/create/', Product_TypeCreateView.as_view()),
#     path('product_type/<pk>', Product_TypeDetailView.as_view()),
#     path('product_type/<pk>/update/', Product_TypeUpdateView.as_view()),


#     path('type_of_product', Type_Of_ProductListView.as_view()),
#     path('type_of_product/create/', Type_Of_ProductCreateView.as_view()),
#     path('type_of_product/<pk>', Type_Of_ProductDetailView.as_view()),
#     path('type_of_product/<pk>/update/', Type_Of_ProductUpdateView.as_view()),

#     path('batch', BatchListView.as_view()),
#     path('batch/create/', BatchCreateView.as_view()),
#     path('batch/<pk>', BatchDetailView.as_view()),
#     path('batch/<pk>/update/', BatchUpdateView.as_view()),


#     path('store', StoreListView.as_view()),
#     path('store/create/', StoreCreateView.as_view()),
#     path('store/<pk>', StoreDetailView.as_view()),
#     path('store/<pk>/update/', StoreUpdateView.as_view()),


#     path('delivery', DeliveryListView.as_view()),
#     path('delivery/create/', DeliveryCreateView.as_view()),
#     path('delivery/<pk>', DeliveryDetailView.as_view()),
#     path('delivery/<pk>/update/', DeliveryUpdateView.as_view()),

#     path('pickup', PickUpListView.as_view()),
#     path('pickup/create/', PickUpCreateView.as_view()),
#     path('pickup/<pk>', PickUpDetailView.as_view()),
#     path('pickup/<pk>/update/', PickUpUpdateView.as_view()),


#     path('bill', BillListView.as_view()),
#     path('bill/create/', BillCreateView.as_view()),
#     path('bill/<pk>', BillDetailView.as_view()),
#     path('bill/<pk>/update/', BillUpdateView.as_view()),

#     path('billdetails', BillDetailsListView.as_view()),
#     path('billdetails/create/', BillDetailsCreateView.as_view()),
#     path('billdetails/<pk>', BillDetailsDetailView.as_view()),
#     path('billdetails/<pk>/update/', BillDetailsUpdateView.as_view()),

#     path('currency', CurrencyListView.as_view()),
#     path('currency/create/', CurrencyCreateView.as_view()),
#     path('currency/<pk>', CurrencyDetailView.as_view()),
#     path('currency/<pk>/update/', CurrencyUpdateView.as_view()),

#     path('exchangerate', ExchangeRateListView.as_view()),
#     path('exchangerate/create/', ExchangeRateCreateView.as_view()),
#     path('exchangerate/<pk>', ExchangeRateDetailView.as_view()),
#     path('exchangerate/<pk>/update/', ExchangeRateUpdateView.as_view()),

#     path('cashregister', CashRegisterListView.as_view()),
#     path('cashregister/create/', CashRegisterCreateView.as_view()),
#     path('cashregister/<pk>', CashRegisterDetailView.as_view()),
#     path('cashregister/<pk>/update/', CashRegisterUpdateView.as_view()),


#     path('paymentmethod', PaymentMethodListView.as_view()),
#     path('paymentmethod/create/', PaymentMethodCreateView.as_view()),
#     path('paymentmethod/<pk>', PaymentMethodDetailView.as_view()),
#     path('paymentmethod/<pk>/update/', PaymentMethodUpdateView.as_view()),

#     path('employee', EmployeeListView.as_view()),
#     path('employee/create/', EmployeeCreateView.as_view()),
#     path('employee/<pk>', EmployeeDetailView.as_view()),
#     path('employee/<pk>/update/', EmployeeUpdateView.as_view()),

#     path('job', JobListView.as_view()),
#     path('job/create/', JobCreateView.as_view()),
#     path('job/<pk>', JobDetailView.as_view()),
#     path('job/<pk>/update/', JobUpdateView.as_view()),

#     path('iva', IVAListView.as_view()),
#     path('iva/create/', IVACreateView.as_view()),
#     path('iva/<pk>', IVADetailView.as_view()),
#     path('iva/<pk>/update/', IVAUpdateView.as_view()),

#     path('storeboss', StoreBossListView.as_view()),
#     path('storeboss/create/', StoreBossCreateView.as_view()),
#     path('iva/<pk>', StoreBossDetailView.as_view()),
#     path('storeboss/<pk>/update/', StoreBossUpdateView.as_view()),

#     path('cashregisterbills', CashRegisterBillsListView.as_view()),
#     path('cashregisterbills/create/', CashRegisterBillsCreateView.as_view()),
#     path('cashregisterbills/<pk>', CashRegisterBillsDetailView.as_view()),
#     path('cashregisterbills/<pk>/update/',
#          CashRegisterBillsUpdateView.as_view()),

#     path('employeestore', EmployeeStoreListView.as_view()),
#     path('employeestore/create/', EmployeeStoreCreateView.as_view()),
#     path('employeestore/<pk>', EmployeeStoreDetailView.as_view()),
#     path('employeestore/<pk>/update/', EmployeeStoreUpdateView.as_view()),

#     path('provider', ProviderListView.as_view()),
#     path('provider/create/', ProviderCreateView.as_view()),
#     path('provider/<pk>', ProviderDetailView.as_view()),
#     path('provider/<pk>/update/', ProviderUpdateView.as_view()),

#     path('providerphone', ProviderPhoneListView.as_view()),
#     path('providerphone/create/', ProviderPhoneCreateView.as_view()),
#     path('providerphone/<pk>', ProviderPhoneDetailView.as_view()),
#     path('providerphone/<pk>/update/', ProviderPhoneUpdateView.as_view()),
# ]
