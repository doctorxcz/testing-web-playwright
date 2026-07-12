import re
from playwright.sync_api import expect


# ==============================================================================
# POMOCNÉ FUNKCE
# ==============================================================================

class WarhorseHelper:
    """Pomocné funkce sdílené napříč všemi testovacími třídami."""

    @staticmethod
    def otevri_stranku(page, url):
        return page.goto(url, wait_until="domcontentloaded")

    @staticmethod
    def over_status_kod(response, ocekavany_kod=200):
        # Kontrola HTTP status kódu odpovědi
        assert response is not None, "Server vůbec neodpověděl"
        assert response.status == ocekavany_kod, (
            f"Očekáván status {ocekavany_kod}, server vrátil {response.status}"
        )

    @staticmethod
    def over_url_obsahuje(page, cast_url, timeout=5000):
        # Ověří, že URL obsahuje daný řetězec – nativní Playwright čekání
        expect(page).to_have_url(re.compile(cast_url), timeout=timeout)

    @staticmethod
    def over_ze_text_existuje(page, text_na_strance, timeout=5000):
        page.wait_for_selector(f"text={text_na_strance}", state="visible", timeout=timeout)
        assert page.get_by_text(text_na_strance, exact=False).first.is_visible()

    @staticmethod
    def klikni_a_over_url(page, selektor, ocekavana_url, timeout=5000):
        # Ověření URL po kliknutí na element – nativní Playwright čekání
        page.click(selektor)
        expect(page).to_have_url(re.compile(ocekavana_url), timeout=timeout)

    @staticmethod
    def klikni_a_zachyt_popup(page, selektor):
        # Popup je nová záložka, která se otevře po kliknutí na odkaz
        with page.expect_popup() as popup_info:
            page.locator(selektor).first.click()
        nova_zalozka = popup_info.value
        nova_zalozka.wait_for_load_state("domcontentloaded")
        return nova_zalozka

    @staticmethod
    def scrollni_na_element_a_klikni(page, selektor):
        # Skroluje na element, počká než bude viditelný a klikne na něj.
        element = page.locator(selektor).first
        element.scroll_into_view_if_needed()
        element.wait_for(state="visible", timeout=5000)
        element.click()


# ==============================================================================
# TESTY
# ==============================================================================

h = WarhorseHelper  # zkratka pro volání v testech


class TestNavigace:
    """Testy navigace a přechodu mezi stránkami."""

    def test_menu_na_projekty(self, homepage):
        # Klikne na 'Projekty' v menu a ověří přechod na stránku her
        h.klikni_a_over_url(homepage, "text=Projekty", "projekty")
        h.over_ze_text_existuje(homepage, "Kingdom Come: Deliverance")

    def test_prepnuti_jazyka_na_en(self, homepage):
        # Klikne na přepínač EN a ověří přepnutí webu do angličtiny
        h.scrollni_na_element_a_klikni(homepage, "a[lang='en']")
        h.over_url_obsahuje(homepage, "/en")
        h.over_ze_text_existuje(homepage, "About us")


class TestExterniOdkazy:
    """Testy externích odkazů – ověření otevření nové záložky."""

    def test_hra_otevre_deepsilver(self, homepage):
        # Klikne na odkaz hry a ověří otevření externí stránky deepsilver.com
        h.klikni_a_over_url(homepage, "text=Projekty", "projekty")
        nova_zalozka = h.klikni_a_zachyt_popup(homepage, "a:has-text('Oficiální stránka hry')")
        assert "deepsilver.com" in nova_zalozka.url
        assert "kingdom-come" in nova_zalozka.url.lower()

    def test_youtube_odkaz(self, homepage):
        # Klikne na YouTube v patičce a ověří otevření správného kanálu
        nova_zalozka = h.klikni_a_zachyt_popup(homepage, "a[href*='youtube.com']")
        assert "youtube.com" in nova_zalozka.url
        assert "warhorsestudios" in nova_zalozka.url.lower()


class TestStranky:
    """Testy chybových stavů a validace obsahu stránek."""

    def test_neexistujici_stranka_vraci_404(self, page, base_url):
        # Zadá neexistující URL a ověří chybovou odpověď serveru (404)
        response = h.otevri_stranku(page, f"{base_url}/tato-stranka-neexistuje-12345")
        h.over_status_kod(response, 404)

    def test_kontakt_obsahuje_mailto(self, page, base_url):
        # Přejde na kontaktní stránku a ověří přítomnost mailto: odkazu
        h.otevri_stranku(page, f"{base_url}/cs/kontakt")
        mailto = page.locator("a[href^='mailto:']").first
        expect(mailto).to_be_visible(timeout=5000)
        assert "info@warhorsestudios.cz" in mailto.get_attribute("href")




