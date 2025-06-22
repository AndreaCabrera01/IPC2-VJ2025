from django.shortcuts import render
from .forms import FileForm


respuesta_default = {
    "status": "OK",
    "message": "SE RECIBIÓ UN XML",
    "status_code": 200
}

libros = [
    {
        "id": 1,
        "imagen": "https://tienda.sophosenlinea.com/images/portadas/14029-978847888629.jpg",
        "titulo": "El Principito",
        "descripcion": "Un libro sobre un joven príncipe que viaja por el universo.",
        "autor": "Antoine de Saint-Exupéry",
        "anio_publicacion": 1943
    },
    {
        "id": 2,
        "imagen": "https://tunovela.es/wp-content/uploads/Cien-anos-de-soledad-de-Gabriel-Garcia-Marquez-resumen-y-analisis.jpg",
        "titulo": "Cien años de soledad",
        "descripcion": "Una novela que narra la historia de la familia Buendía en el pueblo ficticio de Macondo.",
        "autor": "Gabriel García Márquez",
        "anio_publicacion": 1967
    },
    {
        "id": 3,
        "imagen": "https://silverlibros.com/wp-content/uploads/2023/03/978849989094.jpg",
        "titulo": "1984",
        "descripcion": "Una novela distópica que explora temas de vigilancia y totalitarismo.",
        "autor": "George Orwell",
        "anio_publicacion": 1949
    },
    {
        "id": 1,
        "imagen": "https://tienda.sophosenlinea.com/images/portadas/14029-978847888629.jpg",
        "titulo": "El Principito",
        "descripcion": "Un libro sobre un joven príncipe que viaja por el universo.",
        "autor": "Antoine de Saint-Exupéry",
        "anio_publicacion": 1943
    },
    {
        "id": 2,
        "imagen": "https://tunovela.es/wp-content/uploads/Cien-anos-de-soledad-de-Gabriel-Garcia-Marquez-resumen-y-analisis.jpg",
        "titulo": "Cien años de soledad",
        "descripcion": "Una novela que narra la historia de la familia Buendía en el pueblo ficticio de Macondo.",
        "autor": "Gabriel García Márquez",
        "anio_publicacion": 1967
    },
    {
        "id": 3,
        "imagen": "https://silverlibros.com/wp-content/uploads/2023/03/978849989094.jpg",
        "titulo": "1984",
        "descripcion": "Una novela distópica que explora temas de vigilancia y totalitarismo.",
        "autor": "George Orwell",
        "anio_publicacion": 1949
    }
]


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cargarXML(request):
    return render(request, 'subirArchivo.html')

def verXML(request):
    xml_content = ""
    print("PRUEBA 1")
    

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data['file']
            xml_content = file.read().decode('utf-8')

        else:
            print(form.errors)
        return render(request, 'subirArchivo.html', {'xml_content': xml_content})
    
def subirXML(request):
    xml_content = ""
    if request.method == 'POST':
        xml_content = request.POST.get('xml', '')

        cleaned_xml = xml_content.encode('utf-8')
        print("RESPUESTA: ", cleaned_xml)

        # AQUI USTEDES LO DEBEN DE MANDAR AL BACKEND
        # respuesta = lo_del_backend
    
    return render(request, 'subirArchivo.html', {'xml_content': xml_content, 'response': respuesta_default['message'] })


def verLibros(request):
    ### Obtener desde el backend la información:
    return render(request, 'verLibros.html', {'libros': libros})