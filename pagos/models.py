from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User
# Create your models here.

class Pagos(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    fecha_pago = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='users')
    monto = models.FloatField(default=0.0)


##MODELOS PARA VERSION 2 DE PROYECTO
# Services
# - Id
# - Name
# - Description
# - Logo
class Services(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    #logo=models.ImageField(upload_to="logo/images")
    logo = models.CharField(max_length=200)
    def __str__(self):
        return  self.name
# Payment_user
# - Id
# - User_id
# - Service_id
# - Amount
# - PaymentDate
# - ExpirationDate

class Payment_user(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE)
    service= models.ForeignKey(Services,on_delete=models.CASCADE)
    amount=models.FloatField(default=0.0)
    paymentDate=models.DateField(auto_now_add=True)
    expirationDate=models.DateField()

# Expired_payments
# - Id
# - Payment_user_id
# - Penalty_fee_amount
class Expired_payments(models.Model):
    payment_usuario=models.ForeignKey(User, on_delete=models.CASCADE)
    penalty_fee_amount=models.FloatField(default=0.0)

#ESTE USUARIO YA LO DEFINIMOS USERS
# User
# - Id
# - Email
# - Username
# - Password

