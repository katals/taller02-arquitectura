import random

POKENEAS = [
  {
    "id": 1,
    "nombre": "Mazorcacho",
    "altura": 1.0,
    "habilidad": "Chuzo dorado",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/mazorcacho.png",
    "frase": "¡Con maíz no se juega, eso es sagrado!"
  },
  {
    "id": 2,
    "nombre": "Papayuki",
    "altura": 1.5,
    "habilidad": "Smoothie curativo",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/juicioso.jpg",
    "frase": "Solo amor, solo nacional."
  },
  {
    "id": 3,
    "nombre": "Guacamayo",
    "altura": 1.8,
    "habilidad": "Ala tropical",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/nosepai.jpg",
    "frase": "Vuela bajo, pero pica alto."
  },
  {
    "id": 4,
    "nombre": "Arepunch",
    "altura": 0.9,
    "habilidad": "Fuerza de maíz",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/fygonorrea.jpg",
    "frase": "¡Calentao y con queso, ese es mi proceso!"
  },
  {
    "id": 5,
    "nombre": "Cafetín",
    "altura": 1.2,
    "habilidad": "Carga matutina",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/yasuri.jpg",
    "frase": "Sin tinto, ni el alma responde."
  },
  {
    "id": 6,
    "nombre": "Chontaduro",
    "altura": 0.6,
    "habilidad": "Raíz ancestral",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/soy%C3%B1ero.jpg",
    "frase": "Rojo por fuera, sabroso por dentro... y con sal."
  },
  {
    "id": 7,
    "nombre": "Guayabot",
    "altura": 2.3,
    "habilidad": "Pulpa explosiva",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/jj.jpg",
    "frase": "¡Guayaba o muerte!"
  },
  {
    "id": 8,
    "nombre": "Mangostro",
    "altura": 1.1,
    "habilidad": "Zumo ácido",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/peguelosocio.jpg",
    "frase": "Dulce con actitud, ácido con razón."
  },
  {
    "id": 9,
    "nombre": "Platanito",
    "altura": 0.7,
    "habilidad": "Resbalón cósmico",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/zarco.jpg",
    "frase": "Caerse es parte del camino... y del chiste."
  },
  {
    "id": 10,
    "nombre": "Luluchu",
    "altura": 1.4,
    "habilidad": "Abrazo andino",
    "imagen": "https://demo-bucket-katals1.s3.us-east-1.amazonaws.com/pablo.jpg",
    "frase": "Más unido que arepa con queso."
  }
]

def random_pokenea():
    return random.choice(POKENEAS)
