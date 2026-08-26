import pytest
from playwright.sync_api import sync_playwright


"""

"""


@pytest.fixture() # by default scope is function
def browser():
    # this is setup
    print("****** Browser fixture start *******")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=10000)
        yield browser
        # teardown
        browser.close()
    print("******* Browser fixture end ******")


@pytest.fixture
def page(browser):
    print("********** page started *********")
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    print("********* page end *********")
