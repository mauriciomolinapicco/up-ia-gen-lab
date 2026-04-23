#!/bin/bash

# Script para ejecutar el backend en macOS/Linux

echo "🚀 Iniciando Servidor Backend Django..."
echo ""

cd backend

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "✅ Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📥 Instalando dependencias..."
pip install -r requirements.txt > /dev/null 2>&1

# Ejecutar migraciones
echo "🗄️  Aplicando migraciones..."
python manage.py migrate > /dev/null 2>&1

# Iniciar servidor
echo ""
echo "✨ Servidor corriendo en http://localhost:8000"
echo "Presiona Ctrl+C para detener"
echo ""

python manage.py runserver
