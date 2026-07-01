import pytest


# ==============================================================================
# conftest.py – sdílené fixtury pro všechny testy
# ==============================================================================


@pytest.fixture
def homepage(page, base_url):
    """
    Otevře homepage a ověří základní předpoklady:
      - server odpovídá (není None)
      - vrací HTTP status 200

    Automaticky odklidí cookie banner pokud se objeví.
    """
    page.add_locator_handler(
        page.locator("[data-fragment='cp.acceptAllBtn']"),
        lambda locator: locator.click()
    )

    response = page.goto(base_url, wait_until="domcontentloaded")

    assert response is not None, "Server vůbec neodpověděl"
    assert response.status == 200, (
        f"Homepage vrátila neočekávaný status: {response.status}"
    )

    return page

