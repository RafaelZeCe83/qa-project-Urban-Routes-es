import data
from my_methods import UrbanRoutesPage
from selenium import webdriver


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

        cls.chrome_options = Options()
        capabilities = DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}  # Habilitar los logs de rendimiento
        cls.capabilities = DesiredCapabilities
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    # -------------------------------   Test 1: campo "Desde" y "Hasta"   ------------------------------
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # -------------------------------   Test 2: boton: "Pedir un taxi"   -------------------------------
    def test_order_taxi_button(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.wait_load_taxi_button()
        self.routes_page.click_order_taxi_button()
        button_taxi_text = self.routes_page.get_text_button()
        assert button_taxi_text == 'Pedir un taxi'

    # ----------------------------------   Test 3: "tarifa Comfort"   ----------------------------------
    def test_comfort_rate_option(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.wait_load_comfort_rate()
        self.routes_page.click_comfort_rate_option()
        comfort_rate_text = self.routes_page.get_comfort_text()
        assert comfort_rate_text == 'Comfort'

    # --------------------------   Test 4: "Numero de telefono y codigo sms"   --------------------------
    def test_phone_number_and_sms_code(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_phone_number_button()
        self.routes_page.put_phone_number_field()
        self.phone_number = data.phone_number
        phone_number = self.routes_page.get_phone_number()
        assert phone_number == data.phone_number
        self.routes_page.click_next_button()
        next_button_type = self.routes_page.get_next_button_type()
        assert next_button_type == 'submit'
        #self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_sms_code_field()
        self.routes_page.set_sms_code()
        self.routes_page.click_confirm_button()
        text_phone_number_button = self.routes_page.get_phone_number_button_text()
        assert text_phone_number_button == '+1 123 123 12 12'

    # ----------------------------------   Test 5: "Metodo de pago"   -----------------------------------
    def test_payment_method_card_number_and_card_code(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_button()
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.card_number_field()
        card_number = self.routes_page.get_card_number()
        assert card_number == data.card_number
        self.routes_page.code_field()
        card_code = self.routes_page.get_card_code()
        assert card_code == data.card_code
        self.routes_page.click_change_focus()
        self.routes_page.click_add_button()
        self.routes_page.click_close_button()
        change_text_from_cash_to_card = self.routes_page.get_change_text_from_cash_to_card()
        assert change_text_from_cash_to_card == "Tarjeta"

    # -------------------------------   Test 6: "mensaje al conductor"   --------------------------------
    def test_message_to_driver(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_message_field_for_driver()
        self.routes_page.message_for_driver()
        my_message_to_the_driver = self.routes_page.get_message_sent_text()
        assert my_message_to_the_driver == "Traiga un aperitivo"

    # --------------------------- Test 7: para seleccionar manta y pañuelos   ---------------------------
    def test_to_select_blanket_and_scarves(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_slider_round_button()
        button_slider_is_enabled = self.routes_page.get_button_enabled_status()
        assert button_slider_is_enabled

    # ----------------------------------   Test 8: Seccion de helado   ----------------------------------
    def test_for_ice_cream_section(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_ice_cream_counter_plus()
        quantity_ice_cream = self.routes_page.get_quantity_ice_cream()
        assert quantity_ice_cream == '2'

    # ------------------------------------- Test 9: Solicitar taxi y ventana emergente   ------------------------------------
    def test_order_taxi_and_pop_up_window_search_car(self):
        self.routes_page = UrbanRoutesPage(self.driver)
        self.routes_page.click_order_a_taxi_button()
        text_popup_window = self.routes_page.get_popup_window_search_car()
        assert text_popup_window == 'Buscar automóvil'


    @classmethod
    def teardown_class(cls):
         cls.driver.quit()