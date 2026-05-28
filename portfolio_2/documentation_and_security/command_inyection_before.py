import os
import shutil
import platform
import subprocess

class SystemDiagnostics:
    """
    Herramienta de diagnóstico de sistema para servidores de backend.
    Proporciona información sobre recursos, red y logs.
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
        if self.os_type == "Windows":
            cmd = f"ping -n 1 {target_host}"
        else:
            cmd = f"ping -c 1 {target_host}"
            
        # os.popen() ejecuta el comando a través de la shell del sistema.
        output = os.popen(cmd).read()
        return output