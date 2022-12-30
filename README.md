# proyecto_unidad_drf
#PASOS PARA PROBAR LA APLICACION WEB
#INICIAR DJANGO-PROYECTO
1.-crear entorno virtual 
2.- ejecutar los modulos pip install -r requirements.txt
3.- ejecutar las migraciones :python manage.py migrate
3.- ejecutar el script en la base de datos de su preferencia(por defecto esta mysql):OBLIGATORIO//PORQUE MI API NO PUEDE CREAR SERVICIOS DESDE API,POR RESTRINCION DEL ENUNCIADO
create database apipayments_services;
use apipayments_services;
INSERT INTO pagos_services(name,description,logo) values
('Netflix','plataforma de peliculas y series','N.jpg'),
('Amazon Video','plataforma de series','AP.jpg'),
('HBO','plataforma de peliculas','HBO.jpg')
4.- Crear Usuario para probar las apis(se usa JWT) OBLIGATIRO
5.- Logearse con el usuario, y probar las api con su herramienta preferida (POSTMAN,CURL)
6.- PORBAR LA APLICACION CON EL SIGUIENTE PROYECTO(LA PARTE DEL CONSUMO DE LA API)-PROYECTO PARTE 2:
https://github.com/DrakthinK/proyecto_unidad_frontend
se puede crear usuarios desde la misma
