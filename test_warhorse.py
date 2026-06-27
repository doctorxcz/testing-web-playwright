import pytest
import time

# Otevře stránku a vrátí odpověď serveru
def otevri_stranku(page, url):
    response = page.goto(url, wait_until="domcontentloaded")
    return response

# Kontrola HTTP status kódu odpovědi — defaultně očekáváme 200 OK
def over_status_kod(response, ocekavany_kod=200):
    assert response is not None, "Server vůbec neodpověděl"
    assert response.status == ocekavany_kod

# Ověří, že URL obsahuje daný řetězec — někdy se načítá se zpožděním
def over_url_obsahuje_s_cekanim(page, cast_url, timeout_sekund=5):
    konec = time.time() + timeout_sekund
    while time.time() < konec:
        if cast_url in page.url:
            return
        time.sleep(0.2)
    assert cast_url in page.url

# Ověří, že je titulek stránky očekávaný — načítá pomaleji
def over_nadpis_stranky_s_cekanim(page, ocekavany_titulek, timeout_sekund=5):
    konec = time.time() + timeout_sekund
    while time.time() < konec:
        if ocekavany_titulek.lower() in page.title().lower():
            return
        time.sleep(0.2)
    assert ocekavany_titulek.lower() in page.title().lower()

# Ověří, že daný text je na stránce viditelný
def over_ze_text_existuje(page, text_na_strance):
    page.wait_for_selector(
        f"text={text_na_strance}",
        state="visible",
        timeout=5000
    )
    assert page.get_by_text(text_na_strance, exact=False).first.is_visible()

# proměnná základní URL pro testy
BASE_URL = "https://www.warhorsestudios.cz"


def test_warhorse_http_status(page):
    # Kontrola, že server vrací 200 OK pro hlavní stránku a odpovídá na požadavek
    response = otevri_stranku(page, BASE_URL)
    over_status_kod(response, 200)


def test_warhorse_homepage(page):
    # Načte homepage a ověří, že obsahuje očekávaný nadpis a URL
    otevri_stranku(page, BASE_URL)
    over_nadpis_stranky_s_cekanim(page, "warhorse")
    over_url_obsahuje_s_cekanim(page, "warhorsestudios.cz")


def test_warhorse_kcd2_presence(page):
    # Hledání textu "Kingdom Come: Deliverance" na stránce her
    otevri_stranku(page, f"{BASE_URL}/games")
    over_ze_text_existuje(page, "Kingdom Come: Deliverance")



