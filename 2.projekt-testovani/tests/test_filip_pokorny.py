import pytest

#1.test - checks if the title contains the text "Webový designer"
def test_title(page):
    print("Navigating to the homepage.")
    page.goto("https://filippokorny.cz/")

    print("Locating the title element...")
    title = page.locator(".elementor-widget-heading h1")

    print("Asserting the title text...")
    assert title.inner_text() == "Webový designer"

#2.test - closes the cookie bar
def test_click_cookies(page):
    id_button_refuse = "CybotCookiebotDialogBodyButtonDecline"

    print("Navigating to the homepage.")
    page.goto("https://filippokorny.cz/")
    print("Locating the refuse cookies button...")
    refuse_button = page.locator(f"button#{id_button_refuse}")
    print("Clicking the refuse cookies button...")
    refuse_button.click()

    print("Locating the cookie consent bar...")
    cookie_bar = page.locator("div.CybotCookiebotDialogContentWrapper")
    print("Waiting for the cookie consent bar to disappear...")
    cookie_bar.wait_for(state="hidden")

    print("Asserting the cookie consent bar is hidden...")
    assert cookie_bar.is_visible() == False

#3. test - tests if the page redirects to the "reference" subpage after clicking the "reference" button
def test_redirection_on_reference(page):
    print("Navigation to the homepage.")
    page.goto("https://filippokorny.cz/")

    print("Waiting for the 'Reference' link to be visible")
    reference_link = page.locator("a.elementor-item:has-text('Reference')").nth(0)
    reference_link.wait_for(state="visible")
    print("Clicking the 'References' link.")
    reference_link.click()

    print("Waiting for the 'References' page to load...")
    page.wait_for_url("https://filippokorny.cz/reference/")

    print("Asserting the URL matches the 'References' page...")
    assert page.url == "https://filippokorny.cz/reference/"

# 4. test - tests the completion and submission of the form
def test_fill_formular(page):
    print("Navigation to the homepage.")
    page.goto("https://filippokorny.cz/kontakty/")

    print("Filling in name.")    
    page.locator("input#form-field-name").fill("Testovací Jméno")

    print("Filling email.")
    page.locator("input#form-field-email").fill("test@seznam.cz")

    print("Filling phone.")
    page.locator("input#form-field-field_55bfca5").fill("123456789")

    print("Entering a message into the field.")    
    page.locator("textarea#form-field-message").fill("Testovací zpráva.")

    print("Sending formular")
    page.locator("button[type='submit']").click()

    print("Waiting for confirmation message.")
    page.wait_for_selector(".elementor-message-success", timeout=5000)

    print("Validating confirmation message.")
    confirmation_message = page.locator(".elementor-message-success").text_content()
    assert confirmation_message.strip() == "Formulář byl úspěšně odeslán."