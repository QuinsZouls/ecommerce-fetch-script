import os

TARGET_URL = os.getenv('TARGET_URL', 'https://www.soriana.com')
OUTPUT_FILE = os.getenv('OUTPUT_FILE', 'result.json')
DRIVER_PATH = os.getenv('DRIVER_PATH', '/usr/bin/chromedriver')
EXEC_ENVIRONMENT = os.getenv('EXEC_ENVIRONMENT', 'standalone')