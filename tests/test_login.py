"""UI and form contract tests for the UTC login page."""

from urllib.parse import urlparse


def test_login_page_shows_expected_title_and_heading(login_page):
    assert login_page.driver.title == "Đăng nhập"
    heading = login_page.driver.find_element("tag name", "h1")
    assert heading.text == "Không chỉ là một giải pháp quản lý"


def test_username_field_is_located_by_name_and_has_expected_placeholder(login_page):
    username = login_page.find(login_page.USERNAME)
    assert username.get_attribute("type") == "text"
    assert username.get_attribute("placeholder") == "Tên đăng nhập"


def test_username_field_accepts_entered_text(login_page):
    username = login_page.find(login_page.USERNAME)
    username.send_keys("selenium.test")
    assert username.get_attribute("value") == "selenium.test"


def test_password_field_uses_password_locator_and_masks_input(login_page):
    password = login_page.find(login_page.PASSWORD)
    assert password.get_attribute("type") == "password"
    assert password.get_attribute("placeholder") == "Mật khẩu"


def test_password_field_accepts_entered_text(login_page):
    password = login_page.find(login_page.PASSWORD)
    password.send_keys("test-only-password")
    assert password.get_attribute("value") == "test-only-password"


def test_remember_me_is_unchecked_by_default(login_page):
    remember_me = login_page.find(login_page.REMEMBER_ME)
    assert remember_me.get_attribute("type") == "checkbox"
    assert not remember_me.is_selected()


def test_remember_me_can_be_toggled(login_page):
    remember_me = login_page.find(login_page.REMEMBER_ME)
    remember_me.click()
    assert remember_me.is_selected()
    remember_me.click()
    assert not remember_me.is_selected()


def test_login_submit_control_and_post_form_are_available(login_page):
    submit = login_page.find(login_page.SUBMIT)
    form = login_page.find(login_page.LOGIN_FORM)
    redirect = login_page.find(login_page.REDIRECT)

    assert submit.is_displayed()
    assert submit.is_enabled()
    assert submit.get_attribute("value") == "Đăng nhập"
    assert form.get_attribute("method").lower() == "post"
    assert urlparse(form.get_attribute("action")).path == "/Login"
    assert redirect.get_attribute("type") == "hidden"
    assert redirect.get_attribute("value")
