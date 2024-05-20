
import helpers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class UrbanRoutesPage:
    # Localizadores para ingresar direcciones y seleccionar tarifa
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_button = (By.CSS_SELECTOR, "button.round")
    comfort_tariff = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > "
                                       "div.tariff-picker.shown > div.tariff-cards > div:nth-child(5) > "
                                       "div.tcard-title")
    active_tariff = (By.CSS_SELECTOR, "tcard.active")
    # Localizadores para  el número de teléfono
    number_field_button = (By.CLASS_NAME, "np-button")
    phone_field = (By.ID, "phone")
    next_step_phone_button = (By.CSS_SELECTOR, "#root > div > div.number-picker.open > div.modal > div.section.active "
                                               "> form > div.buttons > button")
    sms_code = (By.ID, "code")
    confirm_code_button = (By.CSS_SELECTOR, "#root > div > div.number-picker.open > div.modal > div.section.active > "
                                            "form > div.buttons > button:nth-child(1)")
    filled_phone_field = (By.CLASS_NAME, "np-text")
    # Localizadores para el método de pago
    payment_method_field = (By.CLASS_NAME, "pp-button")
    add_card_option = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal > div.section.active > "
                                        "div.pp-selector > div.pp-row.disabled > div.pp-title")
    card_number_field = (By.CSS_SELECTOR, "#number")
    card_code_field = (By.NAME, 'code')
    add_card_button = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal.unusual > "
                                        "div.section.active.unusual > form > div.pp-buttons > button:nth-child(1)")
    close_payment_button = (By.CSS_SELECTOR, "#root > div > div.payment-picker.open > div.modal > div.section.active "
                                             "> button")
    current_payment_method = (By.CLASS_NAME, "pp-value-text")
    # Localidzoadr para el comentario
    comment_field = (By.ID, "comment")
    # Localizadores para amenidades de tarifa comofort
    blanket_slider = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > "
                                       "div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > "
                                       "div:nth-child(1) > div > div.r-sw > div > span")
    ice_cream_plus_counter = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > "
                                               "div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > "
                                               "div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div >"
                                               "div.r-counter > div > div.counter-plus")
    ice_cream_counter_value = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > "
                                                "div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > "
                                                "div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > "
                                                "div > div.r-counter > div > div.counter-value")
    chocolate_plus_counter = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > "
                                               "div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > "
                                               "div.r.r-type-group > div > div.r-group-items > div:nth-child(2) > div >"
                                               "div.r-counter > div > div.counter-plus")
    chocolate_counter_value = (By.CSS_SELECTOR, "#root > div > div.workflow > div.workflow-subcontainer > "
                                                "div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > "
                                                "div.r.r-type-group > div > div.r-group-items > div:nth-child(2) > "
                                                "div > div.r-counter > div > div.counter-value")
    # Localizador para solicitar taxi
    request_taxi_button = (By.CLASS_NAME, "smart-button")
    # Localizador del título de la ventana emergente de búsqueda de taxi
    search_taxi_window = (By.CLASS_NAME, "order-header-title")
    # Localizador del botón que despliega los detalles del pedido en la ventana emergente
    order_details_button = (By.CSS_SELECTOR, "#root > div > div.order.shown > div.order-body > div.order-subbody > "
                                             "div.order-buttons > div:nth-child(3) > button")

    # Localizadores de los campos de direcciones "desde" y "hasta" en los detalles del pedido
    point_a = (By.CSS_SELECTOR, "#root > div > div.order.shown > div.order-body > div.order-subbody > "
                                "div.order-details.shown > div:nth-child(1) > div.order-details-content > div.o-d-h")

    point_b = (By.CSS_SELECTOR, "#root > div > div.order.shown > div.order-body > div.order-subbody > "
                                "div.order-details.shown > div:nth-child(2) > div.order-details-content > div.o-d-h")
    # Localizador con el nombre del conductor asignado al pedido
    drivers_name = (By.CSS_SELECTOR, "#root > div > div.order.shown > div.order-body > div.order-subbody > "
                                     "div.order-buttons > div:nth-child(1) > div:nth-child(2)")

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Paso para definir la ruta
    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_ask_taxi(self):
        self.driver.find_element(*self.ask_button).click()

    def click_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    def find_comfort_tariff(self):
        return self.driver.find_element(*self.comfort_tariff)

    def check_comfort_is_set(self):
        return self.driver.find_element(*self.comfort_tariff).text

    # Paso para seleccionar tarifa comfort.
    def set_comfort_tariff(self):
        self.click_ask_taxi()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.find_comfort_tariff()))
        self.click_comfort_tariff()

    def click_number_field_button(self):
        self.driver.find_element(*self.number_field_button).click()

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_field).send_keys(phone_number)

    def click_next_step_phone_button(self):
        self.driver.find_element(*self.next_step_phone_button).click()

    def fill_sms_code(self):
        self.driver.find_element(*self.sms_code).send_keys(helpers.retrieve_phone_code(self.driver))

    def confirm_code(self):
        self.driver.find_element(*self.confirm_code_button).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.filled_phone_field).text

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
        self.driver.find_element(*self.payment_method_field).click()

    def click_add_card_option(self):
        self.driver.find_element(*self.add_card_option).click()

    def fill_card_number_field(self, card_number):
        self.driver.find_element(*self.card_number_field).send_keys(card_number)

    def fill_code_field(self, card_code):
        code_field = self.driver.find_element(*self.card_code_field)
        code_field.send_keys(card_code)
        code_field.click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def close_add_payment_window(self):
        self.driver.find_element(*self.close_payment_button).click()

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
        return self.driver.find_element(*self.current_payment_method).text

    # Funcion para enviar mensaje al conductor
    def fill_comment_field(self, message_for_driver):
        self.driver.find_element(*self.comment_field).send_keys(message_for_driver)

    def get_drivers_message(self):
        return self.driver.find_element(*self.comment_field).get_property("value")

    # Función para solicitar manta
    def set_on_blanket_slider(self):
        self.driver.find_element(*self.blanket_slider).click()

    def find_blanket_slider(self):
        return self.driver.find_element(*self.blanket_slider)

    def add_ice_cream_(self):
        ice_cream_plus = self.driver.find_element(*self.ice_cream_plus_counter)
        ice_cream_plus.click()
        ice_cream_plus.click()

    def select_chocolate_ice_cream(self):
        chocolate_plus = self.driver.find_element(*self.chocolate_plus_counter)
        chocolate_plus.click()
        chocolate_plus.click()

    # Paso para solicitar dos helados de chocolate
    def order_ice_cream(self):
        self.add_ice_cream_()
        self.select_chocolate_ice_cream()

    def get_ice_cream_quantity(self):
        return self.driver.find_element(*self.ice_cream_counter_value).text

    def get_chocolate_quantity(self):
        return self.driver.find_element(*self.chocolate_counter_value).text

    # Función para pedir el taxi
    def request_taxi(self):
        self.driver.find_element(*self.request_taxi_button).click()

    # Funcion para obtener texto de la ventana emergente
    def get_search_taxi_text(self):
        return self.driver.find_element(*self.search_taxi_window).text

    def click_order_details_button(self):
        self.driver.find_element(*self.order_details_button).click()

    # Función para obtener el la dirección "desde" en los detalles del pedido
    def get_point_a_text(self):
        return self.driver.find_element(*self.point_a).text

    # Función para obtener el la dirección "hasta" en los detalles del pedido
    def get_point_b_text(self):
        return self.driver.find_element(*self.point_b).text

    # Función para desplegar detalles del pedido
    def show_order_details(self):
        self.click_order_details_button()

    def get_drivers_name(self):
        return self.driver.find_element(*self.drivers_name).text
