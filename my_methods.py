import data
import my_locators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(4) # NOTA: Originalmente es valor de (1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_load_page(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(my_locators.from_field))

        # Metetodos Campos Desde y Hasta
    def set_from(self, from_field):
        self.driver.find_element(*my_locators.from_field).send_keys(from_field)   #UrbanRoutesPageLoc
    def set_to(self, to_field):
        self.driver.find_element(*my_locators.to_field).send_keys(to_field)
    def get_from(self):
        return self.driver.find_element(*my_locators.from_field).get_property('value')
    def get_to(self):
        return self.driver.find_element(*my_locators.to_field).get_property('value')
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)


        # Metetodo Boton pedir un taxi
    def wait_load_taxi_button(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(my_locators.text_taxi_button))
    def click_order_taxi_button(self):
        self.driver.find_element(*my_locators.text_taxi_button).click()
    def get_text_button(self):
        return self.driver.find_element(*my_locators.button_text).text


        # Metetodo Tarifa comfort
    def wait_load_comfort_rate(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.comfort_rate_option))
    def click_comfort_rate_option(self):
        self.driver.find_element(*my_locators.comfort_rate_option).click()
    def get_comfort_text(self):
        return self.driver.find_element(*my_locators.comfort_rate_text).text


        # Metodos boton, campo numero de telefono y codigo sms
    def click_phone_number_button(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.phone_number_button))
        self.driver.find_element(*my_locators.phone_number_button).click()
    def put_phone_number_field(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(my_locators.phone_number_field))
        phone_number = data.phone_number
        self.driver.find_element(*my_locators.phone_number_field).send_keys(phone_number)
    def get_phone_number(self):
        return self.driver.find_element(*my_locators.phone_number_field).get_property('value')

    def click_next_button(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.next_button))
        self.driver.find_element(*my_locators.next_button).click()
    def get_next_button_type(self):
        return self.driver.find_element(*my_locators.next_button_type).get_attribute('type')

    def click_sms_code_field(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.sms_code_label_field))
        self.driver.find_element(*my_locators.sms_code_label_field).click()
    def set_sms_code(self):
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located(my_locators.sms_code_field))
        sms_retrieve_phone_code = retrieve_phone_code(self.driver)
        self.driver.find_element(*my_locators.sms_code_field).send_keys(sms_retrieve_phone_code)
    #def get_sms_code(self):
        #WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.sms_code_field_second))
        #return self.driver.find_element(*my_locators.sms_code_field_second).get_property('value')

    def click_confirm_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(my_locators.confirm_button_third))
        self.driver.find_element(*my_locators.confirm_button_third).click()
    def get_confirm_button_text(self):
        return self.driver.find_element(*my_locators.confirm_button).text

    def get_phone_number_button_text(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(my_locators.phone_number_added))
        return self.driver.find_element(*my_locators.phone_number_added).text



        # Metodos para pago
    def click_payment_method_button(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.payment_method_button))
        self.driver.find_element(*my_locators.payment_method_button).click()
    def click_add_card_button(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.add_card_button))
        self.driver.find_element(*my_locators.add_card_button).click()
    def card_number_field(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(my_locators.card_number_field))
        card_number = data.card_number
        self.driver.find_element(*my_locators.card_number_field).send_keys(card_number)
    def get_card_number(self):
        return self.driver.find_element(*my_locators.card_number_field).get_property('value')

    def code_field(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(my_locators.code_field))
        card_code = data.card_code
        self.driver.find_element(*my_locators.code_field).send_keys(card_code)
    def get_card_code(self):
        return self.driver.find_element(*my_locators.code_field).get_property('value')

    def click_change_focus(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(my_locators.change_focus_second))
        self.driver.find_element(*my_locators.change_focus_second).click()
    def click_add_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(my_locators.add_button))
        self.driver.find_element(*my_locators.add_button).click()
    def click_close_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(my_locators.close_button_third))
        self.driver.find_element(*my_locators.close_button_third).click()
    def get_change_text_from_cash_to_card(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.change_text_from_cash_to_card))
        return self.driver.find_element(*my_locators.change_text_from_cash_to_card).text



        # Metodo para mensaje a conductor
    def click_message_field_for_driver(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(my_locators.message_option_for_driver))
        self.driver.find_element(*my_locators.message_option_for_driver).click()
    def message_for_driver(self):
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(my_locators.message_field_for_driver))
        message_for_driver = data.message_for_driver
        self.driver.find_element(*my_locators.message_field_for_driver).send_keys(message_for_driver)
    def get_message_sent_text(self):
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located(my_locators.message_sent_to_the_driver))
        return self.driver.find_element(*my_locators.message_sent_to_the_driver).get_property('value')


        # Metodo para seleccionar manta y pañuelos
    def click_slider_round_button(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.slider_round_button_first))
        self.driver.find_element(*my_locators.slider_round_button_first).click()
    def get_button_enabled_status(self):
        button_slider_round = self.driver.find_element(*my_locators.slider_round_button_first)
        return button_slider_round.is_enabled()


        # Metodo para agrear helado
    def click_ice_cream_counter_plus(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.ice_cream_counter_plus))
        self.driver.find_element(*my_locators.ice_cream_counter_plus).click()
        self.driver.find_element(*my_locators.ice_cream_counter_plus).click()
    def get_quantity_ice_cream(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(my_locators.quantity_ice_cream))
        return self.driver.find_element(*my_locators.quantity_ice_cream).text


        # Metodo boton "pedir un taxi" y ventana emergente "Buscar automovil"
    def click_order_a_taxi_button(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(my_locators.taxi_button))
        self.driver.find_element(*my_locators.taxi_button).click()
    def get_popup_window_search_car(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(my_locators.heading_search_for_a_car))
        self.driver.find_element(*my_locators.heading_search_for_a_car).click()
        return self.driver.find_element(*my_locators.heading_search_for_a_car).text