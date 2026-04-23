# 🚀 GUÍA RÁPIDA DE INICIO

## Opción 1: Ejecución Manual (Recomendado para aprender)

### Terminal 1 - Backend Django
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Resultado**: Servidor en `http://localhost:8000`

### Terminal 2 - Frontend React
```bash
cd frontend
npm install
npm start
```

**Resultado**: Aplicación en `http://localhost:3000`

---

## Opción 2: Scripts Automáticos (Solo macOS/Linux)

### Hacer los scripts ejecutables
```bash
chmod +x start-backend.sh
chmod +x start-frontend.sh
```

### Ejecutar en dos terminales
```bash
# Terminal 1
./start-backend.sh

# Terminal 2
./start-frontend.sh
```

---

## ✅ Verificación

Si todo está funcionando correctamente:

1. **Backend**: Ve a `http://localhost:8000/api/notes/` - Deberías ver `[]` (lista vacía)
2. **Frontend**: Ve a `http://localhost:3000` - Verás la aplicación de notas
3. **Crear nota**: Llena el formulario y haz clic en "Crear Nota"
4. **Ver nota**: Haz clic en la tarjeta de la nota para ver detalles

---

## 📱 Primera Nota de Prueba

Título: `Mi primera nota`  
Contenido: `¡Hola! Esta es mi primer nota guardada en Django y React.`

---

## 🛑 Para Detener los Servidores

- Presiona `Ctrl + C` en ambas terminales

---

## 📘 Próximos Pasos

1. **Explora el código** en `backend/notes_app/` y `frontend/src/`
2. **Modifica los estilos** en `frontend/src/App.css`
3. **Agrega fields** a la nota (ej: categoría, etiquetas)
4. **Implementa autenticación** con JWT
5. **Deploy** a producción

---

## 🆘 Problemas Comunes

| Problema | Solución |
|----------|----------|
| Puerto 8000 en uso | `python manage.py runserver 8001` |
| Puerto 3000 en uso | `PORT=3001 npm start` |
| Module not found | `pip install -r requirements.txt` o `npm install` |
| CORS error | Verifica que Django está en `http://localhost:8000` |
| Cambios no se guardan | Verifica que SQLite está en `backend/db.sqlite3` |

---

¡Listo para empezar! 🎉
