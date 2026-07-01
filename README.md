# Testing Web Playwright

Konzolová aplikace pro testování webu za pomocí nástroje Playwright.

Engeto akademy projekt který využívá nástroje playwright a pytest

## Požadavky

- Python 3.10+
- pytest
- pytest-playwright
- playwright

## Instalace

1. Naklonuj repozitář:

   ```bash
   git clone https://github.com/doctorxcz/testing-web-playwright
   cd testing-web-playwright
   ```

2. Vytvoř a aktivuj virtuální prostředí:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate    # Mac/Linux
   .venv\Scripts\activate       # Windows
   ```

3. Nainstaluj závislosti:

   ```bash
   pip install -r requirements.txt
   ```



## Spuštění Testů

1. Základní CLI spuštění:

```bash
pytest
```

2. spuštění testů s vizuálním zobrazením prohlížeče

```bash
playwright install chromium
pytest --headed --slowmo=1000
```



## Příklady úspěšných testů

```bash
(.venv) user@localhost:~/D/E/T/0/testing-web-playwright
➤ pytest # zvolený příkaz
=============test session starts ==================
platform -- localhost/testing-web-playwright/.venv/bin/python3.14
cachedir: .pytest_cache
rootdir: localhost/testing-web-playwright
plugins: base-url-2.1.0, playwright-0.8.0
collected 6 items                                                                            

test_warhorse.py::TestNavigace::test_menu_na_projekty[chromium] PASSED                        [ 16%]
test_warhorse.py::TestNavigace::test_prepnuti_jazyka_na_en[chromium] PASSED                   [ 33%]
test_warhorse.py::TestExterniOdkazy::test_hra_otevre_deepsilver[chromium] PASSED              [ 50%]
test_warhorse.py::TestExterniOdkazy::test_youtube_odkaz[chromium] PASSED                      [ 66%]
test_warhorse.py::TestStranky::test_neexistujici_stranka_vraci_404[chromium] PASSED           [ 83%]
test_warhorse.py::TestStranky::test_kontakt_obsahuje_mailto[chromium] PASSED                  [100%]

============ 6 passed in 12.94s ====================
```




