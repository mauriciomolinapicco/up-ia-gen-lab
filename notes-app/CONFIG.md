# Configuración de ejemplo (opcional)

## Variables de entorno

Puedes crear un archivo `.env` en la carpeta `backend/` para configuraciones específicas:

```
DEBUG=True
SECRET_KEY=tu-clave-secreta-aqui
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

## Configuración CORS

CORS está preconfigurado para `http://localhost:3000` en `backend/config/settings.py`.

Para agregar más orígenes, modifica:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://tu-dominio.com",  # Agregar más aquí
]
```

## Configuración de la Base de Datos

La BD SQLite se crea automáticamente en `backend/db.sqlite3`.

Para usar PostgreSQL:
1. Instala: `pip install psycopg2-binary`
2. Cambia en `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'notas_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Variables de Entorno del Frontend

El frontend usa `http://localhost:8000/api` por defecto.

Para cambiar, crea un archivo `.env` en `frontend/`:

```
REACT_APP_API_URL=http://localhost:8000/api
```

Y actualiza `frontend/src/services/noteService.js`:

```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';
```
