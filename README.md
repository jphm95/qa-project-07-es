
# PROYECTO 7. PRUEBAS DE APLICACIONES WEB AUTOMATIZADAS.

Se realizaron 9 pruebas automatizadas para probar el proceso de solicitar un taxi en un aplicativo web. 
La automatización fue  con Selenium en lenguaje Python. 
El aplicativo web es "Urban Routes"

Archivos .py del proyecto:

## Localizadores: (localizadores.py)
Se designaron ocalizadores por ID, CLASS_NAME, CSS_SELECTOR y XPATH.
El XPATH se destinó como última alternativa cuando los elementos no fueron posibles de identificar mediante atributos unicos.

Con el fin de optimizar la escritura de código para el archivo métodos.py localizadores se organizaron dentro la clase:
class AskTaxi.

## Métodos: (métodos.py)
Se organizaron dentro de la clase:
class UrbanRoutesPage

En este archivo se encuentran las diferentes funciones para la correcta interacción con el aplicativo web.
Buscar elementos: find_element, hacer click: .click(), llenar campos de datos: .send_keys()

El archivo también cuenta con funciones para obtener informacion del aplicativo que se puede utilizar en las aserciones.
Obtener textos: .text , obtener data: get_property. 

Se crearon los siguientes pasos:
1. Establecer la dirección
2. Seleccionar tarifa confort 
3. Añadir número de teléfono
4. Añadir tarjeta de crédito
5. Pedir dos helados de chocolate

Se utilizaron funciones para:
1. Enviar mensaje al conductor
2. Solicitar Manta
3. Pedir taxi(modal "Buscar Automovil)
4. Datos del viaje en el modal.

## Pruebas (test_urban_routes.py)
Se probó la funcionalidad de solicitar un Taxi en el aplicativo web "Urban Routes".
Las pruebas fueron las siguientes:
1. Establecer una ruta en los campos "Desde" y "Hasta"
2. Seleccionar la tarifa comfort
3. Añadir número de teléfono
4. Añadir tarjeta de crédito
5. Enviar mensaje al conductor
6. Solicitar manta
7. Ordenar dos helados de chocolate
8. Pedir taxi. Se abre el modal "Buscar automóvil".
9. Desplegar en el modal, la informacion de viaje  al finalizar el temporizador

## Entorno de Pruebas:
-Servidor del aplicativo web
-Pycharm:
*Selenium 
*Driver Chrome
-Navegador Google Chrome

## Resultados
El 100% de las pruebas aprobaron. Se logró con éxito solicitar un taxi con la tarifa comfort en Urban Routes.