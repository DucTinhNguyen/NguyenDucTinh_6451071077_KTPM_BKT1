"""UI and form contract tests for the UTC login page."""


def test_login_page_shows_expected_title_and_heading(login_page):
    assert login_page.driver.title == "Đăng nhập"
    heading = login_page.driver.find_element("tag name", "h1")
    assert heading.text == "Không chỉ là một giải pháp quản lý"


def test_username_field_is_located_by_name_and_has_expected_placeholder(login_page):
    username = login_page.find(login_page.USERNAME)
    assert username.get_attribute("type") == "text"
    assert username.get_attribute("placeholder") == "Tên đăng nhập"
