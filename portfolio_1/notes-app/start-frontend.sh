#!/bin/bash

# Script para ejecutar el frontend en macOS/Linux

echo "🚀 Iniciando Servidor Frontend React..."
echo ""

cd frontend

# Instalar dependencias si no existen
if [ ! -d "node_modules" ]; then
    echo "📥 Instalando dependencias..."
    npm install
fi

echo ""
echo "✨ Servidor corriendo en http://localhost:3000"
echo "Presiona Ctrl+C para detener"
echo ""

npm start
