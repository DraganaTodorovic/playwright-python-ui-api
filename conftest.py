import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.logger import get_logger
from utils.config_reader import get_config

# ==========================================
# CONFIG VALUES
# ==========================================
HEADLESS = get_config("playwright", "headless").lower() == "true"
VIDEO = get_config("playwright", "video").lower() == "true"
TIMEOUT = int(get_config("playwright", "timeout"))
BROWSERS = ["chromium", "firefox", "webkit"]   # Multi-browser

# ==========================================
# LOGGER (SESSION LEVEL)
# ==========================================
@pytest.fixture(scope="session")
def logger():
    """Globalni logger fixture"""
    log_file = os.path.join("reports", "logs", f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    logger = get_logger(log_file)
    logger.info("=== Test session started ===")
    yield logger
    logger.info("=== Test session finished ===")

# ==========================================
# PLAYWRIGHT SESSION
# ==========================================
@pytest.fixture(scope="session")
def playwright_instance():
    """Pokreće i zatvara Playwright sesiju"""
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


# ==========================================
# PARAMETRIZACIJA BROWSERA
# ==========================================
# def pytest_generate_tests(metafunc):
#     """
#     Ako test koristi fixture 'browser_name', svaki test se izvršava 3 puta:
#     chromium + firefox + webkit
#     """
#     if "browser_name" in metafunc.fixturenames:
#         print("pytest_generate_tests")
#         metafunc.parametrize("browser_name", BROWSERS)


# ==========================================
# MAIN FIXTURE: page
# ==========================================
@pytest.fixture(scope="function")
def page(playwright_instance, request, logger, browser_name):
    """Otvara browser pre svakog testa"""
    test_name = request.node.name
    videos_dir = os.path.join("reports", "videos")
    screenshots_dir = os.path.join("reports", "screenshots")
    os.makedirs(videos_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    """
    Creates browser + context based on selected browser
    """
    # Map browser name to Playwright browser type
    # browser_map = {
    #     "chromium": playwright_instance.chromium,
    #     "firefox": playwright_instance.firefox,
    #     "webkit": playwright_instance.webkit,
    # }
    #
    # if browser_name not in browser_map:
    #     raise ValueError(
    #         f"Unsupported browser '{browser_name}'. "
    #         f"Use chromium | firefox | webkit"
    #     )
    #
    # browser = browser_map[browser_name].launch(headless=HEADLESS)

    # browser = playwright_instance.chromium.launch(headless=HEADLESS)
    # Dinamički biramo browser instance
    browser = getattr(playwright_instance, browser_name).launch(headless=HEADLESS)
    # browser = playwright_instance.
    context = browser.new_context(record_video_dir=videos_dir if VIDEO else None)
    page = context.new_page()

    # Timeout settings
    page.set_default_timeout(TIMEOUT)
    page.set_default_navigation_timeout(TIMEOUT)

    # logger.info(f"=== Starting test: {test_name} ===")
    logger.info(f"=== Starting test: {test_name} ({browser_name}) ===")
    yield page

    # Test failure → screenshot
    if request.node.rep_call.failed:
        screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{browser_name}_{datetime.now().strftime('%H%M%S')}.png")
        page.screenshot(path=screenshot_path)
        logger.error(f"❌ Test failed: {test_name} ({browser_name}) → Screenshot saved to {screenshot_path}")
    else:
        logger.info(f"✅ Test passed: {test_name} ({browser_name})")

    # # Ako test padne -> screenshot i video
    # if request.node.rep_call.failed:
    #     screenshot_path = os.path.join(screenshots_dir, f"{test_name}_{datetime.now().strftime('%H%M%S')}.png")
    #     page.screenshot(path=screenshot_path)
    #     logger.error(f"❌ Test failed: {test_name} - Screenshot saved to {screenshot_path}")
    # else:
    #     logger.info(f"✅ Test passed: {test_name}")

    context.close()
    browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Omogućava pristup statusu testa u fixture-ima (pass/fail)"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)



# import os
# import pytest
# from datetime import datetime
# from playwright.sync_api import sync_playwright
# from utils.logger import get_logger
# from utils.config_reader import get_config
#
# # ==========================================
# # CONFIG VALUES
# # ==========================================
# HEADLESS = get_config("playwright", "headless").lower() == "true"
# VIDEO = get_config("playwright", "video").lower() == "true"
# TIMEOUT = int(get_config("playwright", "timeout"))
# BROWSERS = ["chromium", "firefox", "webkit"]   # Multi-browser
#
# # ==========================================
# # LOGGER (SESSION LEVEL)
# # ==========================================
# @pytest.fixture(scope="session")
# def logger():
#     log_file = os.path.join(
#         "reports", "logs", f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
#     )
#     logger = get_logger(log_file)
#     logger.info("=== Test session started ===")
#     yield logger
#     logger.info("=== Test session finished ===")
#
#
# # ==========================================
# # PLAYWRIGHT SESSION
# # ==========================================
# @pytest.fixture(scope="session")
# def playwright_instance():
#     p = sync_playwright().start()
#     yield p
#     p.stop()
#
#
# # ==========================================
# # PARAMETRIZACIJA BROWSERA
# # ==========================================
# def pytest_generate_tests(metafunc):
#     """
#     Ako test koristi fixture 'browser_name', svaki test se izvršava 3 puta:
#     chromium + firefox + webkit
#     """
#     if "browser_name" in metafunc.fixturenames:
#         metafunc.parametrize("browser_name", BROWSERS)
#
#
# # ==========================================
# # MAIN FIXTURE: page
# # ==========================================
# @pytest.fixture(scope="function")
# def page(playwright_instance, browser_name, request, logger):
#     """Otvara browser na osnovu browser_name parametra."""
#
#     test_name = request.node.name
#     videos_dir = os.path.join("reports", "videos")
#     screenshots_dir = os.path.join("reports", "screenshots")
#     os.makedirs(videos_dir, exist_ok=True)
#     os.makedirs(screenshots_dir, exist_ok=True)
#
#     # Dinamički biramo browser instance
#     browser = getattr(playwright_instance, browser_name).launch(headless=HEADLESS)
#
#     context = browser.new_context(record_video_dir=videos_dir if VIDEO else None)
#
#     page = context.new_page()
#
#     # Timeout settings
#     page.set_default_timeout(TIMEOUT)
#     page.set_default_navigation_timeout(TIMEOUT)
#
#     logger.info(f"=== Starting test: {test_name} ({browser_name}) ===")
#
#     yield page
#
#     # Test failure → screenshot
#     if request.node.rep_call.failed:
#         screenshot_path = os.path.join(
#             screenshots_dir,
#             f"{test_name}_{browser_name}_{datetime.now().strftime('%H%M%S')}.png"
#         )
#         page.screenshot(path=screenshot_path)
#         logger.error(f"[FAILED] {test_name} ({browser_name}) → Screenshot saved to {screenshot_path}")
#     else:
#         logger.info(f"[PASSED] {test_name} ({browser_name})")
#
#     context.close()
#     browser.close()
#
#
# # ==========================================
# # HOOK za rep_call (pass/fail detection)
# # ==========================================
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """Omogućava pristup statusu testa (pass/fail) unutar fixtures."""
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, f"rep_{rep.when}", rep)

