from app import create_app

app = create_app()

# if __name__ == "__main__":
#     # Configurable por variables de entorno para evitar problemas del reloader en WSL/montajes
#     # FLASK_DEBUG=1 habilita debug y reloader; por defecto están desactivados
#     import os
#     debug = os.getenv("FLASK_DEBUG", "0") == "1"
#     port = int(os.getenv("PORT", "5000"))
#     app.run(host="0.0.0.0", port=port, debug=debug, use_reloader=debug)
