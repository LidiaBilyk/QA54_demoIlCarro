from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):
    # REGISTRATION_ICON = (By.XPATH, "//a[@class='ico-register']")
    # FIRST_NAME_INPUT = (By.ID, "FirstName")
    # LAST_NAME_INPUT = (By.ID, "LastName")
    # EMAIL_INPUT = (By.ID, "Email")
    # PASSWORD_INPUT = (By.ID, "Password")
    # CONFIRM_PASSWORD_INPUT = (By.ID, "ConfirmPassword")
    # REGISTER_BUTTON = (By.ID, "register-button")
    # LOG_OUT_BUTTON = (By.XPATH, "//a[@class='ico-logout']")
    # WRONG_EMAIL_MESSAGE = (By.XPATH, "//li[normalize-space()='No customer account found']")
    # WRONG_PASSWORD_MESSAGE = (By.XPATH, "//li[normalize-space()='The credentials provided are incorrect']")
    # INVALID_EMAIL_MESSAGE = (By.XPATH, "//span[@for='Email']")

    REGISTRATION_ICON = (By.CSS_SELECTOR, "[href='/register']")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='firstName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[name='lastName']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name = 'username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name = 'password']")
    TERM_OF_USE_CHECK_BOX = (By.ID, "terms-of-use")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Y’alla!']")
    LOG_OUT_BUTTON = (By.XPATH, "//button[text()='Log out']")

    def is_registration_icon_displayed(self):
        return self.is_element_visible(self.REGISTRATION_ICON)

    def are_registration_form_elements_displayed(self):
        return (self.is_element_visible(self.FIRST_NAME_INPUT)
                and self.is_element_visible(self.LAST_NAME_INPUT)
                and self.is_element_visible(self.EMAIL_INPUT)
                and self.is_element_visible(self.PASSWORD_INPUT)
                and self.is_element_visible(self.TERM_OF_USE_CHECK_BOX)
                and self.is_element_visible(self.REGISTRATION_BUTTON))

    def open_registration_page(self):
        self.click_element(self.REGISTRATION_ICON)

    def fill_first_name_field(self, first_name):
        self.input_text(self.FIRST_NAME_INPUT, first_name)

    def fill_last_name_field(self, last_name):
        self.input_text(self.LAST_NAME_INPUT, last_name)

    def fill_email_field(self, email):
        self.input_text(self.EMAIL_INPUT, email)

    def fill_password_field(self, password):
        self.input_text(self.PASSWORD_INPUT, password)

    def click_term_of_use_checkbox(self):
        self.click_element(self.TERM_OF_USE_CHECK_BOX)

    def click_registration_button(self):
        self.click_element(self.REGISTRATION_BUTTON)

    def accept_alert(self):
        self.accept_alert()

    def is_log_out_button_displayed(self):
        return self.is_element_visible(self.LOG_OUT_BUTTON)

    # def is_wrong_email_message(self):
    #     return self.is_element_visible(self.WRONG_EMAIL_MESSAGE)
    #
    # def is_wrong_password_message(self):
    #     return self.is_element_visible(self.WRONG_PASSWORD_MESSAGE)
    #
    # def is_invalid_email_message(self):
    #     return self.is_element_visible(self.INVALID_EMAIL_MESSAGE)

    def register(self, first_name, last_name, email, password):
        self.fill_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.click_term_of_use_checkbox()
        self.click_registration_button()