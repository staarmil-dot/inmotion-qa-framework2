# conftest.py
import pytest

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Модифицируем контекст браузера, чтобы он выглядел как обычный Chrome пользователя,
    а не как автоматизированный тестовый браузер.
    """
    return {
        **browser_context_args,
        "ignore_https_errors": True,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "viewport": {"width": 1920, "height": 1080},
    }