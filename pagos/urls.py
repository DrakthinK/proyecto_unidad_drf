from . import api
from rest_framework import routers
from django.urls import re_path, include
from versionespago.v1.router import api_urlpatterns as api_v1
#from versionespago.v2.router import api_urlpatterns as api_v2
from versionespago.v1 import api as apipagosv1
from versionespago.v2 import api as apipagosv2

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'pagos', api.PagoViewSet, 'pagos')

router.register(r'api/v1/pagos', apipagosv1.PagoViewSet, r'api/v1/pagos')

router.register(r'api/v2/services', apipagosv2.ServicesViewSet, r'api/v2/services')
router.register(r'api/v2/payment_user', apipagosv2.Payment_userViewSet, r'api/v2/payment_user')
router.register(r'api/v2/expired_payments', apipagosv2.Expired_paymentsViewSet, r'api/v2/expired_payments')
#router.register(r'api/v1/pagos', apipagosv1.PagoViewSet, r'api/v1/pagos')
#esto añadir
# urlpatterns = [
#     re_path(r'^api/v1/', include(api_v1))
#     #re_path(r'^api/v2/', include(api_v2)),
# ]
#end

urlpatterns = router.urls