
from geopy.geocoders import Nominatim

def obtener_coordenadas(nombre_equipo):
    geolocalizador = Nominatim(user_agent="mi_aplicacion")
    ubicacion = geolocalizador.geocode(nombre_equipo)
    if ubicacion:
        longitud = ubicacion.longitude
        latitud = ubicacion.latitude
        return longitud, latitud
    else:
        return None

def main():
    nombre_equipo = input("Ingresa el nombre de tu equipo: ")
    coordenadas = obtener_coordenadas(nombre_equipo)
    if coordenadas:
        print("Las coordenadas de", nombre_equipo, "son:")
        print("Longitud:", coordenadas[0])
        print("Latitud:", coordenadas[1])
    else:
        print("No se pudo encontrar la ubicación de", nombre_equipo)

if __name__ == "__main__":
    main()
