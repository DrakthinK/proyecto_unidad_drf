from time import sleep
from celery import shared_task

@shared_task
def comprobar_expiracion(nombre='prueba', mail='prueba'):
    sleep(20)  # Simula operaciones muy pesadas que congelan a Django
    print(
        nombre + " " + mail
    )