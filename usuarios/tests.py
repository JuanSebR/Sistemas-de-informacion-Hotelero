from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

Usuario = get_user_model()


class UsuarioModelTests(TestCase):
    def test_creacion_usuario_roles(self):
        # Cliente
        u1 = Usuario.objects.create_user(username='cliente1', password='Password123!', rol=Usuario.Rol.CLIENTE)
        self.assertEqual(u1.rol, Usuario.Rol.CLIENTE)
        self.assertEqual(str(u1), 'cliente1 (Cliente)')

        # Recepcionista
        u2 = Usuario.objects.create_user(username='recep1', password='Password123!', rol=Usuario.Rol.RECEPCIONISTA)
        self.assertEqual(u2.rol, Usuario.Rol.RECEPCIONISTA)

        # Gerente
        u3 = Usuario.objects.create_user(username='gerente1', password='Password123!', rol=Usuario.Rol.GERENTE)
        self.assertEqual(u3.rol, Usuario.Rol.GERENTE)

        # Admin
        u4 = Usuario.objects.create_superuser(username='admin1', password='Password123!', email='admin@hotel.com')
        u4.rol = Usuario.Rol.ADMIN
        u4.save()
        self.assertEqual(u4.rol, Usuario.Rol.ADMIN)
        self.assertTrue(u4.is_superuser)

    def test_rol_por_defecto_es_cliente(self):
        u = Usuario.objects.create_user(username='default_user', password='Password123!')
        self.assertEqual(u.rol, Usuario.Rol.CLIENTE)


class UsuarioAuthViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Usuario.objects.create_user(
            username='carlos',
            email='carlos@hotel.com',
            first_name='Carlos',
            last_name='Gomez',
            password='TestPassword123!',
            rol=Usuario.Rol.CLIENTE
        )

    def test_get_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/login.html')

    def test_get_registro_page(self):
        response = self.client.get(reverse('registro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/registro.html')

    def test_post_registro_usuario_exitoso(self):
        datos = {
            'username': 'nuevo_huesped',
            'first_name': 'Ana',
            'last_name': 'Martínez',
            'email': 'ana@hotel.com',
            'password1': 'SeguraPass2026!',
            'password2': 'SeguraPass2026!',
        }
        response = self.client.post(reverse('registro'), data=datos, follow=True)
        self.assertEqual(response.status_code, 200)
        
        nuevo_user = Usuario.objects.filter(username='nuevo_huesped').first()
        self.assertIsNotNone(nuevo_user)
        self.assertEqual(nuevo_user.rol, Usuario.Rol.CLIENTE)
        self.assertEqual(nuevo_user.first_name, 'Ana')

    def test_login_y_logout_exitoso(self):
        # Login
        response = self.client.post(reverse('login'), {
            'username': 'carlos',
            'password': 'TestPassword123!'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

        # Acceder a Home autenticado
        home_resp = self.client.get(reverse('home'))
        self.assertEqual(home_resp.status_code, 200)
        self.assertContains(home_resp, 'Carlos')
        self.assertContains(home_resp, 'Cliente')

        # Logout
        logout_resp = self.client.get(reverse('logout'), follow=True)
        self.assertEqual(logout_resp.status_code, 200)
        self.assertFalse(logout_resp.context['user'].is_authenticated)

    def test_acceso_home_anonimo_redirige_a_login(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
