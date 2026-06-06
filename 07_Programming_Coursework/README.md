# 07 — Programming Coursework Portfolio (16 tasks)

> Practical programming tasks: Python → C → SQL → Flask web app
> Praktiskie programmēšanas darbi: Python → C → SQL → Flask web aplikācija

**Context:** RTU programming course (rtudip classroom), RMCE01, 2024/2025
**Source:** 16 GitHub Classroom assignments

---

## EN — for GitHub README / EN CV

**Programming Coursework — 16 progressive tasks (RTU, 2024/2025)**

Full programming foundations spanning Python, C/C++, SQL and web development. Tasks were autograded (input/output + function tests) and developed in GitHub Classroom workflow.

### Python fundamentals (tasks 01–09)
- **01 hello** — input/output, formatted strings
- **02 questions** — type casting, conditionals, function-test autograding
- **03 pyramids** — nested loops (5 progressive variants)
- **04 text-analysis** — Coleman-Liau readability index (letters / words / sentences)
- **05 functions** — `cash` change-making with greedy coin algorithm; functions: `get_cents`, `calculate_quarters`, etc.
- **06 scrabble-lists** — Scrabble scoring with lists, two-player comparison
- **07 dictionary** — fruit-calorie lookup using dicts, `find_fruit()` function with case-insensitive matching
- **08 libraries** — FIGlet ASCII-art (third-party library install + use)
- **09 api** — Game-of-Thrones quotes API (JSON request, 3 Tyrion + 2 Jon Snow quotes parsed)

### C / C++ (tasks 10–13)
- **10 introduction-to-c** — first C programs: `half.cpp`, pyramid printing
- **11 continuing-with-c** — arrays, type conversions, total/average hours calculator
- **12 c-scrabble** — Scrabble scoring rewritten in C (same problem as task 06, different language)
- **13 sort-and-search** — multiple algorithms in C++:
  - Bubble sort with linked lists (known + unknown size)
  - Selection sort with arrays
  - Linear search (arrays + linked lists)
  - Binary search

### Memory management in C (task 14)
- **14 memory-allocation** — read `plates.txt` into dynamically allocated `char*` array using `malloc` with `fread` 7-byte buffer reads; `\n → \0` normalization; correct cleanup on allocation failure (free earlier entries, close file); **verified with valgrind for memory leaks**.

### Databases — SQL (task 15)
- **15 db** — 14 SQL queries against two SQLite databases (`movies.db`, `fiftyville.db`); progression from simple SELECT (1 pt) through JOINs (2 pt) to complex multi-table investigations (3–4 pt). Example: list all actors who starred in *Toy Story* via LEFT JOIN across `people`, `stars`, `movies`.
- 25 points total across 14 tasks.

### Full-stack web — Flask (task 16)
- **16 web** — Spotify-themed music recommendation site:
  - Flask routes (`/`, `/input_page.html`, `/output_page.html`) with GET/POST handling
  - SQLite persistence via parameterized queries (SQL-injection safe)
  - Jinja templates with `head.html` partial, Bootstrap, custom CSS, JavaScript
  - Form: mood dropdown + genre dropdown + username text + checkbox + submit
  - Output page persists each lookup to DB and embeds Spotify iframe (track-ID extraction from URL)
  - Includes a thoughtful AI-usage reflection README documenting how ChatGPT was used (and verified) during development

**Skills demonstrated:** Python · C / C++ · SQL (SQLite, JOINs, aggregation) · Flask · Jinja templates · HTML/CSS · Bootstrap · JavaScript · REST/JSON APIs · data structures (linked lists, arrays, dicts) · sorting & searching algorithms · dynamic memory management (`malloc`/`free`, valgrind) · GitHub Classroom workflow · parameterized SQL queries

---

## LV — for LV CV

**Programmēšanas studiju darbu portfolio — 16 praktisku uzdevumu (RTU, 2024/2025)**

Pilna programmēšanas pamatu apgūšana: Python → C/C++ → SQL → tīmekļa aplikācija. Uzdevumi autograduēti caur GitHub Classroom.

**Tēmu pārskats:**
- **Python (01–09):** ievads/izvads, datu tipi, cikli, virkņu apstrāde (Coleman-Liau lasāmības indekss), funkcijas, saraksti, vārdnīcas, ārējās bibliotēkas (FIGlet), API pieprasījumi (JSON parsēšana).
- **C / C++ (10–13):** ievads C valodā, masīvi un tipa konversijas, algoritmi (bubble sort, selection sort, linear & binary search) gan masīviem, gan saistītajiem sarakstiem.
- **Dinamiskā atmiņa C (14):** `malloc`/`fread`/`free` lietojums, korektais kļūdu apstrādes ceļš (atbrīvošana atmiņas piešķiršanas neveiksmes gadījumā), pārbaude ar **valgrind**.
- **SQL (15):** 14 SQL pieprasījumi pret SQLite datu bāzēm — no vienkāršiem SELECT līdz vairāku tabulu JOIN izmeklēšanas vaicājumiem.
- **Tīmekļa aplikācija — Flask (16):** Spotify stila mūzikas rekomendāciju vietne ar Jinja šablonu sistēmu, Bootstrap, custom CSS, JavaScript; SQLite glabāšana ar parametrizētiem vaicājumiem (drošība pret SQL injekciju); dinamiska Spotify iframe iebūvēšana.

**Prasmes:** Python · C / C++ · SQL (SQLite, JOIN, agregācija) · Flask · Jinja · HTML/CSS · Bootstrap · JavaScript · REST API · datu struktūras · šķirošanas un meklēšanas algoritmi · dinamiskā atmiņa · GitHub Classroom

---

## Files in this folder
- `task01_hello/` … `task16_web/` — full source for each of 16 tasks
- Each task includes its original README and the working code committed to GitHub Classroom

## Highlights for CV (top 3 to lead with)
1. **task16_web** — Flask + SQLite + Bootstrap full-stack site
2. **task15_db** — 14 SQL queries across SQLite schemas (movies + fiftyville investigation)
3. **task14_memory-allocation** — C dynamic memory with valgrind validation

## CV bullet (short, EN)
> *16-task programming portfolio (RTU, 2024/2025) covering Python fundamentals, C/C++ with dynamic memory (valgrind-verified), data structures and algorithms (linked lists, sort/search), SQL on SQLite, and a Flask + Bootstrap full-stack web app.*

## CV bullet (short, LV)
> *16 uzdevumu programmēšanas portfolio (RTU, 2024/2025): Python pamati, C/C++ ar dinamisko atmiņu (valgrind pārbaude), datu struktūras un algoritmi, SQL uz SQLite un Flask + Bootstrap tīmekļa aplikācija.*
