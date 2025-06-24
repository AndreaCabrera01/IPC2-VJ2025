from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests #pip install requests
from .forms import LoginForm, FileForm
import json


api_url = 'http://127.0.0.1:5000'


# Create your views here.
def index(request):
    return render(request, 'login.html')

def iniciarSesion(request):
    try:
        if request.method == 'POST':
            print('Recibiendo los datos del formulario:')
            form = LoginForm(request.POST)

            print("FORMULARIO RECIBIDO", form)

            if form.is_valid():
                print("FORMULARIO VÁLIDO")
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                datos_enviar = json.dumps({
                    'username': username,
                    'password': password
                })

                headers = {
                    'Content-Type': 'application/json'
                }

                response = requests.post(f'{api_url}/login', data=datos_enviar, headers=headers)
                response_json = response.json()

                print("DATOS ENVIADOS AL BACKEND")
                print(response_json)

                if response.status_code == 200:
                    rol = int(response_json['role'])
                    print(f"Rol del usuario: {rol}")

                    if rol == 0:
                        redireccionar = redirect('admin_dashboard')
                        redireccionar.set_cookie('logueado', username)
                        return redireccionar
                        
                    else:
                        return HttpResponse("Rol aún no manejado", status=200)
                else:
                    return render(request, 'login.html', {
                        'form': form,
                        'error': response_json.get("error", "Error desconocido")
                    })
            return render(request, 'login.html', {'form': LoginForm()})

    except Exception as e:
        print(f'Error al iniciar sesion: {e}')
        return HttpResponse('Error interno al procesar la solicitud.', status=500)
    

def admin_dashboard(request):
    try:
        # Verificar si el usuario está logueado
        if request.COOKIES.get('logueado'):
            username = request.COOKIES.get('logueado')
            print(f"Usuario logueado: {username}")
            return render(request, 'admin_dashboard.html', {'username': username})
        else:
            return redirect('iniciarSesion')
    except Exception as e:
        print(f"Error en el dashboard: {e}")
        return render(request, 'admin_dashboard.html', {'error': 'Error al cargar el dashboard'})
    
def logOut(request):
    try:
        response = requests.post(f'{api_url}/logout')
        if response.status_code != 200:
            print('Error al cerrar sesión en el backend: ', response.json())
            return HttpResponse('Error al cerrar sesión', status=500)
        
        print("Cerrar sesión exitoso")
        response = redirect('index')
        response.delete_cookie('logueado')
        return response
    except Exception as e:
        return HttpResponse('Error al cerrar sesión', status=500)
    
def cargarXML(request):
    xml_content = None
    return render(request, 'upload_xml.html', {'xml_content': xml_content})


def verXML(request):
    xml_content = ""

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        print("MIREMOS LO QUE TRAE ESTE FORMS:")
        print(form)

        if form.is_valid():
            xml_file = request.FILES['xml_file']

            xml_content = xml_file.read().decode('utf-8')

            print(xml_content)
        else:
            print('Formulario inválido: ', form.errors)

    return render(request, 'upload_xml.html', {'xml_content': xml_content})

def subirXML(request):
    response_message = ""
    xml_content = None

    if request.method == 'POST':
        xml_content = request.POST.get('xml_content', '')

        if xml_content:
            try:
                headers = {'Content-Type': 'application/xml'}
                # ENVIARLO AL BACKEND:
                response = requests.post(f'{api_url}/procesarXML', data=xml_content.encode('utf-8'), headers=headers)

                if response.status_code == 200:
                    response_message = "XML procesado correctamente"
                    
                    if response.headers['Content-Type'] == 'application/json':
                        response_data = response.json()
                        response_message = response_data.get('message', response_message)

                else:
                    response_message = f'Error al procesar el XML '
            except Exception as e:
                response_message = f"Error de conexión: {str(e)}"

    return render(request, 'upload_xml.html', {'xml_content': xml_content, 'response': response_message})

def verConfigs(request):
    try:
        # Verificar si el usuario está logueado
        if request.COOKIES.get('logueado'):
            username = request.COOKIES.get('logueado')
            print(f"Usuario logueado: {username}")

            # GET desde el backend para obtener las configuraciones de usuarios:
            response = requests.get(f'{api_url}/verUsuarios')
            print(f"URL de la API: {api_url}/verUsuarios")
            if response.status_code == 200:
                
                usuarios = response.json().get('usuarios', [])
                print(f"Usuarios obtenidos: {usuarios}")
            else:
                print("Error al obtener usuarios:", response.json())
                usuarios = []

            # GET desde el backend para obtener las configuraciones de animales:
            response = requests.get(f'{api_url}/verAnimales')
            if response.status_code == 200:
                animales = response.json().get('animales', [])
                print(f"Animales obtenidos: {animales}")
            else:
                print("Error al obtener animales:", response.json())
                animales = []


            return render(request, 'verConfigs.html', {'users': usuarios, 'animals': animales})
        else:
            return redirect('index')
    except Exception as e:
        print(f"Error al cargar configuraciones: {e}")
        return render(request, 'verConfigs.html', {'error': 'Error al cargar las configuraciones'})
    