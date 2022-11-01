import json
import undetected_chromedriver as uc
from config.driver import set_chrome_options
from config.environment import DRIVER_PATH, OUTPUT_FILE, TARGET_URL, EXEC_ENVIRONMENT
from selenium.webdriver.common.by import By
from utils.site import get_department

DEPARTMENTS = ['homeview1', 'homeview2']
DEPARTMENTS_NAME = ['Super en casa', 'Todo para tu hogar']

print('RUNNING SCRIPT')
if __name__ == "__main__":
    print("### STARTED FETCH SCRIPT###")
    chrome_options = set_chrome_options()
    driver = uc.Chrome(options=chrome_options, use_subprocess=True) if EXEC_ENVIRONMENT == 'standalone' else uc.Chrome(
        options=chrome_options, use_subprocess=True, driver_executable_path=DRIVER_PATH)
    driver.get(TARGET_URL)
    data = []
    # Map currents departments
    for department, department_name in zip(DEPARTMENTS, DEPARTMENTS_NAME):
        departments_list = get_department(driver, department)
        data.append({
            "section": department_name,
            "departments": departments_list
        })
    # Generate JSON object
    json_object = json.dumps(
        data, indent=4, ensure_ascii=False)
    with open(OUTPUT_FILE, "w", encoding='utf8') as outfile:
        outfile.write(json_object)
    # Close driver instance
    print("### END FETCH SCRIPT###")
    driver.close()
