import data
from selenium import webdriver
from metodos import UrbanRoutesPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    # 1.Establecer una ruta en los campos "Desde" y "Hasta"
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # 2. Seleccionar la tarifa comfort
    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort_tariff()
        WebDriverWait(self.driver, 5)

    # 3. Añadir número de teléfono
    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number
        WebDriverWait(self.driver, 5)
        routes_page.add_phone_number(phone_number)
        WebDriverWait(self.driver, 5)
        assert routes_page.get_phone_number() == phone_number

    # 4. Añadir tarjeta de crédito
    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 5)
        card_number = data.card_number
        card_code = data.card_code
        routes_page.add_credit_card(card_number, card_code)
        routes_page.close_add_payment_window()
        WebDriverWait(self.driver, 5)
        assert routes_page.get_current_payment_method() == "Tarjeta"

    # 5. Enviar mensaje al conductor
    def test_write_driver_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        message_for_driver = data.message_for_driver
        routes_page.fill_comment_field(message_for_driver)
        assert routes_page.get_drivers_message() == message_for_driver

    # 6. Solicitar manta.
    def test_request_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(routes_page.find_blanket_slider()))
        routes_page.set_on_blanket_slider()

    # 7. Ordenar dos helados de chocolate.
    def test_order_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_ice_cream()
        assert routes_page.get_ice_cream_quantity() == "2"
        assert routes_page.get_chocolate_quantity() == "2"

    # 8. Pedir taxi. Se abre el modal "Buscar automóvil".
    def test_show_taxi_search(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.request_taxi()
        assert routes_page.get_search_taxi_text() == "Buscar automóvil"

    # 10. Desplegar en el modal, la informacion de viaje  al finalizar el temporizador.
    def test_show_order_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located(routes_page.ask_taxi.order_details_button))
        routes_page.show_order_details()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.ask_taxi.point_a))
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.ask_taxi.point_b))
        assert routes_page.get_point_a_text() == data.address_from
        assert routes_page.get_point_b_text() == data.address_to
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(routes_page.ask_taxi.drivers_name))
        drivers_name = routes_page.get_drivers_name()
        assert drivers_name is not None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
