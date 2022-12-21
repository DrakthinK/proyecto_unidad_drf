from rest_framework import serializers
from pagos.models import (
    Pagos, Services,Payment_user,Expired_payments
)

#serializador Service
class ServiceSerializer(serializers.ModelSerializer):
      class Meta:
          model= Services
          fields='__all__'
          #read_only_fields='__all__'

#serializador Payment_user
class Payment_userSerializer(serializers.ModelSerializer):

     #usuario=serializers.StringRelatedField()
     #service=serializers.StringRelatedField()

     class Meta:
        model = Payment_user
        fields = '__all__'
        #read_only_fields = '__all__'


#serializador Expired_payments

class Expired_paymentsSerializer(serializers.ModelSerializer):
    #payment_usuario=serializers.StringRelatedField()
    class Meta:
        model = Expired_payments
        fields = '__all__'
        #read_only_fields = '__all__'




