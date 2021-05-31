# primerProyectoDjango

1) Crear proyecto django
    django-admin startproject xxx
    cd xxx

2) configuración mínima de setting del proyecto

    xxx/xxx/settings  lenguage_code en --> es

*) Agregar archivo .gitignore
        https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

3) Crear la app de django principal (core)
    python manage.py startapp core  
    agregar app core a settings en installed apps

4) Dentro de core, crear carpetas templates/core
    nombreapp/templates/nombreapp

    - Creo el template  home.html dentro de templates/core
    - En el archivo views.py agregó la función 
        def home(request):
            return render(request, 'core/home.html')

5) Agregar el archivo urls.py a la carpeta core con el código

    from django.urls import path
    from .views import home


    urlpatterns = [
         path('', home, name='home'),

    En el archivo urls.py general del proyecto agregar
     path('', include('core.urls'))
     Recordar impotar include, junto con path


6) Archivos estáticos

    Crear una carpeta static con la  lógica similar a templates
    nombreapp/static/nombreapp

    Crear dentro de esa carpeta, una estructura ordenada con carpetas: js, img, lib, css.

    En el html del template de django, primero se debe cargar los archivos staticos de la app.

    {%load static%}

    Luego llamar al recurso, ejemplo
    <img src="{% static 'core/img/millenial.jpg'%}" >
