"""UI and form contract tests for the UTC login page."""


def test_login_page_shows_expected_title_and_heading(login_page):
    assert login_page.is_on_login_page()
    assert login_page.get_title() == "Đăng nhập"
    assert login_page.get_heading() == "Không chỉ là một giải pháp quản lý"


def test_username_field_is_located_by_name_and_has_expected_placeholder(login_page):
    assert login_page.get_username_type() == "text"
    assert login_page.get_username_placeholder() == "Tên đăng nhập"


def test_username_field_accepts_entered_text(login_page):
    login_page.enter_username("selenium.test")
    assert login_page.get_username_value() == "selenium.test"


def test_password_field_uses_password_locator_and_masks_input(login_page):
    assert login_page.get_password_type() == "password"
    assert login_page.get_password_placeholder() == "Mật khẩu"


def test_password_field_accepts_entered_text(login_page):
    login_page.enter_password("test-only-password")
    assert login_page.get_password_value() == "test-only-password"


def test_remember_me_is_unchecked_by_default(login_page):
    assert login_page.get_remember_me_type() == "checkbox"
    assert not login_page.is_remember_me_selected()


def test_remember_me_can_be_toggled(login_page):
    login_page.toggle_remember_me()
    assert login_page.is_remember_me_selected()
    login_page.toggle_remember_me()
    assert not login_page.is_remember_me_selected()


def test_login_submit_control_and_post_form_are_available(login_page):
    assert login_page.is_submit_displayed()
    assert login_page.is_submit_enabled()
    assert login_page.get_submit_text() == "Đăng nhập"
    assert (login_page.get_form_method() or "").lower() == "post"
    assert login_page.get_form_action_path() == "/Login"
    assert login_page.get_redirect_input_type() == "hidden"
    assert login_page.get_redirect_value()


def test_forgot_password_link_points_to_password_recovery(login_page):
    assert login_page.is_forgot_password_displayed()
    assert login_page.get_forgot_password_path() == "/Login/GetPass"


def test_utc_email_login_link_uses_google_accounts(login_page):
    assert login_page.is_utc_email_login_displayed()
    assert "Đăng nhập bằng e-mail UTC" in login_page.get_utc_email_login_text()
    assert login_page.get_utc_email_login_host() == "accounts.google.com"
