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
2. Spuštění s detailním výstupem

```bash
pytest -vs
```
3. spuštění testů s vizuálním zobrazením prohlížeče

```bash
playwright install chromium
pytest -vs --headed --slowmo=1000
```



## Příklady úspěšných testů

```bash
(.venv) user@localhost:~/D/E/T/0/testing-web-playwright
➤ pytest -vs # zvolený příkaz
=============test session starts ==================
platform -- localhost/testing-web-playwright/.venv/bin/python3.14
cachedir: .pytest_cache
rootdir: localhost/testing-web-playwright
plugins: base-url-2.1.0, playwright-0.8.0
collected 3 items                                                                                                                                  

test_warhorse.py::test_warhorse_http_status[chromium] PASSED
test_warhorse.py::test_warhorse_homepage[chromium] PASSED
test_warhorse.py::test_warhorse_kcd2_presence[chromium] PASSED

============ 3 passed in 1.83s ====================
```


