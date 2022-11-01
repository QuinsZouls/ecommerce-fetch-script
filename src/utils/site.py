from selenium.webdriver.common.by import By


def get_department(driver, target):
    items = []
    department_list = driver.find_elements(
        By.CSS_SELECTOR, '#%s > li.nav__cat.w_spaceY.c_spaceY' % target)
    for department in department_list:
        department_entry = department.find_element(
            By.CSS_SELECTOR, 'button')
        # normalize text
        department_name = department_entry.get_attribute(
            'textContent').replace('\n', '')
        department_link = department.find_element(
            By.CSS_SELECTOR, 'li.nav__cat--level2__header > div > a').get_attribute('href')
        items.append({
            'url': department_link,
            'department': department_name,
            'categories': get_department_categories(department)
        })
    return items


def get_department_categories(driver):
    categories_list = []
    raw_categories = driver.find_elements(
        By.CSS_SELECTOR, 'ul.nav__cat--level2 > li.nav__spaceY')
    for category in raw_categories:
        raw_title = category.find_element(By.TAG_NAME, 'a')
        category_name = raw_title.get_attribute(
            'textContent').replace('\n', '')
        category_url = raw_title.get_attribute('href')
        categories_list.append({
            'name': category_name,
            'url': category_url,
            'subcategories': get_department_subcategories(category)
        })
    return categories_list


def get_department_subcategories(driver):
    categories_list = []
    raw_subcategories = driver.find_elements(
        By.CSS_SELECTOR, 'ul > li')
    for category in raw_subcategories:
        raw_category = category.find_element(By.TAG_NAME, 'a')
        category_name = raw_category.get_attribute(
            'textContent').replace('\n', '')
        category_url = raw_category.get_attribute('href')
        categories_list.append({
            'name': category_name,
            'url': category_url
        })
    return categories_list
