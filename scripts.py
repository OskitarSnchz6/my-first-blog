from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from datetime import datetime

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navegar a la página de inicio de sesión
driver.get('http://127.0.0.1:8000/admin/login/?next=/')

# Introducir el nombre de usuario y la contraseña
username_field = driver.find_element(By.NAME, 'username')
username_field.send_keys('oskitarsnchz')
password_field = driver.find_element(By.NAME, 'password')
password_field.send_keys('Oskitar2301Snchz')
password_field.send_keys(Keys.RETURN)

# Navegar a la página para crear un nuevo post
driver.get('http://127.0.0.1:8000/posts/new/')

# Obtener el título y el contenido del post del usuario
title_input = input("Introduce el título del post: ")
content_input = input("Introduce el contenido del post: ")

# Introducir el título y el contenido del post
title_field = driver.find_element(By.NAME, 'title')
title_field.send_keys(title_input)

content_field = driver.find_element(By.NAME, 'text')
content_field.send_keys(content_input)

# Obtener la hora actual
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

# Introducir la hora actual en los campos Created date y Published date
created_date_field = driver.find_element(By.NAME, 'created_date')
created_date_field.send_keys(current_time)
published_date_field = driver.find_element(By.NAME, 'published_date')
published_date_field.send_keys(current_time)


# Esperar a que se cargue la página de detalles del post
wait = WebDriverWait(driver, 10)  # esperar hasta 10 segundos

# esperar a que aparezca el botón de envío
submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "POST")]')))

# hacer clic en el botón de envío
submit_button.click()

driver.quit()