"""Recomienda destinos de Chile según los intereses del viajero."""


# Cada destino puede asociarse a más de un interés para ofrecer alternativas útiles.
DESTINOS = [
    {
        "nombre": "Parque Nacional Torres del Paine",
        "intereses": ("naturaleza", "aventura"),
        "descripcion": "Montañas, glaciares y senderos en los paisajes de la Patagonia.",
    },
    {
        "nombre": "San Pedro de Atacama",
        "intereses": ("naturaleza", "aventura"),
        "descripcion": "Un pueblo del desierto ideal para explorar salares, géiseres y cielos estrellados.",
    },
    {
        "nombre": "Valparaíso",
        "intereses": ("cultura", "gastronomía"),
        "descripcion": "Una ciudad portuaria de cerros coloridos, arte urbano y cocina local.",
    },
    {
        "nombre": "Pucón",
        "intereses": ("aventura", "relajación", "naturaleza"),
        "descripcion": "Lagos, bosques y actividades al aire libre, además de termas para descansar.",
    },
    {
        "nombre": "Valle del Elqui",
        "intereses": ("relajación", "naturaleza", "gastronomía"),
        "descripcion": "Valles tranquilos, observación de estrellas y productos locales.",
    },
]

INTERESES = ("naturaleza", "aventura", "gastronomía", "cultura", "relajación")


def recomendar_destinos(interes):
    """Devuelve los destinos relacionados con el interés indicado."""
    interes = interes.strip().casefold()
    return [
        destino
        for destino in DESTINOS
        if interes in destino["intereses"]
    ]


def main():
    print("¡Bienvenido a Descubre tu próximo destino!")
    print("¿Qué te gustaría disfrutar en tu viaje por Chile?")

    # Se muestra un menú numerado para que sea fácil elegir sin preocuparse por tildes.
    for numero, interes in enumerate(INTERESES, start=1):
        print(f"{numero}. {interes.capitalize()}")

    eleccion = input("Escribe el número o el interés que prefieres: ").strip()
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(INTERESES):
        interes = INTERESES[int(eleccion) - 1]
    else:
        interes = eleccion.casefold()

    if interes not in INTERESES:
        print("No reconocí ese interés. Elige una de las opciones del menú.")
        return

    recomendaciones = recomendar_destinos(interes)
    print(f"\nDestinos recomendados para {interes}:")
    for destino in recomendaciones:
        print(f"- {destino['nombre']}: {destino['descripcion']}")


if __name__ == "__main__":
    main()