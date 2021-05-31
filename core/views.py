from django.shortcuts import render


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__( )
        


def home(request):

    hijo = Persona("Bambina", 12)
    lista = ["napoli", "colo-colo"]
    contexto = {
        "nombre": "Vicente Carmona",
        "edad": 32,
        "equipos": lista,
        "hijo": hijo,
    }
    return render(request, 'core/home.html', contexto)
