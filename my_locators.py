from selenium.webdriver.common.by import By

# Localizador campo Desde y Hasta
from_field = (By.ID, 'from')
to_field = (By.ID, 'to')


# Localizador de Boton ordenar un taxi
order_taxi_button = (By.CLASS_NAME, 'button round')
text_taxi_button = (By.XPATH, "//*[text()='Pedir un taxi']")
button = (By.CSS_SELECTOR, "button[type='button']")
button_text = (By.XPATH, "//*[text()='Pedir un taxi']")


# Localizador tarifa comfort
comfort_rate_option = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
comfort_rate_text = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
comfort_rate = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[1]/img")
comfort_rate_second = (By.CSS_SELECTOR, "img[alt='Comfort']")
comfort_rate_third = (By.XPATH, "//button[@data-for='tariff-card-4']")
comfort_rate_fourth = (By.XPATH, "//div[@class='tcard']//button[.//div[@class='tcard-title' and text()='Comfort']]")
comfort_rate_fifth = (By.CSS_SELECTOR, "div.tcard button[data-for='tariff-card-4']")
comfort_rate_requirement = (By.XPATH, "//*[text()='Cubeta de helado']")
comfort_image_locator = (By.CSS_SELECTOR, "img[src='/static/media/kids.075fd8d4.svg']")


# Localizadores boton y campo para telefono y codigo sms
phone_number_button = (By.CLASS_NAME, 'np-text')
phone_number_button_text = (By.XPATH, "//div[text()='Número de teléfono']")
phone_number_field = (By.XPATH, "//input[@placeholder='+1 xxx xxx xx xx']")
phone_number_field_second = (By.XPATH, "//input[@placeholder='+1 xxx xxx xx xx']")
next_button = (By.XPATH, "//*[text()='Siguiente']")
next_button_type = (By.CSS_SELECTOR, "button.button.full") ####################
sms_code_field = (By.XPATH, "//*[@placeholder='xxxx']")
sms_code_field_second = (By.CSS_SELECTOR, "input[placeholder='xxxx']")
sms_code_label_field = (By.CSS_SELECTOR, "label[for='code']")
confirm_button = (By.XPATH, "//*[text()='Confirmar']")
confirm_button_second = (By.CSS_SELECTOR, "button.button.full")
confirm_button_third = (By.XPATH, "//button[contains(@class, 'button full') and text()='Confirmar']")
confirm_button_forth = (By.XPATH, "//button[@type='submit' and contains(text(), 'Confirmar')]")
phone_number_added = (By.XPATH, "//div[@class='np-text' and text()='+1 123 123 12 12']")


# Localizadores para pago
payment_method_button = (By.CLASS_NAME, 'pp-text')
add_card_button = (By.XPATH, "//div[@class='pp-title' and text()='Agregar tarjeta']")
card_number_field = (By.XPATH, "//*[@placeholder='1234 4321 1408']")
code_field = (By.XPATH, "//*[@placeholder='12']")
change_focus = (By.CLASS_NAME, 'section active unusual')
change_focus_second = (By.CLASS_NAME, 'card-wrapper')
add_button = (By.XPATH, "//*[@type='submit' and @class='button full' and text()='Agregar']")
close_button = (By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[1]")
close_button_second = (By.CLASS_NAME, 'close-button section-close')
close_button_third = (By.XPATH, "//div[@class='section active' and .//div[text()='Método de pago']]//button[@class='close-button section-close']")
change_text_from_cash_to_card = (By.CSS_SELECTOR, 'div.pp-value-text')


# Localizador para enviar mensaje al conductor
message_option_for_driver = (By.XPATH, "//label[@for='comment' and contains(text(), 'Mensaje para el conductor...')]")
message_field_for_driver = (By.XPATH, "//input[@placeholder='Traiga un aperitivo']")
message_sent_to_the_driver = (By.XPATH, "//input[@placeholder='Traiga un aperitivo']")


# Localizador para seleccionar manta y pañuelos
slider_round_button_first = (By.XPATH, "//span[@class='slider round'][1]")
slider_round_button_second = (By.XPATH, "//span[contains(@class, 'slider')][1]")


# Localizador para agrear helado
ice_cream_counter_plus = (By.XPATH, "//div[@class='counter-plus' and text()='+'][1]")
quantity_ice_cream = (By.XPATH, "//div[@class='counter-value' and text()='2']")


# Localizador para boton pedir un taxi y ventana buscar un automovil
taxi_button = (By.CSS_SELECTOR, '.smart-button-main')
heading_search_for_a_car = (By.XPATH, "//div[@class='order-header-title' and text()='Buscar automóvil']")