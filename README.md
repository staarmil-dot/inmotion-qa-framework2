# InMotion Hosting QA Automation Framework

Фреймворк для автоматизированного тестирования сайта InMotion Hosting.

## Стек технологий
- Python 3.11+
- Playwright
- Pytest
- GitHub Actions (CI/CD)

## Локальный запуск
1. Установите зависимости: `pip install -r requirements.txt`
2. Установите браузеры Playwright: `playwright install`
3. Запустите тесты: `pytest`
4. Для запуска в видимом режиме (headed): `pytest --headed`