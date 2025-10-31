import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(env_path)

S3_BUCKET = os.getenv('S3_BUCKET')

def get_image_url(image_name):
    """
    Construye la URL pública de una imagen en S3
    """
    # Si ya viene una URL absoluta, retornar tal cual
    if not image_name:
        return ""
    if isinstance(image_name, str) and (image_name.startswith("http://") or image_name.startswith("https://")):
        return image_name

    bucket = S3_BUCKET or os.getenv('S3_BUCKET')
    region = os.getenv('AWS_REGION', 'us-east-1')
    # Si no hay bucket configurado, devolvemos el valor original
    # (evita romper la vista; útil si luego sirves estáticos locales)
    if not bucket:
        return image_name

    return f'https://{bucket}.s3.{region}.amazonaws.com/{image_name}'