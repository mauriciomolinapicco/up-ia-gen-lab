# 📚 Documentación Técnica

## Arquitectura General

```
┌─────────────────────────────────────────────────────┐
│                    FRONTEND (React)                 │
│  - App.js (Estado y orquestación)                   │
│  - Components (CreateNoteForm, NoteList, etc.)      │
│  - Services (noteService.js - Comunicación API)     │
└─────────────────────────────────────────────────────┘
                         ↓ (Axios HTTP)
                    http://localhost:8000
                         ↓
┌─────────────────────────────────────────────────────┐
│                  BACKEND (Django REST)              │
│  - ViewSets (Lógica de notas)                       │
│  - Serializers (Validación y serialización)         │
│  - Models (Estructura de datos)                     │
└─────────────────────────────────────────────────────┘
                         ↓ (ORM Django)
┌─────────────────────────────────────────────────────┐
│                DB (SQLite)                          │
│  - db.sqlite3                                       │
└─────────────────────────────────────────────────────┘
```

---

## Backend - Estructura de Carpetas

```
backend/
├── config/                    # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py           # Configuraciones: BD, apps, CORS, etc.
│   ├── urls.py               # URLs principales y enrutamiento API
│   └── wsgi.py               # Interfaz WSGI para despliegue
├── notes_app/                 # Aplicación principal
│   ├── __init__.py
│   ├── admin.py              # (Extensible para admin)
│   ├── apps.py               # Configuración de la app
│   ├── models.py             # Modelo Note
│   ├── serializers.py        # Validación y serialización
│   ├── views.py              # ViewSet para la API
│   └── tests.py              # Tests (extensible)
├── manage.py                  # Gestor de Django
└── requirements.txt           # Dependencias

```

### Detalles del Backend

#### models.py - Modelo de Datos
```python
class Note(models.Model):
    title = models.CharField(max_length=200)      # Título
    content = models.TextField()                  # Contenido
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha creación
    updated_at = models.DateTimeField(auto_now=True)      # Fecha actualización
```

#### serializers.py - Validación
```python
class NoteSerializer(serializers.ModelSerializer):
    # Valida que title y content no estén vacíos
    # Retorna: id, title, content, created_at, updated_at
```

#### views.py - API REST
```python
class NoteViewSet(viewsets.ModelViewSet):
    # GET    /api/notes/          → list()
    # POST   /api/notes/          → create()
    # GET    /api/notes/{id}/     → retrieve()
    # PUT    /api/notes/{id}/     → update()
    # DELETE /api/notes/{id}/     → destroy()
```

---

## Frontend - Estructura de Carpetas

```
frontend/
├── public/
│   └── index.html            # HTML principal
├── src/
│   ├── components/           # Componentes React
│   │   ├── CreateNoteForm.js # Formulario para crear nota
│   │   ├── NoteList.js       # Lista de notas en grid
│   │   ├── NoteDetail.js     # Vista detallada de nota
│   │   └── LoadingSpinner.js # Indicador de carga
│   ├── services/
│   │   └── noteService.js    # Cliente HTTP (Axios)
│   ├── App.js                # Componente principal
│   ├── App.css               # Estilos
│   └── index.js              # Punto de entrada
├── package.json              # Dependencias NPM
└── .gitignore

```

### Detalles del Frontend

#### App.js - Gestión de Estado
```javascript
// Estados principales:
- notes: Array de todas las notas
- selectedNoteId: ID de nota seleccionada
- selectedNote: Objeto de nota completo
- loading: Indicador de carga
- error: Mensajes de error

// Funciones principales:
- loadNotes()          → Obtiene todas las notas
- loadSelectedNote()   → Obtiene nota por ID
- handleNoteCreated()  → Actualiza lista después de crear
- handleDeleteNote()   → Elimina nota con confirmación
- handleSelectNote()   → Muestra detalle de nota
- handleBack()         → Vuelve a lista de notas
```

#### noteService.js - Comunicación API
```javascript
noteService.getAllNotes()      // GET /api/notes/
noteService.getNoteById(id)    // GET /api/notes/{id}/
noteService.createNote(t, c)   // POST /api/notes/
noteService.updateNote(id, t, c) // PUT /api/notes/{id}/
noteService.deleteNote(id)     // DELETE /api/notes/{id}/
```

#### Componentes

**CreateNoteForm.js**
- Inputs: title (text), content (textarea)
- Validaciones: campos requeridos, sin espacios en blanco
- Muestra spinner mientras se guarda
- Reset del formulario al crear nota exitosamente

**NoteList.js**
- Grid responsivo de tarjetas
- Click en tarjeta abre detalle
- Botón de eliminar (con confirmación)
- Mostrador de fecha de actualización

**NoteDetail.js**
- Muestra titulo completo y contenido
- Metadata: fechas de creación y actualización
- Botón para volver a lista

**LoadingSpinner.js**
- Spinner CSS animado
- Usado en carga inicial

---

## Flujo de Datos

### Crear Nota
```
Usuario escribe → CreateNoteForm valida → noteService.createNote() 
→ POST /api/notes/ → Backend valida → Guarda en BD → 
Response con nota creada → App.loadNotes() → Actualiza lista
```

### Ver Nota
```
Usuario hace click en tarjeta → App.handleSelectNote(id) → 
App.loadSelectedNote(id) → GET /api/notes/{id}/ → 
NoteDetail muestra nota
```

### Eliminar Nota
```
Usuario hace click eliminar → Confirmación → noteService.deleteNote(id) 
→ DELETE /api/notes/{id}/ → Backend elimina → 
App.loadNotes() → Actualiza lista
```

---

## Variables de Estado en App.js

```javascript
const [notes, setNotes] = useState([]);              // Lista de notas
const [selectedNoteId, setSelectedNoteId] = useState(null);  // ID seleccionada
const [selectedNote, setSelectedNote] = useState(null);      // Nota detallada
const [loading, setLoading] = useState(true);        // Cargando?
const [error, setError] = useState('');              // Mensaje error
```

---

## Validaciones

### Frontend (CreateNoteForm.js)
- ✅ Título no vacío (sin espacios)
- ✅ Contenido no vacío (sin espacios)
- ✅ Mostrar errores inline

### Backend (serializers.py y models.py)
- ✅ Validación de campos
- ✅ Retornar mensajes de error claros
- ✅ Clean() en modelo para validaciones adicionales

---

## Manejo de Errores

### Frontend
- Try/catch en todas las llamadas API
- Mostrar banner de error rojo
- Usuario puede cerrar el error
- Log en consola para debugging

### Backend
- Validación de serializer
- Retorno de HTTP 400 para errores de validación
- HTTP 404 para notas no encontradas
- HTTP 201 para creación exitosa

---

## Estilos y Responsive

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

### Componentes
- Encabezado con gradiente
- Grid responsivo con `grid-template-columns: repeat(auto-fill, minmax(250px, 1fr))`
- Tarjetas con hover effect (boxShadow)
- Botones con colores distintivos (verde crear, rojo eliminar, azul atrás)

---

## Performance

- ✅ Lazy loading de notas
- ✅ No recarga innecesaria de lista
- ✅ Spinner mientras se carga
- ✅ Deshabilitación de formulario durante submit

---

## Extensibilidad

### Fácil de agregar:

1. **Nuevos campos a Nota**
   - Cambiar models.py
   - Actualizar serializers.py
   - Actualizar componentes React

2. **Autenticación**
   - Instalar: `djangorestframework-jwt`
   - Agregar middleware
   - Filtar notas por usuario: `Note.objects.filter(user=request.user)`

3. **Búsqueda y filtros**
   - Django: `queryset.filter(title__icontains=query)`
   - React: Estadofilter y onChange en input

4. **Categorías/Etiquetas**
   - Agregar ForeignKey en modelo
   - Crear ViewSet para categorías
   - Mostrar en UI

---

## Base de Datos

### Creación automática
- Se ejecuta con `python manage.py migrate`
- SQLite crea archivo `db.sqlite3` automáticamente

### Inspeccionar datos (Django shell)
```bash
python manage.py shell
>>> from notes_app.models import Note
>>> Note.objects.all()
>>> Note.objects.create(title="Test", content="Contenido")
```

---

## Testing

### Para agregar tests en backend:

```python
# backend/notes_app/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Note

class NoteAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_create_note(self):
        response = self.client.post('/api/notes/', 
            {'title': 'Test', 'content': 'Testing'})
        self.assertEqual(response.status_code, 201)
```

Ejecutar: `python manage.py test`

---

## Despliegue

### Para producción:
1. Cambia `DEBUG = False` en settings.py
2. Usa Gunicorn: `pip install gunicorn`
3. Configura Nginx como reverse proxy
4. Usa variables de entorno para SECRET_KEY
5. Deploy Frontend en Vercel, Netlify o GitHub Pages
6. Deploy Backend en Heroku, PythonAnywhere o AWS

---

Esta arquitectura es **escalable**, **mantenible** y **educativa**. 🚀
