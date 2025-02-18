import requests
import hashlib
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.contrib.auth.models import Group

User = get_user_model()

SPRING_AUTH_URL = "http://localhost:8080/login"  # URL del servicio en Spring Boot

class SpringBootAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None  # Retorna None si no hay credenciales

        # 🔹 Encriptar la contraseña antes de enviarla a Spring Boot
        encrypted_password = self.encrypt_password(password)

        # 🔹 Crear un diccionario con los datos a enviar en el cuerpo de la solicitud
        payload = {
            'username': username,
            'password': encrypted_password
        }

        try:
            # 🔹 Consultar el servicio de autenticación en Spring Boot
            response = requests.post(SPRING_AUTH_URL,json=payload)

            if response.status_code == 200:
                data = response.json()
                print("✅ Respuesta del servidor Spring Boot:", data)
                # 🔹 Si el usuario es autenticado en Spring Boot, buscarlo en Django
                if data == 0:
                    return None
                
                # 🔹 Si la autenticación es exitosa, verificar si el usuario ya existe
                user, created = User.objects.get_or_create(username=username)

                if created:
                    user.set_password(password)  # Guardar la contraseña correctamente en Django
                    user.email = data.get("email", "")  # Asignar el email si existe en la respuesta
                    user.first_name = data.get("first_name", "")
                    user.last_name = data.get("last_name", "")
                    user.is_staff = True  # Convertirlo en staff si es necesario
                    # 🔹 Agregar al grupo "BDD"
                    try:
                        grupo = Group.objects.get(name="BDD")
                        user.groups.add(grupo)
                    except Group.DoesNotExist:
                        print("⚠️ El grupo 'BDD' no existe")
                    user.save()

                # 🔹 Establecer manualmente el backend usado
                user.backend = 'login.auth_backends.SpringBootAuthBackend'  # 📌 Cambia esto por el path real de tu backend

                # 🔹 Si `request` está disponible, iniciar sesión en Django
                if request:
                    login(request, user, backend=user.backend)  # 🔥 Solución aquí

                return user  # Usuario autenticado

        except requests.RequestException as e:
            print(f"❌ Error al conectar con Spring Boot: {e}")
            return None  # Retorna None si hay un error en la conexión

        # 🔹 Si la autenticación falla en Spring Boot, intentar con la autenticación de Django
        return super().authenticate(request, username=username, password=password)

    def encrypt_password(self, password):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        return sha256_hash.hexdigest()
        