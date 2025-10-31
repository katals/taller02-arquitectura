import os
import socket

def get_container_id() -> str:
    # Prioriza variable de entorno si existe
    env_id = os.getenv("CONTAINER_ID")
    if env_id:
        return env_id
    # Si no, usa el hostname (Docker lo setea con el container id corto)
    return socket.gethostname()
