from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests #pip install requests
from .forms import LoginForm
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