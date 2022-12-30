#from pagos.models import Pagos
#from rest_framework import viewsets
#from pagos.serializers import PagoSerializer
from pagos.models import (
    Pagos,
    Services,
    Payment_user,
    Expired_payments
)
from .serializers import (
ServiceSerializer,
Payment_userSerializer,
Expired_paymentsSerializer
)
from rest_framework.permissions import IsAuthenticated
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters

from rest_framework import mixins
# class PagoViewSet(viewsets.ModelViewSet):
#     queryset = Pagos.objects.get_queryset().order_by('id')
#     serializer_class = PagoSerializer
#     pagination_class = StandardResultsSetPagination
#     filter_backends = [filters.SearchFilter]
#     permission_classes = [IsAuthenticated]
#
#     search_fields = ['usuario__id', 'fecha_pago', 'servicio']
#     throttle_scope = 'pagos'

#Services api

#serviceViewset
class ServicesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Services.objects.get_queryset().order_by('id')
    serializer_class = ServiceSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]

    #search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    #throttle_scope = 'pagos'


#Payment_userViewset
class Payment_userViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.get_queryset().order_by('id')
    serializer_class = Payment_userSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    search_fields=['paymentDate','expirationDate']
    #search_fields = ['usuario__id', 'fecha_pago', 'servicio']
    throttle_scope = 'payment_user'


#Expired_paymentsViewset
class Expired_paymentsViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
viewsets.GenericViewSet):
    queryset = Expired_payments.objects.get_queryset().order_by('id')
    serializer_class = Expired_paymentsSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAuthenticated]
    throttle_scope = 'expired_payments'