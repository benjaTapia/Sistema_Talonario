# Sistema_Talonario
Este repositorio contiene el desarrollo completo del Sistema Talonario, una aplicación web construida con Django para la gestión de registros y adjuntos, organizada bajo una estructura modular y preparada para entorno de desarrollo local.

1. Estructura del proyecto

```text
.
├─ talonario_project/                ← Proyecto principal Django
│   ├─ logs/
│   ├─ media/
│   │   └─ adjuntos/                 ← Archivos cargados por usuarios
│   │
│   ├─ registros/                    ← Aplicación principal
│   │   ├─ migrations/
│   │   ├─ templates/
│   │   ├─ templatetags/
│   │   ├─ __init__.py
│   │   ├─ admin.py
│   │   ├─ apps.py
│   │   ├─ forms.py
│   │   ├─ models.py
│   │   ├─ scripts.py
│   │   ├─ tests.py
│   │   ├─ urls.py
│   │   └─ views.py
│   │
│   ├─ static/                       ← Archivos estáticos del sistema
│   │   ├─ css/
│   │   ├─ img/
│   │   └─ js/
│   │
│   ├─ staticfiles/                  ← Archivos recolectados (producción)
│   │   ├─ admin/
│   │   ├─ css/
│   │   ├─ django_extensions/
│   │   ├─ img/
│   │   └─ js/
│   │
│   ├─ talonario_project/            ← Configuración central del proyecto
│   │   ├─ __init__.py
│   │   ├─ asgi.py
│   │   ├─ settings.py
│   │   ├─ urls.py
│   │   └─ wsgi.py
│   │
│   ├─ .env
│   ├─ db.sqlite3
│   ├─ manage.py
│   ├─ requirements.txt
│   └─ README.md

```
2. Requisitos previos

   * Python 3.10+

   * pip
  
   * Entorno virtual (venv)


3. Configuración de Base de Datos (Entorno Desarrollo)

   * El sistema está configurado para utilizar SQLite3 en entorno de desarrollo.

Dirígete a:

```text
talonario_project/talonario_project/settings.py
```

Verifica que la configuración de base de datos esté definida de la siguiente manera:


```text
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

4. Configuración del Entorno de Desarrollo

   * Crear entorno virtual

Abrir la terminal dentro del editor de código y ejecutar:



```text
python -m venv venv
```

5. Activar entorno virtual

En Windows:

```text
venv\Scripts\activate
```

Si se activó correctamente, la terminal debería verse similar a:

```text
```text(venv) PS C:\ruta\Sistema_Talonario>
```

6. Acceder al directorio principal

Dirigirse al directorio donde se encuentra manage.py:

```text
cd .\talonario_project\
```

La terminal debería quedar dentro de la carpeta que contiene:

   * manage.py

   * requirements.txt

   * db.sqlite3

7. Instalar dependencias

Con el entorno virtual activo, ejecutar:

```text
pip install -r requirements.txt
```

8. Ejecución del Sistema

Una vez completados los pasos anteriores, ejecutar:

```text
python manage.py runserver
```

El sistema quedará disponible en:

```text
[pip install -r requirements.txt](http://127.0.0.1:8000/)
```

Componentes Principales

📌 Aplicación registros

Contiene la lógica principal del sistema:

   * models.py → Modelos de base de datos.

   * views.py → Lógica de negocio.

   * forms.py → Formularios.

   * admin.py → Configuración del panel administrativo.

   * urls.py → Rutas de la aplicación.

   * templates/ → Plantillas HTML.

   * templatetags/ → Filtros personalizados.

   * migrations/ → Control de versiones de base de datos.

📁 Media y Archivos Adjuntos

Los archivos cargados por los usuarios se almacenan en:

```text
media/adjuntos/
```

Archivos Estáticos

Ubicados en:

```text
static/
```

Incluye:

   * CSS

   * JavaScript

   * Imágenes

La carpeta staticfiles/ corresponde a los archivos recolectados para producción.

📌 Comandos Útiles


Aplicar migraciones:

```text
python manage.py makemigrations
python manage.py migrate
```

Crear superusuario:

```text
python manage.py createsuperuser
```

Acceder al panel admin:

```text
http://127.0.0.1:8000/admin/
```

📌 Orden Recomendado de Ejecución

   * Configurar base de datos en settings.py

   * Crear entorno virtual

   * Activar entorno virtual

   * Instalar dependencias

   * Ejecutar migraciones

   * Ejecutar servidor

   * (Opcional) Crear superusuario

📝 Notas Finales

   * El proyecto está configurado para entorno local.

   * Utiliza SQLite3 en desarrollo.

   * La estructura está preparada para escalar a entornos de producción.

   * Se recomienda no subir la carpeta venv/ al repositorio.

   * El archivo .env puede utilizarse para variables sensibles si se configura en producción.
