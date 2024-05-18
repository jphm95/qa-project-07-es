
from selenium.webdriver.common.by import By


class AskTaxi:
    # Localizadores para ingresar direcciones y seleccionar tarifa
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_button = (By.CSS_SELECTOR, "button.round")
    comfort_tariff = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
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
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_payment_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
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
    drivers_name = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[2]')
