# views.py
from django.shortcuts import render, redirect 
from .forms import UsuarioForm
from .models import Usuario
from django.http import JsonResponse
from .models import Pelicula
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib import messages





def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')

        # Buscar un usuario con el nombre de usuario proporcionado en tu modelo Usuario
        user = Usuario.objects.filter(nombre_usuario=username).first()

        # Verificar si se encontró un usuario y si la contraseña es correcta
        if user and user.contraseña == password:
            # Si las credenciales son correctas, verificar el tipo de usuario
            if user.tipo_usuario == 'taquillero':
                # Si el usuario es taquillero, redirigir a la interfaz_ta
                request.session['user_id'] = user.id  # Almacenar el ID del usuario en la sesión
                return redirect('interfaz_ta')
            else:
                # Si el usuario es otro tipo, redirigir a la interfaz_sa
                request.session['user_id'] = user.id  # Almacenar el ID del usuario en la sesión
                return redirect('interfaz_sa')
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # Si la solicitud no es POST, mostrar el formulario de inicio de sesión
        return render(request, 'login.html')


def interfaz_sa(request):
    usuarios = Usuario.objects.all()  # Obtener todos los usuarios de la base de datos
    return render(request, 'interfaz_sa.html', {'usuarios': usuarios})



def interfaz_ta(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'interfaz_ta.html', {'peliculas': peliculas})
def guardar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interfaz_sa')  
    else:
        form = UsuarioForm()
    return render(request, 'guardar_usuario.html', {'form': form})


def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    # Lógica para eliminar el usuario
    usuario.delete()
    return redirect('interfaz_sa')


def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        # Obtener los nuevos datos del formulario
        nombre_usuario = request.POST.get('nombre_usuario')
        tipo_usuario = request.POST.get('tipo_usuario')
        estado = request.POST.get('estado')

        # Actualizar el usuario con los nuevos valores
        usuario.nombre_usuario = nombre_usuario
        usuario.tipo_usuario = tipo_usuario
        usuario.estado = estado
        usuario.save()  # Guardar los cambios en la base de datos

        # Retornar un JSON con el mensaje de éxito
        return JsonResponse({'success': True, 'message': 'Usuario editado exitosamente'})

    return render(request, 'editar_usuario.html', {'usuario': usuario})


def peliculas(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        
        # Verificar si ya existe una película con el mismo título
        if Pelicula.objects.filter(titulo=titulo).exists():
            return JsonResponse({'error': 'Ya existe una película con este título.'}, status=400)
        
        # Resto del código para guardar la película
        sinopsis = request.POST.get('sinopsis')
        duracion = request.POST.get('duracion')
        genero = request.POST.get('genero')
        estado = request.POST.get('estado')
        imagen = request.FILES.get('imagen')
        precio = request.POST.get('precio')
        
        pelicula = Pelicula(titulo=titulo, sinopsis=sinopsis, duracion=duracion, genero=genero, estado=estado, imagen=imagen, precio=precio)
        pelicula.save()
        
        return JsonResponse({'message': 'Película agregada exitosamente.'})
    elif request.method == 'GET':
        peliculas = Pelicula.objects.all()
        return render(request, 'peliculas.html', {'peliculas': peliculas})
    else:
        return HttpResponseNotFound()




    #Elimar una pelicula
def eliminar_pelicula(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')  # Obtener el título de la película a eliminar
        peliculas_a_eliminar = Pelicula.objects.filter(titulo=titulo)  # Buscar todas las películas con ese título
        peliculas_a_eliminar.delete()  # Eliminar todas las películas encontradas
        return redirect('peliculas')  # Redirigir a la página de películas después de la eliminación
    else:
        # Manejar otras solicitudes HTTP
        return HttpResponseNotFound()
    
def guardar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            tipo_usuario = form.cleaned_data['tipo_usuario']
            estado = form.cleaned_data['estado']
            
            # Verificar si ya existe un usuario con el mismo nombre de usuario
            if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
                
                messages.error(request, error_message)  # Agregar el mensaje de error a la lista de mensajes
                return redirect('interfaz_sa')  # Redirigir de vuelta a la página de interfaz_sa
            
            # Si el usuario no existe, guardar el usuario
            form.save()
            return redirect('interfaz_sa')  
    else:
        form = UsuarioForm()
    return render(request, 'guardar_usuario.html', {'form': form})


def home(request):
    return render(request, 'home.html')   