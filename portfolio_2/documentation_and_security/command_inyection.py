"""
Herramienta de diagnóstico del sistema con énfasis en seguridad.

Este módulo ofrece utilidades para obtener información del sistema,
uso de disco y lectura de logs. Contiene funciones que ejecutan
comandos del sistema; dichos puntos requieren precaución para evitar
inyección de comandos y concesión de privilegios innecesarios.

Como regla general:
- Evitar ejecutar comandos construidos como cadenas por la shell.
- Usar `subprocess.run` con listas de argumentos (`shell=False`).
- Validar y/o normalizar cualquier entrada que provenga del usuario.
"""

import os
import shutil
import platform
import subprocess

class SystemDiagnostics:
    """
    Herramienta de diagnóstico de sistema para servidores de backend.
    Proporciona información sobre recursos, red y logs.

        Nota de seguridad:
        - Algunas funciones interactúan con el sistema operativo y pueden
            exponer riesgos si se les pasa entrada controlada por un atacante.
        - No llame a los métodos que ejecutan comandos de sistema con
            parámetros no validados desde interfaces públicas (e.g., APIs
            expuestas a usuarios finales).
    """
    def __init__(self):
        self.os_type = platform.system()
        self.hostname = platform.node()

    def get_system_summary(self) -> dict:
        """Retorna un resumen de la información del sistema operativo."""
        return {
            "OS": self.os_type,
            "Hostname": self.hostname,
            "Release": platform.release(),
            "Architecture": platform.machine()
        }

    def get_disk_usage(self, path: str = "/") -> dict:
        """Verifica el uso de disco para la ruta dada."""
        total, used, free = shutil.disk_usage(path)
        return {
            "path": path,
            "total_gb": round(total / (2**30), 2),
            "used_gb": round(used / (2**30), 2),
            "free_gb": round(free / (2**30), 2),
            "percent_used": round((used / total) * 100, 2)
        }

    def read_last_log_lines(self, filename: str, lines: int = 10) -> list:
        """Lee las últimas N líneas de un archivo de log si existe."""
        if not os.path.exists(filename):
            return [f"Error: El archivo {filename} no existe."]
        
        try:
            with open(filename, 'r') as file:
                all_lines = file.readlines()
                return [line.strip() for line in all_lines[-lines:]]
        except Exception as e:
            return [f"Error al leer el archivo: {str(e)}"]

    def network_ping_trace(self, target_host: str) -> str:
        """
        [USO INTERNO - SOLO ADMINS]
        Realiza una traza de red (ping) hacia un host destino.
        Útil para diagnosticar problemas de conectividad rápida.
        """
        # Construimos la lista de argumentos en lugar de una cadena.
        if self.os_type == "Windows":
            args = ["ping", "-n", "1", target_host]
        else:
            args = ["ping", "-c", "1", target_host]

        # Ejecutar sin shell reduce el vector de inyección de comandos.
        try:
            # timeout evita procesos colgados; captura la salida como texto.
            completed = subprocess.run(
                args,
                capture_output=True,
                text=True,
                shell=False,
                timeout=10
            )

            # Retornar stdout o, si hay error, stderr para facilitar
            # diagnóstico; en producción lo ideal es registrar los
            # errores y retornar un mensaje genérico al usuario.
            if completed.returncode == 0:
                return completed.stdout
            else:
                return completed.stderr or f"Comando finalizado con código {completed.returncode}"
        except subprocess.TimeoutExpired:
            return "Error: la operación de ping excedió el tiempo límite."
        except FileNotFoundError:
            return "Error: comando 'ping' no disponible en el sistema."
        except Exception as e:
            # Evitar exponer trazas internas en interfaces públicas.
            return f"Error al ejecutar ping: {str(e)}"