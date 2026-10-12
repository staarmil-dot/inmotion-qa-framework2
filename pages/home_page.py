# pages/home_page.py
from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.currency_indicator = self.page.get_by_text("€", exact=False)
        self.hosting_menu = self.page.get_by_role("link", name="Hosting")
        self.hero_heading = self.page.get_by_role("heading", name="Web Hosting")

    def navigate(self):
        # 1. Используем полный URL с параметром
        # 2. Увеличиваем таймаут до 30 секунд
        # 3. Ждем domcontentloaded
        self.page.goto(
            "https://www.inmotionhosting.com/?currency=EUR",
            wait_until="domcontentloaded",
            timeout=30000
        )
        # Даем 2 секунды на отработку JS и снятие базовой защиты от ботов
        self.page.wait_for_timeout(2000)

    def is_currency_eur_visible(self) -> bool:
        try:
            expect(self.currency_indicator).to_be_visible(timeout=5000)
            return True
        except Exception:
            return False

    def get_title(self) -> str:
        return self.page.title()