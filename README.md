# Gestor [Documentación en construcción] [18/01/21] :rocket:

Módulo independiente de gestión de Empleador y Departamentos para control de empresa desarrollado en Django 3.1

## ¿Qué hace el proyecto? :satellite:

Permite operaciones CRUD para Empleados y Departamentos, relacionando estos modelos y almacenando la información en una base de datos.

## ¿Cómo obtener ayudar? :heavy_exclamation_mark:

Actualmente el Software no cuenta con un módulo de ayuda, sin embargo es posible solicitar ayuda formal por este medio o ayuda un poco más informal en la red social del desarrollador: [@Janobourian][twitter]

## Paquetes necesarias para ejecución :heavy_check_mark:

Python 3.9.1

pip install asgiref==3.2.7

pip install django==3.1.\*

pip install django-model-utils==4.0.0

pip install psycopg2-binary==2.8.5

pip install pytz==2019.3

pip install sqlparse==0.3.1

pip install unipath==1.1

## ¿Cómo comenzar? :part_alternation_mark:

Para comenzar debe crear un entorno virtual (con venv o conda) e instalar las dependencias indicadas en **Dependencias necesarias para ejecución**. Clone el repositorio y puede comenzar a ejecutar escribiendo en la raíz del proyecto (a la altura del _manage.py_): python manage.py runserver.

Nota: Es necesario contar con un navegador web, ya que es aquí donde se ejecuta y visualiza el software.

Una vez logrado esto puede comenzar a explorar las funciones disponibles. Puede agregar recomendaciones para nuevas funcionalidades, módulos o mejoras para la experiencia e interfaz de usuario por este medio a la red social del desarrollador: [@Janobourian][twitter]

## Información Importante :loudspeaker: :bangbang:

### Base de datos :elephant:

Aunque por defecto podríamos utilizar SDQLite, para fines de integración y mantenimiento el gestor de base de datos que utiliza _Gestor_ es _PostgreSQL_. La instalación del gestor de base de datos no es parte de esta documentación, sin embargo los canales de comunicación están abiertos para resolver cualquier duda.

- database: empresadb

- usuario: ruleadmin

- contraseña: password

## Mantenimiento y soporte :link:

Desarrollo mantenido y soportado por: [@Janobourian][twitter]

## Sobre el uso :copyright:

Siéntase con la libertad de clonar, utilizar y distribuir este software siempre y cuando no se realice cobro alguno por el mismo o las posibles mejoras realizadas por el equipo de trabajo.

[twitter]: https://twitter.com/JanoBourian
