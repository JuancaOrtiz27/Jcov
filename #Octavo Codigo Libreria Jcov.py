#Octavo Codigo Libreria Jcov
import http.client


# Crear conexión con el servidor
conn = http.client.HTTPSConnection("es.wikipedia.org")

# Realizar una solicitud GET
conn.request("GET", "/posts/1")

# Obtener la respuesta
response = conn.getresponse()

# Leer y mostrar el contenido
print("Estado:", response.status)
print("Razón:", response.reason)
print("Contenido:", response.read().decode())