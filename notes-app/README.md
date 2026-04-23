# 📝 Aplicación de Notas - Full Stack

Una aplicación web completa de notas simple construida con **React**, **Django** y **SQLite**.

## 🎯 Características

- ✅ Crear nuevas notas con título y contenido
- ✅ Listar todas las notas guardadas
- ✅ Ver detalles completos de cada nota
- ✅ Eliminar notas
- ✅ Persistencia de datos con SQLite
- ✅ API REST completa
- ✅ Interfaz moderna y responsiva
- ✅ Validación de campos
- ✅ Manejo de errores

## 📋 Estructura del Proyecto

```
notes-app/
├── backend/                 # API Django REST
│   ├── config/             # Configuración del proyecto
│   ├── notes_app/          # Aplicación de notas
│   ├── manage.py           # Gestor de Django
│   └── requirements.txt    # Dependencias Python
└── frontend/               # Interfaz React
    ├── public/             # Archivos públicos
    ├── src/                # Código fuente React
    │   ├── components/     # Componentes React
    │   ├── services/       # Servicios (API)
    │   └── App.js         # Componente principal
    └── package.json        # Dependencias Node

```

## 🚀 Instalación y Ejecución

### Requisitos Previos

- Python 3.8 o superior
- Node.js 14.0 o superior
- npm o yarn

### Paso 1: Configurar el Backend

```bash
# Navegar a la carpeta del backend
cd backend

# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
# En macOS/Linux:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones de la base de datos
python manage.py migrate

# Iniciar el servidor (puerto 8000)
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

### Paso 2: Configurar el Frontend

En otra terminal (sin cerrar el backend):

```bash
# Navegar a la carpeta del frontend
cd frontend

# Instalar dependencias
npm install

# Iniciar el servidor de desarrollo (puerto 3000)
npm start
```

La aplicación estará disponible en: `http://localhost:3000`

## 📡 Endpoints de la API

### Obtener todas las notas
```bash
GET /api/notes/
```

### Crear una nueva nota
```bash
POST /api/notes/
Content-Type: application/json

{
  "title": "Mi Nueva Nota",
  "content": "Contenido de la nota"
}
```

### Obtener una nota específica
```bash
GET /api/notes/{id}/
```

### Actualizar una nota
```bash
PUT /api/notes/{id}/
Content-Type: application/json

{
  "title": "Título actualizado",
  "content": "Contenido actualizado"
}
```

### Eliminar una nota
```bash
DELETE /api/notes/{id}/
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 3.2** - Framework web Python
- **Django REST Framework** - Para la API REST
- **SQLite** - Base de datos
- **Python 3.8+**

### Frontend
- **React 17** - Librería de UI
- **Axios** - Cliente HTTP
- **CSS3** - Estilos

## 📝 Validaciones

- **Título**: Requerido, no puede estar vacío
- **Contenido**: Requerido, no puede estar vacío
- Se eliminan espacios en blanco al validar

## 🎨 Estilos

La aplicación incluye:
- Diseño responsivo (móvil, tablet, desktop)
- Colores modernos con gradiente en encabezado
- Tarjetas de notas en grid
- Animaciones suaves
- Indicadores visuales de carga

## ⚠️ Manejo de Errores

- Validación de campos en frontend y backend
- Mensajes de error claros al usuario
- Indicador de carga durante operaciones
- Confirmación antes de eliminar notas
- Notificación si el servidor no está disponible

## 🔐 Notas de Seguridad

⚠️ **IMPORTANTE**: Esta aplicación está desarrollada con fines educativos. Para producción:
- Cambia la `SECRET_KEY` en `settings.py`
- Establece `DEBUG = False`
- Configura `ALLOWED_HOSTS` apropiadamente
- Usa HTTPS
- Implementa autenticación y autorización
- Valida y sanitiza todas las entradas

## 📚 Estructura de Datos

### Modelo Note
```python
{
  "id": 1,
  "title": "Título de la nota",
  "content": "Contenido completo de la nota",
  "created_at": "2024-04-23T10:30:00Z",
  "updated_at": "2024-04-23T10:30:00Z"
}
```

## 🐛 Solución de Problemas

### Error de conexión al backend
- Asegúrate de que el servidor Django está corriendo en `http://localhost:8000`
- Verifica que CORS está configurado correctamente
- Revisa la consola del navegador para más detalles

### Error de puerto en uso
```bash
# Cambiar puerto del backend (ej: 8001)
python manage.py runserver 8001

# Cambiar puerto del frontend en package.json o:
PORT=3001 npm start
```

### Errores de migración
```bash
# Ejecutar de nuevo las migraciones
python manage.py migrate --run-syncdb
```

## 📖 Ejemplos de Uso

### Crear una nota con cURL
```bash
curl -X POST http://localhost:8000/api/notes/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Mi Primera Nota",
    "content": "Este es el contenido de mi nota"
  }'
```

### Obtener todas las notas
```bash
curl http://localhost:8000/api/notes/
```

## 🎓 Aprendizaje

Este proyecto es excelente para aprender:
- ✅ Full Stack con React y Django
- ✅ Creación de APIs REST
- ✅ Comunicación frontend-backend con Axios
- ✅ Estado en React con hooks
- ✅ ORM de Django
- ✅ CORS en Django
- ✅ Validaciones en frontend y backend

## 📞 Soporte

Si encuentras problemas:
1. Revisa que ambos servidores están corriendo
2. Comprueba la consola del navegador (F12)
3. Revisa los logs del servidor Django
4. Asegúrate de que los puertos 3000 y 8000 están disponibles

## 📄 Licencia

Este proyecto está disponible para fines educativos.

---

**¡Disfruta desarrollando con React y Django!** 🚀
