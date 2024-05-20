
# PROYECTO 7. PRUEBAS DE APLICACIONES WEB AUTOMATIZADAS.

Se realizaron 9 pruebas automatizadas para probar el proceso de solicitar un taxi en un aplicativo web. 
La automatización fue  con Selenium en lenguaje Python. 
El aplicativo web es "Urban Routes"

Archivos .py del proyecto:

## data.py
Contiene la dirección del servidor y la información necesaria para introducir en los campos de datos 
(Direcciones, número de teléfono, Tarjeta de crédito)

## helpers.py
Contiene métodos de apoyo. En este caso la función  {def retrieve_phone_code(driver) -> str:} para interceptar
el código de verificacion que se envia SMS par ala verificación del número de teléfono.


## Métodos: (métodos.py)
Se organizaron dentro de la clase:
class UrbanRoutesPage

### Localizadores: 
Se designaron ocalizadores por ID, CLASS_NAME, CSS_SELECTOR y XPATH.

### Métodos:
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

*Las nueve pruebas tienen aserciones

## Entorno de Pruebas:
-Servidor del aplicativo web
-Pycharm:
*Selenium 
*Driver Chrome
-Navegador Google Chrome

## Pasos a seguir para la ejecución de las pruebas

###Precondiciones:
-Navegador Google Chrome instalado
-Github vinculado a TripleTen
-Pycharm instalado:
a)Pytest
b)Selenium
c)Controlador Google Chrome

### Pasos a seguir:
1. Clonar repositorio 
En la terminal escribir el comando : git clone git@github.com:tu_usuario/qa-project-07-es.git
2. Iniciar servidor 
3. En el archivo data.py pegar en "urban_routes_url" la URL generada por el servidor.
4. Ejecutar las pruebas: 
Opción 1:
4.1 Ir al archivo test_urban_routes.py
4.2 Dar click a "Run" (triángulo color verde en la parte superior derecha de la pantalla) 
    * Debe decir Current File
   
Opción 2:
4.1.1 En la terminal de Pycharm ejecutar el siguiente comando: pytest test_urban_routes.py 

## Resultados
El 100% de las pruebas aprobaron. Se logró con éxito solicitar un taxi con la tarifa comfort en Urban Routes.
