
import undetected_chromedriver as uc
from config.driver import set_chrome_options
from config.environment import DRIVER_PATH, TARGET_URL, EXEC_ENVIRONMENT
from selenium.webdriver.common.by import By
from utils.site import get_department, get_department_categories, get_department_subcategories

def pytest_html_report_title(report):
    report.title = "Pruebas unitarias"

def generate_driver():
    chrome_options = set_chrome_options()
    driver = uc.Chrome(options=chrome_options, use_subprocess=True) if EXEC_ENVIRONMENT == 'standalone' else uc.Chrome(
        options=chrome_options, use_subprocess=True, driver_executable_path=DRIVER_PATH)
    driver.get(TARGET_URL)
    return driver


def test_get_department():
    print("Test: Get department")
    driver = generate_driver()
    items = get_department(driver, 'homeview1')
    print(len(items))
    assert len(items) > 0


def test_get_department_categories():
    driver = generate_driver()
    departments = driver.find_elements(
        By.CSS_SELECTOR, '#homeview1 > li.nav__cat.w_spaceY.c_spaceY')
    items = get_department_categories(departments[0])
    assert len(items) > 0


def test_get_department_subcategories():
    driver = generate_driver()
    departments = driver.find_elements(
        By.CSS_SELECTOR, '#homeview1 > li.nav__cat.w_spaceY.c_spaceY')
    raw_categories = departments[0].find_elements(
        By.CSS_SELECTOR, 'ul.nav__cat--level2 > li.nav__spaceY')
    items = get_department_subcategories(raw_categories[0])
    assert len(items) > 0
