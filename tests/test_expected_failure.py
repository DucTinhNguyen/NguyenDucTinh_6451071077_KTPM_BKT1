def test_login_page_title_is_home_page(login_page):
    assert login_page.get_title() == "Trang chủ"
