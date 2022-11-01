# ecommerce-fetch-script
Script de extracción, para el menú de despensa del sitio.

# Herramientas y librerías utilizadas
- Python 3.9
- Selenium
- Google Chrome
- Google Chrome webdriver
- undetected-chromedriver (una librería para evitar la detección de bots)
# Requerimientos standalone
- Python 3.9
- un navegador chrome y su respectivo webdriver (se puede omitir ese paso en usando docker)
- 4GB memoria RAM
# Requerimientos docker
- Docker y docker-compose
- 2gb de memoria RAM
## Ejecutar script
Para ejecutar el script debe asegurarse de contar con las variables de ambiente adecuadas:
- TARGET_URL: la url del sitio
- OUTPUT_FILE: la ruta del archivo json
- DRIVER_PATH: la ruta del webdriver
- EXEC_ENVIRONMENT: el tipo de ambiente a ejecutar (standalone o server)
```bash
python3 src/main.py
```
En caso se usar docker, primero construir la imagen con docker-compose:
```bash
docker-compose build
```
Una vez creada la imagen, se procede a correr el contenedor, de preferencia en segundo plano (ya que tarda unos minutos en completar el script)
Nota: asegurarse de contar con el volumen de salida, de lo contrario no se guardará el archivo json
```bash
docker-compose up -d
```
# Incidencias
Debido al uso de selenium, después de varios intentos corriendo el script la página comenzó a bloquear toda actividad, para ello se implementó la librería de python undetected-chromedriver para evitar dicho bloqueo.