"""UI and form contract tests for the UTC login page."""


def test_login_page_shows_expected_title_and_heading(login_page):
    assert login_page.driver.title == "Đăng nhập"
    heading = login_page.driver.find_element("tag name", "h1")
    assert heading.text == "Không chỉ là một giải pháp quản lý"
