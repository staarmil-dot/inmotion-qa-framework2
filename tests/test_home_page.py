import pytest
from playwright.sync_api import Page, expect  # <-- ДОБАВЛЕНО: импорт expect
from pages.home_page import HomePage

def test_page_loads_successfully(page: Page):
    """Проверка успешной загрузки страницы и наличия ключевого слова в заголовке"""
    home_page = HomePage(page)
    home_page.navigate()
    title = home_page.get_title()
    assert "InMotion" in title, f"Ожидалось 'InMotion' в заголовке, получено: {title}"

def test_currency_is_eur(page: Page):
    """Проверка того, что валюта корректно отображается в EUR (€)"""
    home_page = HomePage(page)
    home_page.navigate()
    assert home_page.is_currency_eur_visible(), "Символ валюты EUR (€) не найден на странице"

def test_navigation_menu_exists(page: Page):
    """Проверка наличия основного меню навигации"""
    home_page = HomePage(page)
    home_page.navigate()
    # Увеличили таймаут до 10 сек для надежности
    expect(home_page.hosting_menu).to_be_visible(timeout=10000)