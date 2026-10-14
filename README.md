# Sistemas de Información Hotelero - Hotel Eclipse

Sistema de gestión hotelera desarrollado en **Django**, enfocado en la administración de reservas, control operativo, habitaciones, tarifas y perfiles de usuarios.

##  Módulos del Sistema

### Módulo 1: Usuarios y Autenticación (Implementado)
- Modelo de usuario personalizado (`Usuario`) heredando de `AbstractUser`.
- 4 roles diferenciados:
  - **`CLIENTE`**: Registro público y consulta de reservas.
  - **`RECEPCIONISTA`**: Gestión de check-in / check-out y atención operativa.
  - **`GERENTE`**: Supervisión, reportes y control de tarifas.
  - **`ADMIN`**: Control técnico y administrativo total.
- Vistas completas de inicio de sesión (`login`), registro de usuarios (`registro`), cierre de sesión (`logout`) y dashboard de bienvenida (`home`).
- Plantillas responsivas con Bootstrap 5 bajo la identidad de diseño **Hotel Eclipse**.
- Gestión de usuarios y roles adaptada en el panel de Django Admin.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.14+**
- **Django 6.1.1**
- **SQLite3** (Base de datos por defecto para desarrollo)
- **Bootstrap 5** & **Bootstrap Icons** (Frontend)

---

## 🚀 Instalación y Puesta en Marcha

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/JuanSebR/Sistemas-de-informacion-Hotelero.git
   cd Sistemas-de-informacion-Hotelero
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   # En Linux / Mac:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario (Administrador):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
   Accede en el navegador a: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Pruebas Unitarias

Para ejecutar la suite de pruebas del módulo de autenticación:
```bash
python manage.py test
```
