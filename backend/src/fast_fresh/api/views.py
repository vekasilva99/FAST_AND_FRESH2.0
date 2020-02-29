from rest_framework import viewsets, permissions
# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from fast_fresh.models import Product, Client, Member, Zona, City, State, Payment, Product_Type, Type_Of_Product, Batch, Store, Delivery, PickUp, Bill, BillDetails, Currency, ExchangeRate, CashRegister, PaymentMethod, Employee, Job, IVA, Provider, ProviderPhone, EmployeeStore, CashRegisterBills, StoreBoss
from .serializers import ProductSerializer, ClientSerializer, MemberSerializer, ZonaSerializer, CitySerializer, StateSerializer, PaymentSerializer, Product_TypeSerializer, Type_Of_ProductSerializer, BatchSerializer, StoreSerializer, DeliverySerializer, PickUpSerializer, BillSerializer, BillDetailsSerializer, CurrencySerializer, ExchangeRateSerializer, CashRegisterSerializer,  PaymentMethodSerializer, EmployeeSerializer, JobSerializer, IVASerializer, StoreBossSerializer, CashRegisterBillsSerializer, EmployeeStoreSerializer, ProviderSerializer, ProviderPhoneSerializer


# LIST VIEWS

# class ProductListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ClientListView(ListAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class MemberListView(ListAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer


# class ZonaListView(ListAPIView):
#     queryset = Zona.objects.all()
#     serializer_class = Zona


# class CityListView(ListAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer


# class StateListView(ListAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer


# class PaymentListView(ListAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer


# class Product_TypeListView(ListAPIView):
#     queryset = Product_Type.objects.all()
#     serializer_class = Product_TypeSerializer


# class Type_Of_ProductListView(ListAPIView):
#     queryset = Type_Of_Product.objects.all()
#     serializer_class = Type_Of_ProductSerializer


# class BatchListView(ListAPIView):
#     queryset = Batch.objects.all()
#     serializer_class = BatchSerializer


# class StoreListView(ListAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer


# class DeliveryListView(ListAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer


# class BillListView(ListAPIView):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer


# class PickUpListView(ListAPIView):
#     queryset = PickUp.objects.all()
#     serializer_class = PickUpSerializer


# class BillDetailsListView(ListAPIView):
#     queryset = BillDetails.objects.all()
#     serializer_class = BillDetailsSerializer


# class CurrencyListView(ListAPIView):
#     queryset = Currency.objects.all()
#     serializer_class = CurrencySerializer


# class ExchangeRateListView(ListAPIView):
#     queryset = ExchangeRate.objects.all()
#     serializer_class = ExchangeRateSerializer


# class CashRegisterListView(ListAPIView):
#     queryset = CashRegister.objects.all()
#     serializer_class = CashRegisterSerializer


# class PaymentMethodListView(ListAPIView):
#     queryset = PaymentMethod.objects.all()
#     serializer_class = PaymentMethodSerializer


# class EmployeeListView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class JobListView(ListAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer


# class IVAListView(ListAPIView):
#     queryset = IVA.objects.all()
#     serializer_class = IVASerializer


# class ProviderListView(ListAPIView):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer


# class ProviderPhoneListView(ListAPIView):
#     queryset = ProviderPhone.objects.all()
#     serializer_class = ProviderPhoneSerializer


# class EmployeeStoreListView(ListAPIView):
#     queryset = EmployeeStore.objects.all()
#     serializer_class = EmployeeStoreSerializer


# class CashRegisterBillsListView(ListAPIView):
#     queryset = CashRegisterBills.objects.all()
#     serializer_class = CashRegisterBillsSerializer


# class StoreBossBillsListView(ListAPIView):
#     queryset = StoreBoss.objects.all()
#     serializer_class = StoreBossSerializer


# Detail View


# class ProductDetailView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ClientDetailView(RetrieveAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class MemberDetailView(RetrieveAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer


# class ZonaDetailView(RetrieveAPIView):
#     queryset = Zona.objects.all()
#     serializer_class = Zona


# class CityDetailView(RetrieveAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer


# class StateDetailView(RetrieveAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer


# class PaymentDetailView(RetrieveAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer


# class Product_TypeDetailView(RetrieveAPIView):
#     queryset = Product_Type.objects.all()
#     serializer_class = Product_TypeSerializer


# class Type_Of_ProductDetailView(RetrieveAPIView):
#     queryset = Type_Of_Product.objects.all()
#     serializer_class = Type_Of_ProductSerializer


# class BatchDetailView(RetrieveAPIView):
#     queryset = Batch.objects.all()
#     serializer_class = BatchSerializer


# class StoreDetailView(RetrieveAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer


# class DeliveryDetailView(RetrieveAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer


# class BillDetailView(RetrieveAPIView):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer


# class PickUpDetailView(RetrieveAPIView):
#     queryset = PickUp.objects.all()
#     serializer_class = PickUpSerializer


# class BillDetailsDetailView(RetrieveAPIView):
#     queryset = BillDetails.objects.all()
#     serializer_class = BillDetailsSerializer


# class CurrencyDetailView(RetrieveAPIView):
#     queryset = Currency.objects.all()
#     serializer_class = CurrencySerializer


# class ExchangeRateDetailView(RetrieveAPIView):
#     queryset = ExchangeRate.objects.all()
#     serializer_class = ExchangeRateSerializer


# class CashRegisterDetailView(RetrieveAPIView):
#     queryset = CashRegister.objects.all()
#     serializer_class = CashRegisterSerializer


# class PaymentMethodDetailView(RetrieveAPIView):
#     queryset = PaymentMethod.objects.all()
#     serializer_class = PaymentMethodSerializer


# class EmployeeDetailView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class JobDetailView(RetrieveAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer


# class IVADetailView(RetrieveAPIView):
#     queryset = IVA.objects.all()
#     serializer_class = IVASerializer


# class ProviderDetailView(RetrieveAPIView):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer


# class ProviderPhoneDetailView(RetrieveAPIView):
#     queryset = ProviderPhone.objects.all()
#     serializer_class = ProviderPhoneSerializer


# class EmployeeStoreDetailView(RetrieveAPIView):
#     queryset = EmployeeStore.objects.all()
#     serializer_class = EmployeeStoreSerializer


# class CashRegisterBillsDetailView(RetrieveAPIView):
#     queryset = CashRegisterBills.objects.all()
#     serializer_class = CashRegisterBillsSerializer


# class StoreBossBillsDetailView(RetrieveAPIView):
#     queryset = StoreBoss.objects.all()
#     serializer_class = StoreBossSerializer


# Model View Sets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClientSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MemberSerializer


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Zona


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CitySerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StateSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PaymentSerializer


class Product_TypeViewSet(viewsets.ModelViewSet):
    queryset = Product_Type.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Product_TypeSerializer


class Type_Of_ProductViewSet(viewsets.ModelViewSet):
    queryset = Type_Of_Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Type_Of_ProductSerializer


class BatchViewSet(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BatchSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StoreSerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DeliverySerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BillSerializer


class PickUpViewSet(viewsets.ModelViewSet):
    queryset = PickUp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PickUpSerializer


class BillDetailsViewSet(viewsets.ModelViewSet):
    queryset = BillDetails.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BillDetailsSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CurrencySerializer


class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ExchangeRateSerializer


class CashRegisterViewSet(viewsets.ModelViewSet):
    queryset = CashRegister.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CashRegisterSerializer


class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PaymentMethodSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JobSerializer


class IVAViewSet(viewsets.ModelViewSet):
    queryset = IVA.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IVASerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProviderSerializer


class ProviderPhoneViewSet(viewsets.ModelViewSet):
    queryset = ProviderPhone.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProviderPhoneSerializer


class EmployeeStoreViewSet(viewsets.ModelViewSet):
    queryset = EmployeeStore.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmployeeStoreSerializer


class CashRegisterBillsViewSet(viewsets.ModelViewSet):
    queryset = CashRegisterBills.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CashRegisterBillsSerializer


class StoreBossViewSet(viewsets.ModelViewSet):
    queryset = StoreBoss.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StoreBossSerializer

# Create View


# class ProductCreateView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ClientCreateView(CreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class MemberCreateView(CreateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer


# class ZonaCreateView(CreateAPIView):
#     queryset = Zona.objects.all()
#     serializer_class = Zona


# class CityCreateView(CreateAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer


# class StateCreateView(CreateAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer


# class PaymentCreateView(CreateAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer


# class Product_TypeCreateView(CreateAPIView):
#     queryset = Product_Type.objects.all()
#     serializer_class = Product_TypeSerializer


# class Type_Of_ProductCreateView(CreateAPIView):
#     queryset = Type_Of_Product.objects.all()
#     serializer_class = Type_Of_ProductSerializer


# class BatchCreateView(CreateAPIView):
#     queryset = Batch.objects.all()
#     serializer_class = BatchSerializer


# class StoreCreateView(CreateAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer


# class DeliveryCreateView(CreateAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer


# class BillCreateView(CreateAPIView):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer


# class PickUpCreateView(CreateAPIView):
#     queryset = PickUp.objects.all()
#     serializer_class = PickUpSerializer


# class BillDetailsCreateView(CreateAPIView):
#     queryset = BillDetails.objects.all()
#     serializer_class = BillDetailsSerializer


# class CurrencyCreateView(CreateAPIView):
#     queryset = Currency.objects.all()
#     serializer_class = CurrencySerializer


# class ExchangeRateCreateView(CreateAPIView):
#     queryset = ExchangeRate.objects.all()
#     serializer_class = ExchangeRateSerializer


# class CashRegisterCreateView(CreateAPIView):
#     queryset = CashRegister.objects.all()
#     serializer_class = CashRegisterSerializer


# class PaymentMethodCreateView(CreateAPIView):
#     queryset = PaymentMethod.objects.all()
#     serializer_class = PaymentMethodSerializer


# class EmployeeCreateView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class JobCreateView(CreateAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer


# class IVACreateView(CreateAPIView):
#     queryset = IVA.objects.all()
#     serializer_class = IVASerializer


# class ProviderCreateView(CreateAPIView):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer


# class ProviderPhoneCreateView(CreateAPIView):
#     queryset = ProviderPhone.objects.all()
#     serializer_class = ProviderPhoneSerializer


# class EmployeeStoreCreateView(CreateAPIView):
#     queryset = EmployeeStore.objects.all()
#     serializer_class = EmployeeStoreSerializer


# class CashRegisterBillsCreateView(CreateAPIView):
#     queryset = CashRegisterBills.objects.all()
#     serializer_class = CashRegisterBillsSerializer


# class StoreBossBillsCreateView(CreateAPIView):
#     queryset = StoreBoss.objects.all()
#     serializer_class = StoreBossSerializer

# Update View


# class ProductUpdateView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ClientUpdateView(UpdateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class MemberUpdateView(UpdateAPIView):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer


# class ZonaUpdateView(UpdateAPIView):
#     queryset = Zona.objects.all()
#     serializer_class = Zona


# class CityUpdateView(UpdateAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer


# class StateUpdateView(UpdateAPIView):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer


# class PaymentUpdateView(UpdateAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer


# class Product_TypeUpdateView(UpdateAPIView):
#     queryset = Product_Type.objects.all()
#     serializer_class = Product_TypeSerializer


# class Type_Of_ProductUpdateView(UpdateAPIView):
#     queryset = Type_Of_Product.objects.all()
#     serializer_class = Type_Of_ProductSerializer


# class BatchUpdateView(UpdateAPIView):
#     queryset = Batch.objects.all()
#     serializer_class = BatchSerializer


# class StoreUpdateView(UpdateAPIView):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer


# class DeliveryUpdateView(UpdateAPIView):
#     queryset = Delivery.objects.all()
#     serializer_class = DeliverySerializer


# class BillUpdateView(UpdateAPIView):
#     queryset = Bill.objects.all()
#     serializer_class = BillSerializer


# class PickUpUpdateView(UpdateAPIView):
#     queryset = PickUp.objects.all()
#     serializer_class = PickUpSerializer


# class BillDetailsUpdateView(UpdateAPIView):
#     queryset = BillDetails.objects.all()
#     serializer_class = BillDetailsSerializer


# class CurrencyUpdateView(UpdateAPIView):
#     queryset = Currency.objects.all()
#     serializer_class = CurrencySerializer


# class ExchangeRateUpdateView(UpdateAPIView):
#     queryset = ExchangeRate.objects.all()
#     serializer_class = ExchangeRateSerializer


# class CashRegisterUpdateView(UpdateAPIView):
#     queryset = CashRegister.objects.all()
#     serializer_class = CashRegisterSerializer


# class PaymentMethodUpdateView(UpdateAPIView):
#     queryset = PaymentMethod.objects.all()
#     serializer_class = PaymentMethodSerializer


# class EmployeeUpdateView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class JobUpdateView(UpdateAPIView):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer


# class IVAUpdateView(UpdateAPIView):
#     queryset = IVA.objects.all()
#     serializer_class = IVASerializer


# class ProviderUpdateView(UpdateAPIView):
#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer


# class ProviderPhoneUpdateView(UpdateAPIView):
#     queryset = ProviderPhone.objects.all()
#     serializer_class = ProviderPhoneSerializer


# class EmployeeStoreUpdateView(UpdateAPIView):
#     queryset = EmployeeStore.objects.all()
#     serializer_class = EmployeeStoreSerializer


# class CashRegisterBillsUpdateView(UpdateAPIView):
#     queryset = CashRegisterBills.objects.all()
#     serializer_class = CashRegisterBillsSerializer


# class StoreBossBillsUpdateView(UpdateAPIView):
#     queryset = StoreBoss.objects.all()
#     serializer_class = StoreBossSerializer
