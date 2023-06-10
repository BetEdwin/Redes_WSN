# -- coding: utf-8 --
"""
Created on Wed Sep 14 20:51:18 2022
"""

from _future_ import print_function
import http.client
import time
import urllib.parse

# API KEY
THINGSPEAK_APIKEY = 'M67K53WMR9YVQBIZ'
print("Welcome to the ThingSpeak Raspberry Pi sensor! Press CTRL+C to stop.")

# Archivo de texto para almacenar los datos
file_path = "datos.txt"

try:
    while True:
        # Obtener los valores de los campos
        temp_corporal = ((500 * 3.30) - 0.5) * 10
        freq_cardiaca = (temp_corporal * 9.0 / 5.0) + 32.0
        presion_art = ((50 * 3.30) ** 0.5) * 10
        saturacion_ox = (presion_art * 9.0 / 50.0) + 32.0
        
        # Mostrar los resultados para diagnóstico
        print("Uploading {0:.2f} C, {1:.2f} F, {2:.2f} V, {3:.2f} V".format(temp_corporal, freq_cardiaca, presion_art, saturacion_ox), end=' ... ')
        
        # Configurar los datos para enviar en formato JSON (diccionario)
        params = urllib.parse.urlencode(
            {
                'field1': temp_corporal,
                'field2': freq_cardiaca,
                'field3': presion_art,
                'field4': saturacion_ox,
                'key': THINGSPEAK_APIKEY,
            }
        )
        
        # Crear el encabezado
        headers = {"Content-type": "application/x-www-form-urlencoded", 'Accept': "text/plain"}
        
        # Crear una conexión a través de HTTP
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        
        try:
            # Ejecutar la solicitud de publicación (o actualización) para cargar los datos
            conn.request("POST", "/update", params, headers)
            
            # Verificar la respuesta del servidor (200 es éxito)
            response = conn.getresponse()
            
            # Mostrar la respuesta (debería ser 200)
            print("Response: {0} {1}".format(response.status, response.reason))
            
            # Leer los datos para diagnóstico
            data = response.read()
            conn.close()
            
            # Almacenar los datos en un archivo de texto
            with open(file_path, "a") as file:
                file.write("{0:.2f} C, {1:.2f} F, {2:.2f} V, {3:.2f} V\n".format(temp_corporal, freq_cardiaca, presion_art, saturacion_ox))
            
        except Exception as err:
            print("WARNING: ThingSpeak connection failed: {0}, data: {1}".format(err, data))
        
        # Esperar durante 20 segundos
        time.sleep(20)

except KeyboardInterrupt:
    print("Thanks, bye!")

exit(0)
       
        