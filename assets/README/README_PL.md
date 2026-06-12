<div align="center">

<p align="center"><img src="../../assets/figs/logo/logo.png" alt="DeepTutor logo" height="56" style="vertical-align: middle;">&nbsp;<img src="../../assets/figs/logo/banner.png" alt="DeepTutor" height="48" style="vertical-align: middle;"></p>

# DeepTutor: Spersonalizowane Korepetycje Natywne dla Agentów

<p align="center">
  <a href="https://deeptutor.info" target="_blank"><img alt="Docs — deeptutor.info" src="https://img.shields.io/badge/Docs-deeptutor.info%20%E2%86%97-0A0A0A?style=for-the-badge&labelColor=F5F5F4" height="36"></a>
</p>

<a href="https://trendshift.io/repositories/17099" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17099" alt="HKUDS%2FDeepTutor | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  <a href="../../README.md"><img alt="English" height="40" src="https://img.shields.io/badge/English-CDCFD4"></a>&nbsp;
  <a href="README_CN.md"><img alt="简体中文" height="40" src="https://img.shields.io/badge/简体中文-CDCFD4"></a>&nbsp;
  <a href="README_JA.md"><img alt="日本語" height="40" src="https://img.shields.io/badge/日本語-CDCFD4"></a>&nbsp;
  <a href="README_ES.md"><img alt="Español" height="40" src="https://img.shields.io/badge/Español-CDCFD4"></a>&nbsp;
  <a href="README_FR.md"><img alt="Français" height="40" src="https://img.shields.io/badge/Français-CDCFD4"></a>&nbsp;
  <a href="README_AR.md"><img alt="Arabic" height="40" src="https://img.shields.io/badge/Arabic-CDCFD4"></a>&nbsp;
  <a href="README_RU.md"><img alt="Русский" height="40" src="https://img.shields.io/badge/Русский-CDCFD4"></a>&nbsp;
  <a href="README_HI.md"><img alt="Hindi" height="40" src="https://img.shields.io/badge/Hindi-CDCFD4"></a>&nbsp;
  <a href="README_PT.md"><img alt="Português" height="40" src="https://img.shields.io/badge/Português-CDCFD4"></a>&nbsp;
  <a href="README_TH.md"><img alt="Thai" height="40" src="https://img.shields.io/badge/Thai-CDCFD4"></a>&nbsp;
  <a href="README_PL.md"><img alt="Polski" height="40" src="https://img.shields.io/badge/Polski-BCDCF7"></a>
</p>

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-000000?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=flat-square)](../../LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/HKUDS/DeepTutor?style=flat-square&color=brightgreen)](https://github.com/HKUDS/DeepTutor/releases)
[![arXiv](https://img.shields.io/badge/arXiv-2604.26962-b31b1b?style=flat-square&logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.26962)

[![Discord](https://img.shields.io/badge/Discord-Community-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/eRsjPgMU4t)
[![Feishu](https://img.shields.io/badge/Feishu-Group-00D4AA?style=flat-square&logo=feishu&logoColor=white)](../../Communication.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-07C160?style=flat-square&logo=wechat&logoColor=white)](https://github.com/HKUDS/DeepTutor/issues/78)

[Funkcje](#-główne-funkcje) · [Pierwsze kroki](#-pierwsze-kroki) · [Eksploracja](#-eksploracja-deeptutor) · [CLI](#️-deeptutor-cli--interfejs-natywny-dla-agentów) · [Wielu użytkowników](#-wielu-użytkowników--wdrożenia-współdzielone) · [Społeczność](#-społeczność-i-ekosystem)

</div>

---

> 🤝 **Zapraszamy do wszelkich form współpracy!** Głosuj na elementy planu działania lub proponuj nowe w [`Roadmap`](https://github.com/HKUDS/DeepTutor/issues/498), a szczegóły dotyczące strategii gałęzi, standardów kodowania i sposobu rozpoczęcia pracy znajdziesz w naszym [Przewodniku dla współtwórców](../../CONTRIBUTING.md).

### 📦 Wydania

> **[2026.6.12]** [v1.4.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.3) — TutorBot staje się **Partners** w produkcyjnym potoku IM z odpowiedziami na żywo w transmisji strumieniowej i 15 kanałami, Chat przechodzi na pojedynczą pętlę agenta, prawdziwa izolacja per-użytkownik dla wdrożeń wieloużytkownikowych, Visualize przebudowany z lokalną weryfikacją+naprawą, plus ulepszenia w Co-writerze, przeglądarce plików, analizie MinerU w chmurze i CLI. Dokumentacja w pełni odświeżona na [deeptutor.info](https://deeptutor.info/).

> **[2026.5.28]** [v1.4.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.2) — Stabilność + dopracowanie v1.4.1: Gemini 2.5+ odblokowany w Visualize i Chat, poprawka routingu uwierzytelniania ContextVar (#485), wzmocniony protokół etykiet reasoning + native-tools, płynne strumieniowanie UX na każdej powierzchni czatu, nowy zwijany pasek boczny Recents i obsługa lokalnego dostawcy Lemonade.

> **[2026.5.27]** [v1.4.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.1) — Poprawka bezpieczeństwa + stabilności: sandbox narzędzi TutorBot zablokowany, izolacja zasobów per-użytkownik, zapasowy obraz multimodalny dla dostawców z możliwością wizji, interfejs API HTTP/SSE do rozmowy z TutorBot i poprawka regresji czatu v1.4.0.

> **[2026.5.22]** [v1.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0) — Wydanie GA v1.4: Tryb Auto, Pamięć trzywarstwowa, agentyczne Deep Research / Solve / Question, refaktoryzacja RAG z LlamaIndex, scalenie Visualize/Animator, normalizacja wysiłku rozumowania, zapasowy schemat narzędzi i bezpieczne środowisko uruchomieniowe tury przy restartach.

<details>
<summary><b>Poprzednie wydania (ponad 2 tygodnie temu)</b></summary>

> **[2026.5.21]** [v1.4.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.4.0-beta) — Stacja robocza Pamięci trzywarstwowej (L1/L2/L3), wszystkie możliwości czatu przebudowane na jednym silniku agentycznym, wyłącznie RAG LlamaIndex i ujednolicona powierzchnia Settings + Capabilities.

> **[2026.5.10]** [v1.3.10](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.10) — Odzyskiwanie CORS zdalnego Dockera, `DISABLE_SSL_VERIFY` dla dostawców SDK, bezpieczniejsze cytowania bloków kodu i opcjonalny dodatek Matrix E2EE.

> **[2026.5.9]** [v1.3.9](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.9) — Obsługa Zulip i NVIDIA NIM dla TutorBot, bezpieczniejszy routing modelu myślącego, `deeptutor start`, podpowiedzi paska bocznego i parytety magazynu sesji.

> **[2026.5.8]** [v1.3.8](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.8) — Opcjonalne wdrożenia wieloużytkownikowe z izolowanymi obszarami roboczymi użytkowników, uprawnieniami administratora, trasami uwierzytelniania i ograniczonym dostępem do środowiska uruchomieniowego.

> **[2026.5.4]** [v1.3.7](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.7) — Poprawki modelu myślącego/dostawcy, widoczna historia indeksu Knowledge i bezpieczniejsze czyszczenie/edycja szablonów Co-Writer.

> **[2026.5.3]** [v1.3.6](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.6) — Wybór modelu oparty na katalogu dla czatu i TutorBot, bezpieczniejsze ponowne indeksowanie RAG, poprawki limitu tokenów OpenAI Responses i weryfikacja edytora Skills.

> **[2026.5.2]** [v1.3.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.5) — Płynniejsze ustawienia lokalnego uruchamiania, bezpieczniejsze zapytania RAG, czystsze lokalne uwierzytelnianie osadzania i dopracowanie trybu ciemnego Settings.

> **[2026.5.1]** [v1.3.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.4) — Trwałość czatu na stronach Book i przepływy przebudowy, odwołania z czatu do Book, silniejsza obsługa języka/rozumowania, wzmocnienie ekstrakcji dokumentów RAG.

> **[2026.4.30]** [v1.3.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.3) — Obsługa osadzania NVIDIA NIM + Gemini, ujednolicony kontekst Space dla historii czatu/umiejętności/pamięci, migawki sesji, odporność ponownego indeksowania RAG.

> **[2026.4.29]** [v1.3.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.2) — Przezroczyste adresy URL punktów końcowych osadzania, odporność ponownego indeksowania RAG dla nieprawidłowych trwałych wektorów, czyszczenie pamięci dla danych wyjściowych modelu myślącego, poprawka środowiska uruchomieniowego Deep Solve.

> **[2026.4.28]** [v1.3.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.1) — Stabilność: bezpieczniejszy routing RAG i weryfikacja osadzania, trwałość Dockera, bezpieczne wprowadzanie IME, solidność Windows/GBK.

> **[2026.4.27]** [v1.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.3.0) — Wersjonowane indeksy KB z przepływem ponownego indeksowania, przebudowany obszar roboczy Knowledge, automatyczne wykrywanie osadzania z nowymi adapterami, centrum Space.

> **[2026.4.25]** [v1.2.5](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.5) — Trwałe załączniki czatu z szufladą podglądu plików, potoki możliwości obsługujące załączniki, eksport Markdown TutorBot.

> **[2026.4.25]** [v1.2.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.4) — Załączniki tekstowe/kodu/SVG, jednopoleceniowy Setup Tour, eksport Markdown czatu, kompaktowy interfejs zarządzania KB.

> **[2026.4.24]** [v1.2.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.3) — Załączniki dokumentów (PDF/DOCX/XLSX/PPTX), wyświetlanie bloków myślenia rozumowania, edytor szablonów Soul, zapisywanie Co-Writer do notatnika.

> **[2026.4.22]** [v1.2.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.2) — System Skills tworzonych przez użytkowników, gruntowna modernizacja wydajności wprowadzania czatu, automatyczne uruchamianie TutorBot, interfejs Book Library, pełnoekranowa wizualizacja.

> **[2026.4.21]** [v1.2.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.1) — Limity tokenów na etap, regeneracja odpowiedzi we wszystkich punktach wejścia, poprawki zgodności RAG i Gemma.

> **[2026.4.20]** [v1.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.2.0) — Kompilator „żywej książki" Book Engine, wielodokumentowy Co-Writer, interaktywne wizualizacje HTML, @-wzmianka Question Bank.

> **[2026.4.18]** [v1.1.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.2) — Karta Channels sterowana schematem, konsolidacja jednopotokowego RAG, zewnętrzne prompty czatu.

> **[2026.4.17]** [v1.1.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.1) — Uniwersalne „Odpowiedz teraz", synchronizacja przewijania Co-Writer, zunifikowany panel ustawień, przycisk Stop strumieniowania.

> **[2026.4.15]** [v1.1.0](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0) — Gruntowna modernizacja matematyki blokowej LaTeX, sonda diagnostyczna LLM, wskazówki dotyczące Dockera + lokalnego LLM.

> **[2026.4.14]** [v1.1.0-beta](https://github.com/HKUDS/DeepTutor/releases/tag/v1.1.0-beta) — Sesje z możliwością zakładek, motyw Snow, puls WebSocket i automatyczne ponowne łączenie, gruntowna modernizacja rejestru osadzania.

> **[2026.4.13]** [v1.0.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.3) — Question Notebook z zakładkami i kategoriami, Mermaid w Visualize, wykrywanie niezgodności osadzania, zgodność Qwen/vLLM, obsługa LM Studio i llama.cpp oraz motyw Glass.

> **[2026.4.11]** [v1.0.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.2) — Konsolidacja wyszukiwania z rezerwą SearXNG, poprawka przełączania dostawcy, poprawki wycieków zasobów frontendowych.

> **[2026.4.10]** [v1.0.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.1) — Możliwość Visualize (Chart.js/SVG), zapobieganie duplikacjom w quizach, obsługa modelu o4-mini.

> **[2026.4.10]** [v1.0.0-beta.4](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.4) — Śledzenie postępu osadzania z ponowną próbą limitu szybkości, poprawki zależności wieloplatformowych, poprawka weryfikacji MIME.

> **[2026.4.8]** [v1.0.0-beta.3](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.3) — Natywny SDK OpenAI/Anthropic (usunięcie litellm), obsługa Math Animator w Windows, solidne parsowanie JSON i pełne i18n w języku chińskim.

> **[2026.4.7]** [v1.0.0-beta.2](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.2) — Gorące przeładowanie ustawień, zagnieżdżone dane wyjściowe MinerU, poprawka WebSocket i minimum Python 3.11+.

> **[2026.4.4]** [v1.0.0-beta.1](https://github.com/HKUDS/DeepTutor/releases/tag/v1.0.0-beta.1) — Przepisanie architektury natywnej dla agentów (~200 tys. linii): model wtyczek Tools + Capabilities, CLI i SDK, TutorBot, Co-Writer, Guided Learning i trwała pamięć.

> **[2026.1.23]** [v0.6.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.6.0) — Trwałość sesji, przyrostowe przesyłanie dokumentów, elastyczny import potoku RAG i pełna lokalizacja w języku chińskim.

> **[2026.1.18]** [v0.5.2](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.2) — Obsługa Docling dla RAG-Anything, optymalizacja systemu logowania i poprawki błędów.

> **[2026.1.15]** [v0.5.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.5.0) — Ujednolicona konfiguracja usług, wybór potoku RAG per baza wiedzy, gruntowna modernizacja generowania pytań i dostosowywanie paska bocznego.

> **[2026.1.9]** [v0.4.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.4.0) — Obsługa wielu dostawców LLM i osadzania, nowa strona główna, oddzielenie modułu RAG i refaktoryzacja zmiennych środowiskowych.

> **[2026.1.5]** [v0.3.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.3.0) — Ujednolicona architektura PromptManager, GitHub Actions CI/CD i gotowe obrazy Dockera na GHCR.

> **[2026.1.2]** [v0.2.0](https://github.com/HKUDS/DeepTutor/releases/tag/v0.2.0) — Wdrożenie Docker, uaktualnienie Next.js 16 i React 19, wzmocnienie zabezpieczeń WebSocket i poprawki krytycznych podatności.

</details>

### 📰 Aktualności

> **[2026.5.22]** 🌐 Nasza oficjalna strona dokumentacji jest dostępna na [**deeptutor.info**](https://deeptutor.info/) — przewodniki, odniesienia i wycieczki po możliwościach w jednym miejscu.

> **[2026.4.19]** 🎉 Osiągnęliśmy 20 tys. gwiazdek w 111 dni! Dziękujemy za niesamowite wsparcie — jesteśmy zaangażowani w ciągłe doskonalenie w kierunku prawdziwie spersonalizowanych i inteligentnych korepetycji dla każdego.

> **[2026.4.10]** 📄 Nasz artykuł jest już dostępny na arXiv! Przeczytaj [preprint](https://arxiv.org/abs/2604.26962), aby dowiedzieć się więcej o projekcie i pomysłach stojących za DeepTutor.

> **[2026.4.4]** Dawno się nie widzieliśmy! ✨ DeepTutor v1.0.0 jest w końcu tutaj — ewolucja natywna dla agentów z gruntownym przepisaniem architektury, TutorBot i elastycznym przełączaniem trybów na licencji Apache-2.0. Nowy rozdział się zaczyna i nasza historia trwa!

> **[2026.2.6]** 🚀 Osiągnęliśmy 10 tys. gwiazdek w zaledwie 39 dni! Ogromne podziękowania dla naszej niesamowitej społeczności!

> **[2026.1.1]** Szczęśliwego Nowego Roku! Dołącz do naszego [Discorda](https://discord.gg/eRsjPgMU4t), [WeChat](https://github.com/HKUDS/DeepTutor/issues/78) lub [Dyskusji](https://github.com/HKUDS/DeepTutor/discussions) — razem kształtujmy przyszłość DeepTutor!

> **[2025.12.29]** DeepTutor jest oficjalnie wydany!

## ✨ Główne funkcje

DeepTutor jest zorganizowany wokół natywnego dla agentów środowiska uruchomieniowego: współdzielony ChatOrchestrator kieruje każdą turę do możliwości, ToolRegistry udostępnia jednorazowe narzędzia gdy model ich potrzebuje, a CapabilityRegistry pozwala głębszym przepływom pracy przejąć kontrolę nad turą gdy zadanie wymaga struktury.

<div align="center">
<img src="../../assets/figs/system/system%20architecture.png" alt="Architektura systemu DeepTutor" width="900">
</div>

**Jeden obszar roboczy do nauki**

- **Czat jako domyślna pętla** — nieformalne korepetycje, pytania i odpowiedzi oparte na źródłach, Deep Solve, Deep Question, Deep Research, Visualize i Auto Mode współdzielą ten sam kontekst sesji i zasoby źródeł.
- **Połączone powierzchnie uczenia się** — szkice Co-Writer, strony Book, Bazy wiedzy, zasoby Space i Pamięć to oddzielne obszary robocze, ale zasilają to samo środowisko uruchomieniowe agenta zamiast stawać się izolowanymi aplikacjami.
- **Partners dla trwałego towarzystwa** — towarzyszki połączone przez IM działają teraz na tej samej pętli agenta czatu co główny produkt, ze swoim własnym syntetycznym obszarem roboczym i przypisaną biblioteką.

**Narzędzia, pamięć i kontrola**

- **Składalne narzędzia** — RAG, odczyt źródeł, odczyt/zapis pamięci, notatniki, pobieranie URL, wyszukiwanie GitHub, pauzy pytań do użytkownika, wykonanie w piaskownicy i opcjonalne narzędzia burzy mózgów/web/paper/reason mogą być montowane zgodnie z kontekstem i ustawieniami.
- **Pamięć trzywarstwowa** — ślady L1, podsumowania per-powierzchnia L2 i synteza między-powierzchniowa L3 sprawiają, że personalizacja jest możliwa do sprawdzenia zamiast ukryta za czarną skrzynką.
- **Ujednolicone ustawienia i CLI** — katalogi modeli, osadzania, wyszukiwania, sieci, serwerów MCP, narzędzi, możliwości i ustawień wdrożenia są edytowalne z interfejsu webowego i skryptowalne z `deeptutor`.

---

## 🚀 Pierwsze kroki

DeepTutor oferuje cztery ścieżki instalacji. Wszystkie współdzielą jeden układ obszaru roboczego: ustawienia żyją w `data/user/settings/` pod katalogiem, z którego uruchamiasz (lub pod `DEEPTUTOR_HOME` / `deeptutor start --home` jeśli ustawisz je jawnie). Dla pełnej aplikacji zalecany przepływ to **wybierz katalog obszaru roboczego → zainstaluj → `deeptutor init` → `deeptutor start`**.

> ✨ **v1.4.3 jest dostępny.** `pip install -U deeptutor` pobiera najnowszą stabilną wersję. Wersje wstępne (gdy dostępne) można wybrać za pomocą `pip install --pre -U deeptutor`.

### Opcja 1 — Instalacja z PyPI

Pełna lokalna aplikacja Web + CLI, bez potrzeby klonowania. Wymaga **Python 3.11+** i środowiska uruchomieniowego **Node.js 20+** na PATH (spakowany serwer standalone Next.js jest uruchamiany przez `deeptutor start`).

```bash
mkdir -p my-deeptutor && cd my-deeptutor
pip install -U deeptutor
deeptutor init     # pyta o porty + dostawcę LLM + opcjonalne osadzanie
deeptutor start    # uruchamia backend + frontend; utrzymuj terminal otwarty
```

`deeptutor init` pyta o port backendu (domyślnie `8001`), port frontendu (domyślnie `3782`), dostawcę LLM / bazowy URL / klucz API / model i opcjonalnego dostawcę osadzania dla Bazy wiedzy / RAG.

Po `deeptutor start` otwórz adres URL frontendu wydrukowany w terminalu — domyślnie [http://127.0.0.1:3782](http://127.0.0.1:3782). Naciśnij `Ctrl+C` w tym terminalu, aby zatrzymać backend i frontend. Pominięcie `deeptutor init` jest dobre dla szybkiego testu; aplikacja uruchamia się z domyślnymi portami i pustymi ustawieniami modelu, skonfiguruj je później w **Settings → Models**.

### Opcja 2 — Instalacja ze źródeł

Do programowania przy użyciu kodu źródłowego. Użyj **Python 3.11+** i **Node.js 22 LTS**, aby dopasować do CI i Dockera.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Utwórz venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv ; .\.venv\Scripts\Activate.ps1
python3 -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip

# Zainstaluj zależności backendu + frontendu
python -m pip install -e .
( cd web && npm ci --legacy-peer-deps )

deeptutor init
deeptutor start
```

Instalacje ze źródeł uruchamiają Next.js w trybie deweloperskim względem lokalnego katalogu `web/`; wszystko inne (układ konfiguracji, porty, zatrzymanie za pomocą `Ctrl+C`) odpowiada Opcji 1.

<details>
<summary><b>Środowisko Conda</b> (zamiast <code>venv</code>)</summary>

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

</details>

<details>
<summary><b>Opcjonalne dodatki instalacyjne</b> — dev / partners / matrix / math-animator</summary>

```bash
pip install -e ".[dev]"             # narzędzia testów/lint
pip install -e ".[partners]"        # SDK kanałów IM Partners + klient MCP
pip install -e ".[matrix]"          # kanał Matrix bez E2EE/libolm
pip install -e ".[matrix-e2e]"      # Matrix E2EE; wymaga libolm
pip install -e ".[math-animator]"   # addon Manim; wymaga LaTeX/ffmpeg/bibliotek systemowych
```

</details>

<details>
<summary><b>Dostosowania zależności frontendowych i rozwiązywanie problemów z serwerem deweloperskim</b></summary>

**Zmiana zależności frontendowych:** uruchom `npm install --legacy-peer-deps`, aby odświeżyć `web/package-lock.json`, a następnie zatwierdź zarówno `web/package.json`, jak i `web/package-lock.json`.

**Zablokowany serwer deweloperski:** jeśli `deeptutor start` zgłasza istniejący frontend, który nie odpowiada, zatrzymaj PID, który wydrukuje. Jeśli żaden proces Next.js nie jest uruchomiony, pliki blokady są przestarzałe — usuń je i spróbuj ponownie:

```bash
rm -f web/.next/dev/lock web/.next/lock
deeptutor start
```

</details>

### Opcja 3 — Docker

Jeden kontener dla pełnej aplikacji Web. Obrazy w GitHub Container Registry:

- `ghcr.io/hkuds/deeptutor:latest` — stabilne wydanie
- `ghcr.io/hkuds/deeptutor:pre` — wersja wstępna, gdy dostępna

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 \
  -p 127.0.0.1:8001:8001 \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

> ⚠️ **Zmapuj zarówno `3782`, jak i `8001`.** `3782` obsługuje interfejs webowy; `8001` to backend FastAPI, który twoja przeglądarka wywołuje bezpośrednio — wewnątrz kontenera nie ma proxy. Pominięcie mapowania `8001` powoduje, że strona nadal się ładuje, ale **Settings** pokazuje „Backend unreachable" i jest bezużyteczne.

Otwórz [http://127.0.0.1:3782](http://127.0.0.1:3782). Kontener tworzy `/app/data/user/settings/*.json` przy pierwszym uruchomieniu; skonfiguruj dostawców modeli ze strony Web Settings. Konfiguracja, klucze API, dzienniki, pliki obszaru roboczego, pamięć i bazy wiedzy są przechowywane w woluminie `deeptutor-data`.

- **Różne porty hosta:** zmień lewą stronę każdego mapowania `-p host:kontener` (np. `-p 127.0.0.1:8088:3782`). Jeśli zmienisz porty po stronie kontenera w `/app/data/user/settings/system.json`, uruchom ponownie i zaktualizuj prawą stronę każdego mapowania, aby pasowała.
- **Odłączony:** dodaj `-d`, następnie `docker logs -f deeptutor`, aby śledzić, `docker stop deeptutor`, aby zatrzymać, `docker rm deeptutor` przed ponownym użyciem nazwy. Wolumin `deeptutor-data` przechowuje ustawienia i obszar roboczy między restartami.

**Zdalny Docker / odwrotne proxy:** interfejs webowy działa w przeglądarce, więc przeglądarka potrzebuje adresu URL backendu, do którego może dotrzeć. W przypadku serwerów zdalnych otwórz **Settings -> Network** lub edytuj `data/user/settings/system.json`:

```json
{
  "next_public_api_base_external": "https://deeptutor.example.com"
}
```

`public_api_base` jest akceptowany jako alias zgodności i jest normalizowany do `next_public_api_base_external` przy zapisywaniu. CORS używa **źródeł** frontendu, a nie adresów URL API. Przy wyłączonym uwierzytelnianiu DeepTutor domyślnie zezwala na normalne źródła przeglądarki HTTP/HTTPS. Przy włączonym uwierzytelnianiu dodaj dokładne źródła frontendu:

```json
{
  "cors_origins": ["https://deeptutor.example.com"]
}
```

<details>
<summary><b>Łączenie z Ollama / LM Studio / llama.cpp / vLLM / Lemonade na hoście</b></summary>

Wewnątrz Dockera `localhost` to sam kontener, a nie maszyna hosta. Aby dotrzeć do usługi modelu działającej na hoście, użyj bramy hosta (zalecane):

```bash
docker run --rm --name deeptutor \
  -p 127.0.0.1:3782:3782 -p 127.0.0.1:8001:8001 \
  --add-host=host.docker.internal:host-gateway \
  -v deeptutor-data:/app/data \
  ghcr.io/hkuds/deeptutor:latest
```

Następnie w **Settings → Models** wskaż bazowy URL dostawcy na `host.docker.internal`:

- Ollama LLM: `http://host.docker.internal:11434/v1`
- Ollama embedding: `http://host.docker.internal:11434/api/embed`
- LM Studio: `http://host.docker.internal:1234/v1`
- llama.cpp: `http://host.docker.internal:8080/v1`
- Lemonade: `http://host.docker.internal:13305/api/v1`

Docker Desktop (macOS/Windows) zazwyczaj rozwiązuje `host.docker.internal` bez `--add-host`. Na Linuksie flaga jest przenośnym sposobem tworzenia tej nazwy hosta w nowoczesnym Docker Engine.

**Alternatywa dla Linuksa — sieć hosta:** dodaj `--network=host` i usuń flagi `-p`. Kontener bezpośrednio współdzieli sieć hosta, więc otwórz [http://127.0.0.1:3782](http://127.0.0.1:3782) (lub `frontend_port` w `system.json`), a usługi hosta są dostępne pod normalnymi adresami URL localhost, jak `http://127.0.0.1:11434/v1`. Pamiętaj, że sieciowanie hosta bezpośrednio ujawnia porty kontenera na hoście i może powodować konflikty z istniejącymi usługami.

</details>

### Piaskownica wykonania kodu (umiejętności biurowe)

Wbudowane umiejętności biurowe — **docx / pdf / pptx / xlsx** — działają, sprawiając że model pisze krótki skrypt Python (`python-docx`, `reportlab`, `openpyxl`, …), uruchamia go przez narzędzia `exec` / `code_execution` i zwraca adres URL do pobrania. Te narzędzia montują się za każdym razem, gdy backend piaskownicy jest aktywny, co ma miejsce **domyślnie** w każdym kształcie wdrożenia:

- **Lokalne (Opcja 1 / 2) i Docker (Opcja 3, pojedynczy kontener):** ograniczona piaskownica podprocesu uruchamia kod modelu (lokalnie na hoście lub wewnątrz kontenera pod Dockerem — kontener będący własną granicą izolacji).
- **docker-compose:** zamiast tego kierowany do utwardzonego, o najmniejszych uprawnieniach **sidecar runner** (`Dockerfile.runner`) przez `DEEPTUTOR_SANDBOX_RUNNER_URL` — najsilniejsza postawa, automatycznie preferowana gdy jest obecna.

Piaskownica podprocesu jest kontrolowana przez ustawienie `sandbox_allow_subprocess` w `data/user/settings/system.json` (domyślnie `true`). Uruchamianie kodu generowanego przez model na twoim hoście to prawdziwa decyzja dotycząca zaufania — ustaw na `false` (lub eksportuj `DEEPTUTOR_SANDBOX_ALLOW_SUBPROCESS=0`), aby wyłączyć wykonanie po stronie hosta kosztem tego, że umiejętności biurowe nie będą mogły produkować plików.

### Opcja 4 — Tylko CLI

Gdy nie potrzebujesz interfejsu webowego. Pakiet tylko CLI jest instalowany ze źródłowego kodu, a nie z PyPI.

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Utwórz venv (macOS/Linux). Windows PowerShell:
#   py -3.11 -m venv .venv-cli ; .\.venv-cli\Scripts\Activate.ps1
python3 -m venv .venv-cli && source .venv-cli/bin/activate
python -m pip install --upgrade pip

python -m pip install -e ./packaging/deeptutor-cli
deeptutor init --cli
deeptutor chat
```

`deeptutor init --cli` współdzieli ten sam układ `data/user/settings/` co pełna aplikacja, ale pomija monity o porty backendu/frontendu i domyślnie wyłącza osadzanie (wybierz `Yes` jeśli planujesz używać `deeptutor kb …` lub narzędzi RAG). Nadal zapisuje kompletny układ środowiska uruchomieniowego (`system.json`, `auth.json`, `integrations.json`, `model_catalog.json`, `main.yaml`, `agents.yaml`) i nadal pyta o aktywnego dostawcę LLM i model.

<details>
<summary><b>Typowe polecenia</b></summary>

```bash
deeptutor chat                                          # interaktywny REPL
deeptutor chat --capability deep_solve --tool rag --kb my-kb
deeptutor run chat "Explain Fourier transform"
deeptutor run deep_solve "Solve x^2 = 4" --tool rag --kb my-kb
deeptutor kb create my-kb --doc textbook.pdf
deeptutor memory show
deeptutor config show
```

</details>

Lokalna instalacja `deeptutor-cli` nie zawiera zasobów webowych ani zależności serwera. Zachowaj źródłowy kod — instalacja edytowalna wskazuje na niego. Aby dodać aplikację Web później, zainstaluj pakiet PyPI (Opcja 1) i uruchom `deeptutor init` + `deeptutor start` z tego samego obszaru roboczego.

### Odniesienie do konfiguracji

<details>
<summary><b>Pliki konfiguracyjne w <code>data/user/settings/</code></b> — odniesienie JSON/YAML</summary>

Wszystko w `data/user/settings/` to zwykły JSON/YAML. Strona **Settings** w przeglądarce jest zalecanym edytorem.

| Plik | Cel |
|:---|:---|
| `model_catalog.json` | Profile dostawców LLM, osadzania i wyszukiwania; klucze API; aktywne modele |
| `system.json` | Porty backendu/frontendu, publiczna baza API, CORS, weryfikacja SSL, katalog załączników |
| `auth.json` | Opcjonalny przełącznik uwierzytelniania, nazwa użytkownika, hash hasła, ustawienia tokena/cookie |
| `integrations.json` | Opcjonalne ustawienia PocketBase i integracji sidecar |
| `interface.json` | Preferencje języka / motywu / paska bocznego interfejsu użytkownika |
| `main.yaml` | Domyślne zachowanie środowiska uruchomieniowego i wstrzykiwanie ścieżek |
| `agents.yaml` | Ustawienia temperatury i tokenów możliwości/narzędzi |

Plik `.env` w katalogu głównym projektu **nie** jest czytany jako plik konfiguracyjny aplikacji. Dla minimalnej konfiguracji modelu otwórz **Settings → Models**, dodaj profil LLM (bazowy URL / klucz API / nazwa modelu) i zapisz. Dodaj profil osadzania tylko jeśli planujesz korzystać z funkcji Bazy wiedzy / RAG.

</details>

## 📖 Eksploracja DeepTutor

Wycieczka README podąża za powierzchniami produktu w kolejności, w jakiej najczęściej się z nimi spotkasz: Chat, Partner, Co-Writer, Book, Knowledge, Space, Memory i Settings.

### 💬 Chat — Pętla agenta, której naprawdę używasz

<div align="center">
<img src="../../assets/figs/webui/chat.png" alt="Obszar roboczy czatu DeepTutor" width="900">
</div>

Chat to domyślna możliwość i miejsce, gdzie zaczyna się większość pracy. Jeden wątek może rozmawiać normalnie, wywoływać narzędzia, opierać się na wybranych bazach wiedzy, czytać załączniki, pisać rekordy notatnika i kontynuować z tym samym zasobem źródeł przez tury.

<div align="center">
<img src="../../assets/figs/system/chat-agent-loop.png" alt="Pętla agenta czatu DeepTutor" width="900">
</div>

Obecna pętla jest celowo prosta: model myśli w rundach, wywołuje narzędzia gdy są przydatne, obserwuje wyniki narzędzi i kończy gdy ma wystarczające dowody. Narzędzia przełączalne przez użytkownika to `brainstorm`, `web_search`, `paper_search` i `reason`; kontekstowe narzędzia takie jak `rag`, `read_source`, `read_memory`, `write_memory`, `read_skill`, `load_tools`, `exec`, `web_fetch`, `ask_user`, `list_notebook`, `write_note` i `github` montują się gdy tura ma właściwy kontekst.

Chat jest również punktem startowym dla głębszych możliwości: `deep_solve` dla wypracowanego rozumowania, `deep_question` dla generowania pytań, `deep_research` dla cytowanych raportów, `visualize` i `math_animator` dla wizualnych wyników, `auto` dla routingu i `mastery_path` dla przepływów planów nauki.

### 🤝 Partner — Stali towarzysze na tym samym mózgu

<div align="center">
<img src="../../assets/figs/webui/partners.png" alt="Obszar roboczy partners DeepTutor" width="900">
</div>

Partners zastępują starszy silnik TutorBot czystszym modelem: każda przychodząca wiadomość webowa lub IM staje się normalną turą ChatOrchestrator wewnątrz obszaru roboczego o zasięgu partnera. Nie ma oddzielnego mózgu bota do synchronizowania.

<div align="center">
<img src="../../assets/figs/system/partners-architecture.png" alt="Architektura partners DeepTutor" width="900">
</div>

Każdy partner ma `SOUL.md`, wybór modelu, kanały, politykę narzędzi i przypisaną bibliotekę. Bazy wiedzy, umiejętności i notatniki są kopiowane do `data/partners/<id>/workspace/`, więc te same narzędzia RAG, umiejętności, notatnika i pamięci działają bez specjalnych przypadków.

<div align="center">
<img src="../../assets/figs/webui/partners02.png" alt="Widok szczegółów partnera DeepTutor" width="900">
</div>

Warstwa kanałów jest sterowana schematem i może łączyć się z platformami IM, takimi jak Feishu, Telegram, Slack, DingTalk, QQ/Napcat, WeCom, WhatsApp, Zulip, Matrix i Microsoft Teams w zależności od zainstalowanych dodatków i skonfigurowanych danych uwierzytelniających.

### ✍️ Co-Writer — Redagowanie Markdown ze świadomością zaznaczenia

Co-Writer to obszar roboczy Markdown z podzielonym widokiem dla raportów, samouczków, notatek i długich artefaktów uczenia się. Dokumenty są automatycznie zapisywane, renderują podgląd na żywo i mogą być zapisane z powrotem do notatników gdy szkic staje się kontekstem wielokrotnego użytku.

Zaznacz tekst i poproś DeepTutor o przepisanie, rozszerzenie lub skrócenie. Agent edycji śledzi wywołania narzędzi i może oprzeć edycję na bazie wiedzy lub dowodach webowych, więc Co-Writer zachowuje się bardziej jak edytor z odzyskiwaniem niż oddzielone pole tekstowe.

### 📖 Book — Żywe książki z twoich materiałów

<p align="center">
<img src="../../assets/figs/webui/book01.png" alt="Widok czytania książki DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book02.png" alt="Widok interaktywnego bloku książki DeepTutor" width="31%">
&nbsp;
<img src="../../assets/figs/webui/book03.png" alt="Widok tworzenia książki DeepTutor" width="31%">
</p>

Book przekształca wybrane źródła w interaktywny materiał do nauki. Książka może zaczynać się od baz wiedzy, notatników, banków pytań lub historii czatu; przepływ tworzenia proponuje strukturę przed wygenerowaniem treści, więc użytkownicy mogą sprawdzić kształt zamiast akceptować ślepe jednorazowe wyjście.

BookEngine kompiluje strony do typowanych bloków: tekst, sekcje, callouts, quizy, fiszki, osie czasu, kod, figury, interaktywny HTML, animacje, grafy konceptów, dogłębne analizy i notatki użytkownika. Polecenia konserwacyjne takie jak `deeptutor book health` i `deeptutor book refresh-fingerprints` pomagają wykryć, kiedy wiedza źródłowa odbiega od skompilowanych stron.

### 📚 Knowledge — Wersjonowane biblioteki RAG

<div align="center">
<img src="../../assets/figs/webui/knowledge.png" alt="Obszar roboczy bazy wiedzy DeepTutor" width="900">
</div>

Bazy wiedzy to kolekcje dokumentów stojące za RAG. Obecny stos to wyłącznie LlamaIndex, z płaskim układem przechowywania `version-N` zakodowanym przez sygnaturę osadzania. Ponowne indeksowanie zachowuje poprzednie wersje i unika nadpisywania działającego indeksu podczas przetwarzania nowych dokumentów.

Obszar roboczy webowy udostępnia pliki, przesyłanie, wersje indeksów i ustawienia. CLI odzwierciedla ten sam cykl życia za pomocą `deeptutor kb list`, `info`, `create`, `add`, `search`, `set-default` i `delete`.

### 🌐 Space — Umiejętności, persony i kontekst wielokrotnego użytku

<div align="center">
<img src="../../assets/figs/webui/space.png" alt="Obszar roboczy Space DeepTutor" width="900">
</div>

Space to warstwa biblioteki dla kontekstu wielokrotnego użytku. Gromadzi umiejętności tworzone przez użytkowników, persony, notatniki, historię czatu i zasoby w stylu banku pytań, aby agent mógł być sterowany celowym kontekstem zamiast doraźnym promptowaniem.

Umiejętności są przechowywane jako pliki `SKILL.md` w obszarze roboczym użytkownika i mogą być oznaczone, edytowane lub zachowane jako tylko do odczytu gdy są wbudowane. Persony podążają za tym samym pomysłem dla roli i głosu. Te zasoby mogą być przypisane do partnerów, przywoływane w czacie i ponownie używane w przepływach uczenia się.

### 🧠 Memory — Inspekcjonowalna personalizacja

<div align="center">
<img src="../../assets/figs/webui/memory01.png" alt="Stacja robocza pamięci DeepTutor" width="900">
</div>

Memory to system trzywarstwowy zakorzeniony w aktywnym obszarze roboczym użytkownika: `trace/<surface>/<date>.jsonl` dla śladów zdarzeń L1, `L2/<surface>.md` dla faktów per-powierzchnia i `L3/<recent|profile|scope|preferences>.md` dla syntezy między-powierzchniowej.

<div align="center">
<img src="../../assets/figs/webui/memory02.png" alt="Graf pamięci DeepTutor" width="900">
</div>

Obsługiwane powierzchnie pamięci to `chat`, `notebook`, `quiz`, `kb`, `book`, `tutorbot` i `cowriter`. Starszawa nazwa `tutorbot` pozostaje w warstwie pamięci dla zgodności, mimo że model towarzysza zorientowany na produkt to teraz Partners. Stacja robocza pozwala inspekcjonować, edytować, uruchamiać konsolidację i używać grafu do śledzenia zsyntetyzowanych twierdzeń z powrotem do faktów wspierających i surowych zdarzeń.

### ⚙️ Settings — Jeden płaszczyzna kontroli

<div align="center">
<img src="../../assets/figs/webui/settings.png" alt="Obszar roboczy ustawień DeepTutor" width="900">
</div>

Settings to operacyjna płaszczyzna kontroli. Obejmuje wygląd, porty sieciowe i zewnętrzną bazę API, katalogi LLM i osadzania, dostawców wyszukiwania, parsowanie MinerU, budżety możliwości, rytm pamięci, serwery MCP, wbudowane narzędzia i listę włączonych opcjonalnych narzędzi.

Większość ustawień używa przepływu szkic-i-zastosuj, aby użytkownicy mogli testować dostawców przed ich zatwierdzeniem. Pliki `.env` w katalogu głównym projektu są celowo ignorowane; konfiguracja środowiska uruchomieniowego żyje w `data/user/settings/*.json`, chyba że `DEEPTUTOR_HOME` lub `deeptutor start --home` wskaże aplikację gdzie indziej.

---

## ⌨️ DeepTutor CLI — Interfejs natywny dla agentów

DeepTutor to natywny CLI: ten sam punkt wejścia `deeptutor` może inicjalizować obszar roboczy, uruchamiać aplikację webową, uruchamiać jednorazową możliwość, otwierać interaktywny REPL, zarządzać bazami wiedzy, inspekcjonować sesje, utrzymywać książki i obsługiwać partnerów.

```bash
deeptutor run chat "Explain Fourier transform" --tool rag --kb textbook
deeptutor run deep_solve "Solve x^2 = 4" --tool reason
deeptutor chat --capability deep_research --kb papers
deeptutor partner create math-tutor --soul "Socratic math tutor"
deeptutor kb create calculus --doc textbook.pdf
```

<details>
<summary><b>Odniesienie do poleceń</b></summary>

| Polecenie | Opis |
|:---|:---|
| `deeptutor init` | Utwórz lub zaktualizuj `data/user/settings` dla bieżącego obszaru roboczego |
| `deeptutor start [--home PATH]` | Uruchom backend + frontend razem |
| `deeptutor serve [--port PORT]` | Uruchom tylko backend FastAPI |
| `deeptutor run <capability> <message>` | Uruchom pojedynczą turę możliwości (`chat`, `deep_solve`, `deep_question`, `deep_research`, `visualize`, `math_animator`, `auto`, `mastery_path`) |
| `deeptutor chat` | Interaktywny REPL z kontrolkami możliwości, narzędzia, KB, notatnika i historii |
| `deeptutor partner list/create/start/stop` | Zarządzaj partnerami połączonymi przez IM |
| `deeptutor kb list/info/create/add/search/set-default/delete` | Zarządzaj bazami wiedzy LlamaIndex |
| `deeptutor memory show/clear` | Inspekcjonuj dokumenty pamięci L2/L3 lub wyczyść pamięć L1/wszystko |
| `deeptutor session list/show/open/rename/delete` | Zarządzaj współdzielonymi sesjami |
| `deeptutor notebook list/create/show/add-md/replace-md/remove-record` | Zarządzaj notatnikami z plików Markdown |
| `deeptutor book list/health/refresh-fingerprints` | Inspekcjonuj książki i odświeżaj odciski źródeł |
| `deeptutor plugin list/info` | Inspekcjonuj zarejestrowane narzędzia i możliwości |
| `deeptutor config show` | Wydrukuj podsumowanie konfiguracji |
| `deeptutor provider login <provider>` | Zarządzaj logowaniem OAuth dostawcy tam, gdzie jest obsługiwane |

</details>

Dystrybucja tylko CLI znajduje się w `packaging/deeptutor-cli`; w tym kodzie źródłowym powinna być zainstalowana ze źródeł za pomocą `python -m pip install -e ./packaging/deeptutor-cli`. Publiczny pakiet `deeptutor-cli` nie jest obecnie dostępny na PyPI, więc główna sekcja Pierwsze kroki zachowuje ścieżkę instalacji ze źródeł.

---

## 👥 Wielu użytkowników — Wdrożenia współdzielone

<div align="center">
<img src="../../assets/figs/webui/multi-user.png" alt="Obszar roboczy administratora wielu użytkowników DeepTutor" width="900">
</div>

Uwierzytelnianie jest opcjonalne i domyślnie wyłączone. Gdy jest włączone, DeepTutor staje się wdrożeniem współdzielonym z jednym obszarem roboczym administratora, obszarami roboczymi per-użytkownik, obszarami roboczymi partnerów i stanem systemu pod jednym drzewem `data/`.

```text
data/
├── user/                         # Obszar roboczy i ustawienia administratora
├── users/<uid>/                  # Zasięg użytkownika niebędącego administratorem
│   ├── user/chat_history.db
│   ├── user/settings/interface.json
│   ├── user/workspace/{chat,co-writer,book,memory,notebook,...}
│   └── knowledge_bases/...
├── partners/<id>/workspace/      # Zasięg syntetycznego użytkownika partnera
└── system/
    ├── auth/users.json
    ├── grants/<uid>.json
    └── audit/usage.jsonl
```

Pierwszy zarejestrowany użytkownik staje się administratorem i może konfigurować katalogi modeli, dane uwierzytelniające dostawców, bazy wiedzy, umiejętności i uprawnienia użytkowników. Użytkownicy niebędący administratorami otrzymują izolowaną historię czatu, pamięć, notatniki, osobiste bazy wiedzy i zredagowaną stronę Settings; zasoby przypisane przez administratora pojawiają się jako ograniczone, tylko do odczytu opcje zamiast ujawniania kluczy API lub wewnętrznych elementów dostawcy.

Dla lokalnego testu ustaw `data/user/settings/auth.json`, aby włączyć uwierzytelnianie, uruchom ponownie `deeptutor start`, zarejestruj pierwszego administratora w `/register`, a następnie utwórz użytkowników z `/admin/users` i przypisz modele, KB, umiejętności, politykę narzędzi, politykę MCP i dostęp do wykonania kodu przez uprawnienia.

Tryb PocketBase pozostaje integracją dla jednego użytkownika w tym drzewie; wdrożenia wieloużytkownikowe powinny pozostawić `integrations.pocketbase_url` puste i używać domyślnych magazynów uwierzytelniania i sesji JSON/SQLite, chyba że zewnętrzny magazyn użytkowników został jawnie zaprojektowany dla tego wdrożenia.

---

## 🌐 Społeczność i ekosystem

DeepTutor stoi na ramionach wybitnych projektów open-source:

| Projekt | Rola w DeepTutor |
|:---|:---|
| [**nanobot**](https://github.com/HKUDS/nanobot) | Ultralekki silnik agenta, który zasilał oryginalny TutorBot (Partners teraz działają na pętli agenta czatu DeepTutor) |
| [**LlamaIndex**](https://github.com/run-llama/llama_index) | Kręgosłup potoku RAG i indeksowania dokumentów |
| [**ManimCat**](https://github.com/Wing900/ManimCat) | Generowanie animacji matematycznych sterowane sztuczną inteligencją dla Math Animator |

**Z ekosystemu HKUDS:**

| [⚡ LightRAG](https://github.com/HKUDS/LightRAG) | [🤖 AutoAgent](https://github.com/HKUDS/AutoAgent) | [🔬 AI-Researcher](https://github.com/HKUDS/AI-Researcher) | [🧬 nanobot](https://github.com/HKUDS/nanobot) |
|:---:|:---:|:---:|:---:|
| Prosty i szybki RAG | Framework agentów bez kodu | Automatyczne badania | Ultralekki agent AI |


## 🤝 Współtworzenie

<div align="center">

Mamy nadzieję, że DeepTutor stanie się prezentem dla społeczności. 🎁

<a href="https://github.com/HKUDS/DeepTutor/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/DeepTutor&max=999" alt="Współtwórcy" />
</a>

</div>

Przeczytaj [CONTRIBUTING.md](../../CONTRIBUTING.md) w celu uzyskania wytycznych dotyczących konfigurowania środowiska programistycznego, standardów kodu i przepływu pracy dla pull requestów.

## ⭐ Historia gwiazdek

<div align="center">

<a href="https://www.star-history.com/#HKUDS/DeepTutor&type=timeline&legend=top-left">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&theme=dark&legend=top-left" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
    <img alt="Wykres historii gwiazdek" src="https://api.star-history.com/svg?repos=HKUDS/DeepTutor&type=timeline&legend=top-left" />
  </picture>
</a>

</div>

<p align="center">
 <a href="https://www.star-history.com/hkuds/deeptutor">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
   <img alt="Ranking historii gwiazdek" src="https://api.star-history.com/badge?repo=HKUDS/DeepTutor" />
  </picture>
 </a>
</p>

<div align="center">

**[Data Intelligence Lab @ HKU](https://github.com/HKUDS)**

[⭐ Dodaj gwiazdkę](https://github.com/HKUDS/DeepTutor/stargazers) · [🐛 Zgłoś błąd](https://github.com/HKUDS/DeepTutor/issues) · [💬 Dyskusje](https://github.com/HKUDS/DeepTutor/discussions)

---

Licencjonowany na podstawie [Apache License 2.0](../../LICENSE).

<p>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.DeepTutor&style=for-the-badge&color=00d4ff" alt="Odwiedziny">
</p>

</div>
