"""
pip install playwright
playwright install

Using playwright we can automate with all the latest browsers.
We can automate user interface and api.


playwright fixtures
browser:
browser_context:
page:

locators: by using locators we can locate the web elements in web page
get_by_role:
get_by_label:
get_by_value:
get_by_text:
get_by_placeholder:
locator():
xpath:
relative xpath: //tagname[@attribute=value]
absolute xpath: /html/body/div
css_selector:
id:

codegen: by using codegen we can generate automation script by perform navigation
cmd: playwright codegen --target=python https://automationexercise.com/

Web element operations:
click():
fill():
type():
clear():
check():
uncheck():
select_options():
text:

Assertions:
to_be_visible()
to_be_hidden()
to_be_enabled()
to_be_disabled()
to_be_checked()
to_have_text()
to_contain_text()
to_have_url()
to_have_title()

waits:
auto wait:

"""

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=2000) # browser engine
    # browser1 = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://automationexercise.com/")
    # page.get_by_role("link", name=" Products").click()
    # page.get_by_placeholder(text='Search Product').fill('shirts')
    # page.get_by_text(text=' Cart').first.click()
    expect(page.locator('[class="fa fa-home"]')).to_be_visible(timeout=60000) # assertion
    page.locator('[class="fa fa-home"]')
    # print(dir(page))
