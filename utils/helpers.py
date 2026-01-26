
def is_element_visible(page, selector):
    try:
        return page.locator(selector).is_visible()
    except:
        return False
