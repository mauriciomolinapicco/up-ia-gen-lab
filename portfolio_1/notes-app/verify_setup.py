#!/usr/bin/env python
"""
Script de verificación de instalación
Ejecuta: python verify_setup.py
"""

import os
import sys
import subprocess

def check_python():
    """Verificar versión de Python"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor} instalado")
        return True
    else:
        print(f"❌ Se requiere Python 3.8+, tienes {version.major}.{version.minor}")
        return False

def check_nodejs():
    """Verificar Node.js"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js {result.stdout.strip()} instalado")
            return True
    except FileNotFoundError:
        pass
    print("❌ Node.js no está instalado")
    return False

def check_npm():
    """Verificar npm"""
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ npm {result.stdout.strip()} instalado")
            return True
    except FileNotFoundError:
        pass
    print("❌ npm no está instalado")
    return False

def check_project_structure():
    """Verificar estructura del proyecto"""
    files_to_check = [
        'backend/manage.py',
        'backend/requirements.txt',
        'backend/config/settings.py',
        'backend/notes_app/models.py',
        'frontend/package.json',
        'frontend/src/App.js',
        'README.md',
        'QUICKSTART.md',
    ]
    
    all_present = True
    for file in files_to_check:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} no encontrado")
            all_present = False
    
    return all_present

def main():
    print("=" * 50)
    print("🔍 VERIFICACIÓN DE SETUP")
    print("=" * 50)
    print()
    
    print("📋 Verificando requisitos del sistema:")
    python_ok = check_python()
    nodejs_ok = check_nodejs()
    npm_ok = check_npm()
    
    print()
    print("📁 Verificando estructura del proyecto:")
    structure_ok = check_project_structure()
    
    print()
    print("=" * 50)
    
    if python_ok and nodejs_ok and npm_ok and structure_ok:
        print("✅ ¡Todo está listo! Ejecuta:")
        print()
        print("   Terminal 1 (Backend):")
        print("   cd backend && python3 -m venv venv && source venv/bin/activate")
        print("   pip install -r requirements.txt")
        print("   python manage.py migrate")
        print("   python manage.py runserver")
        print()
        print("   Terminal 2 (Frontend):")
        print("   cd frontend && npm install && npm start")
        print()
    else:
        print("❌ Faltan dependencias. Instala:")
        if not python_ok:
            print("   - Python 3.8+")
        if not nodejs_ok:
            print("   - Node.js (https://nodejs.org)")
        if not npm_ok:
            print("   - npm (viene con Node.js)")

if __name__ == '__main__':
    main()
