
from localizadores import AskTaxi
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


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
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver
        self.ask_taxi = AskTaxi()

    def set_from(self, address_from):
        self.driver.find_element(*self.ask_taxi.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.ask_taxi.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.ask_taxi.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.ask_taxi.to_field).get_property('value')

    # Paso para definir la ruta
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_ask_taxi(self):
        self.driver.find_element(*self.ask_taxi.ask_button).click()

    def click_comfort_tariff(self):
        self.driver.find_element(*self.ask_taxi.comfort_tariff).click()

    def find_comfort_tariff(self):
        return self.driver.find_element(*self.ask_taxi.comfort_tariff)

    # Paso para seleccionar tarifa comfort.
    def set_comfort_tariff(self):
        self.click_ask_taxi()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.find_comfort_tariff()))
        self.click_comfort_tariff()

    def click_number_field_button(self):
        self.driver.find_element(*self.ask_taxi.number_field_button).click()

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.ask_taxi.phone_field).send_keys(phone_number)

    def click_next_step_phone_button(self):
        self.driver.find_element(*self.ask_taxi.next_step_phone_button).click()

    def fill_sms_code(self):
        self.driver.find_element(*self.ask_taxi.sms_code).send_keys(retrieve_phone_code(self.driver))

    def confirm_code(self):
        self.driver.find_element(*self.ask_taxi.confirm_code_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.ask_taxi.filled_phone_field).text

    # Paso para añadir número de teléfono
    def add_phone_number(self, phone_number):
        self.click_number_field_button()
        self.fill_phone_number(phone_number)
        WebDriverWait(self.driver, 2)
        self.click_next_step_phone_button()
        WebDriverWait(self.driver, 2)
        self.fill_sms_code()
        self.confirm_code()

    def click_payment_method_field(self):
        self.driver.find_element(*self.ask_taxi.payment_method_field).click()

    def click_add_card_option(self):
        self.driver.find_element(*self.ask_taxi.add_card_option).click()

    def fill_card_number_field(self, card_number):
        self.driver.find_element(*self.ask_taxi.card_number_field).send_keys(card_number)

    def fill_code_field(self, card_code):
        code_field = self.driver.find_element(*self.ask_taxi.card_code_field)
        code_field.send_keys(card_code)
        code_field.click()

    def click_add_card_button(self):
        self.driver.find_element(*self.ask_taxi.add_card_button).click()

    def close_add_payment_window(self):
        self.driver.find_element(*self.ask_taxi.close_payment_button).click()

        # Paso para añadir tarjeta de crédito
    def add_credit_card(self, card_number, card_code):
        self.click_payment_method_field()
        self.click_add_card_option()
        WebDriverWait(self.driver, 2)
        self.fill_card_number_field(card_number)
        WebDriverWait(self.driver, 2)
        self.fill_code_field(card_code)
        self.click_add_card_button()

    def get_current_payment_method(self):
        return self.driver.find_element(*self.ask_taxi.current_payment_method).text

    # Funcion para enviar mensaje al conductor
    def fill_comment_field(self, message_for_driver):
        self.driver.find_element(*self.ask_taxi.comment_field).send_keys(message_for_driver)

    def get_drivers_message(self):
        return self.driver.find_element(*self.ask_taxi.comment_field).get_property("value")

    # Función para solicitar manta
    def set_on_blanket_slider(self):
        self.driver.find_element(*self.ask_taxi.blanket_slider).click()

    def find_blanket_slider(self):
        return self.driver.find_element(*self.ask_taxi.blanket_slider)

    def add_ice_cream_(self):
        ice_cream_plus = self.driver.find_element(*self.ask_taxi.ice_cream_plus_counter)
        ice_cream_plus.click()
        ice_cream_plus.click()

    def select_chocolate_ice_cream(self):
        chocolate_plus = self.driver.find_element(*self.ask_taxi.chocolate_plus_counter)
        chocolate_plus.click()
        chocolate_plus.click()

    # Paso para solicitar dos helados de chocolate
    def order_ice_cream(self):
        self.add_ice_cream_()
        self.select_chocolate_ice_cream()

    def get_ice_cream_quantity(self):
        return self.driver.find_element(*self.ask_taxi.ice_cream_counter_value).text

    def get_chocolate_quantity(self):
        return self.driver.find_element(*self.ask_taxi.chocolate_counter_value).text

    # Función para pedir el taxi
    def request_taxi(self):
        self.driver.find_element(*self.ask_taxi.request_taxi_button).click()

    # Funcion para obtener texto de la ventana emergente
    def get_search_taxi_text(self):
        return self.driver.find_element(*self.ask_taxi.search_taxi_window).text

    def click_order_details_button(self):
        self.driver.find_element(*self.ask_taxi.order_details_button).click()

    # Función para obtener el la dirección "desde" en los detalles del pedido
    def get_point_a_text(self):
        return self.driver.find_element(*self.ask_taxi.point_a).text

    # Función para obtener el la dirección "hasta" en los detalles del pedido
    def get_point_b_text(self):
        return self.driver.find_element(*self.ask_taxi.point_b).text

    # Función para desplegar detalles del pedido
    def show_order_details(self):
        self.click_order_details_button()

    def get_drivers_name(self):
        return self.driver.find_element(*self.ask_taxi.drivers_name).text
