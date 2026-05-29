import os
import shutil
import platform
import subprocess
import re

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
        # Validar el valor de target_host: permitir solo hostnames e IPs válidas
        def _is_valid_target(host: str) -> bool:
            if not host or len(host) > 255:
                return False
            # IPv4 simple
            ipv4 = re.match(r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', host)
            if ipv4:
                try:
                    parts = [int(p) for p in host.split('.')]
                    return all(0 <= p <= 255 for p in parts)
                except Exception:
                    return False

            # Hostname (labels separated by dots, allowed chars: a-zA-Z0-9-)
            hostname_re = re.compile(r'^(?=.{1,255}$)([a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)(?:\.(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?))*$')
            return bool(hostname_re.match(host))

        if not _is_valid_target(target_host):
            return f"Error: target_host inválido: {target_host}"

        # Construir comando como lista (no usar shell) y ejecutar con timeout
        if self.os_type == "Windows":
            cmd = ["ping", "-n", "1", target_host]
        else:
            cmd = ["ping", "-c", "1", target_host]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                return result.stdout
            else:
                return result.stderr or f"Ping falló con código {result.returncode}"
        except subprocess.TimeoutExpired:
            return "Error: ping agotó el tiempo de espera"
        except Exception as e:
            return f"Error ejecutando ping: {e}"
    