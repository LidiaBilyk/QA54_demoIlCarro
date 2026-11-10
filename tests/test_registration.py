import os
import uuid

from dotenv import load_dotenv

from pages.registration_page import RegistrationPage

load_dotenv()

#valid data - user with this data unregistered
random_suffix = uuid.uuid4().hex[:8]
FIRST_NAME = "Test_first_name"
LAST_NAME = "Test_last_name"
VALID_EMAIL = f"test_user_reg{random_suffix}@gm.com"
VALID_PASSWORD = os.getenv("TEST_USER_PASSWORD")
if not VALID_PASSWORD:
    raise ValueError("Critical error: password not found in the environment!")

# #wrong data - unregistered email (valid format), pass (valid format) doesn't match the login
# UNREGISTERED_EMAIL = "test1_user1@gm.com"
# WRONG_PASSWORD = os.getenv("TEST_USER_WRONG_PASSWORD")
# if not WRONG_PASSWORD:
#     raise ValueError("Critical error: wrong password not found in the environment!")
#
# #invalid data - invalid format of email
# INVALID_EMAIL = "test1gg.com"


def test_registration_form_is_available(driver):
    registration_page = RegistrationPage(driver)
    assert registration_page.is_registration_icon_displayed(), "Registration icon not found"
    registration_page.open_registration_page()
    assert registration_page.are_registration_form_elements_displayed(), "Registration form elements are not displayed"

def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.register(FIRST_NAME, LAST_NAME, VALID_EMAIL, VALID_PASSWORD)
    assert registration_page.is_confirm_message1_displayed("Registered"), "Text is not displayed"
    assert registration_page.is_confirm_message2_displayed("You are logged in success"), "Text is not displayed"
    registration_page.close_window()
    assert registration_page.is_log_out_button_displayed(), "Button is not displayed"

def test_invalid_registration_with_empty_name(driver):
        registration_page = RegistrationPage(driver)
        registration_page.open_registration_page()
        registration_page.register("", LAST_NAME, VALID_EMAIL, VALID_PASSWORD)
        assert registration_page.is_error_message_displayed("Name is required"), "Text is not displayed"
        assert registration_page.submit_button_disabled()
