# 07 — Programming Coursework: 16 Progressive Tasks

> 16 autograded assignments — Python → C/C++ → SQL → Flask web app
> A full programming foundation built over one academic year

**Context** RTU programming course (GitHub Classroom: `rtudip`) · RMCE01 · 2024/2025
**Workflow** GitHub Classroom — each task is a separate `rtudip/practical-task-N-*-Lavs-Daniels-Skots-231RMC173` repo with autograded tests (input/output + function tests)
**Languages** Python · C / C++ · SQL · HTML / CSS / JavaScript · Jinja
**Frameworks** Flask · Bootstrap · SQLite

---

## What this folder is

A consolidated archive of all 16 practical tasks I completed in the programming course. Each task is in its own subfolder with the original source files exactly as they were submitted (and autograded as passing) to GitHub Classroom.

The 16 tasks form a deliberate progression:
- Tasks 01–09 build up Python from `print()` to API requests
- Tasks 10–13 transition to C/C++ for low-level work
- Task 14 adds dynamic memory management with valgrind-verified correctness
- Task 15 introduces SQL on SQLite
- Task 16 caps the year with a full-stack Flask + Bootstrap + SQLite web application

---

## Python fundamentals (tasks 01–09)

| # | Folder | Topic | Key technique |
|---|---|---|---|
| 01 | `task01_hello/` | I/O, formatted strings | `input()`, f-strings |
| 02 | `task02_questions/` | Type casting, conditionals | int/float conversion, function-test autograding |
| 03 | `task03_pyramids/` | Nested loops, 5 variants | Building patterns of increasing difficulty |
| 04 | `task04_text-analysis/` | Coleman-Liau readability | String iteration, sentence detection, grade-level formula |
| 05 | `task05_functions/` | Cash / change-making | Greedy coin algorithm in 4 functions: `get_cents()`, `calculate_quarters(change)`, etc |
| 06 | `task06_scrabble-lists/` | Scrabble scoring | List comprehensions, letter→points map |
| 07 | `task07_dictionary/` | Fruit-calorie lookup | `find_fruit()` function with case-insensitive matching |
| 08 | `task08_libraries/` | FIGlet ASCII-art | Third-party library install + use, requirements file |
| 09 | `task09_api/` | Game of Thrones quotes API | HTTP request, JSON parsing — 3 Tyrion + 2 Jon Snow quotes |

---

## C / C++ (tasks 10–13)

| # | Folder | Topic | Key technique |
|---|---|---|---|
| 10 | `task10_introduction-to-c/` | First C programs | `half.cpp`, pyramid printing, `int main()`, basic I/O |
| 11 | `task11_continuing-with-c-and-c/` | Arrays, type conversions | Total/average hours calculator with array input |
| 12 | `task12_c-scrabble/` | Scrabble in C | Same problem as task 06, different language |
| 13 | `task13_sort-and-search/` | Sort & search algorithms in C++ | Multiple implementations (see below) |

Task 13 in detail (`task13_sort-and-search/`):
- `bubble_sort.cpp` — bubble sort with linked lists (known + unknown element count variants)
- `selection_sort.cpp` — selection sort with arrays
- `linear_search.cpp` — linear search (arrays + linked lists)
- `binary_search.cpp` — binary search on arrays
- All compile to working executables that the grader runs against test inputs

---

## C memory management (task 14)

The first task that requires the engineer to think about memory ownership.

`task14_memory-allocation/main.c`:

- Reads `plates.txt` 7 bytes at a time using `fread` into a buffer
- Allocates `char *plates[8]` dynamically with `malloc(strlen(buffer) + 1)`
- Normalizes line breaks (`\n → \0`)
- Frees previously allocated entries on subsequent allocation failure — **clean error recovery**
- Closes the file pointer
- **Verified with valgrind** — zero memory leaks

```c
plates[idx] = malloc(strlen(buffer) + 1);
if (!plates[idx])
{
    fprintf(stderr, "Memory allocation failed at plate %d\n", idx);
    // cleanup any earlier allocations
    for (int j = 0; j < idx; j++)
        free(plates[j]);
    fclose(infile);
    return 1;
}
```

This is the "knowing what done means" pattern in C — allocation is paired with cleanup, even in the error path.

---

## SQL (task 15)

![DB schema](images/07_sql_schema.png)

*Fig. 1 — SQLite schema for `movies.db`: tables `people`, `movies`, `stars`, `ratings`, `directors` and the foreign-key relationships between them. Task 15 has 14 queries practicing JOINs across these tables.*

`task15_db/` contains 14 SQL query files (`1.py` through `14.py`), each one wrapping a query in a small Python harness so the grader can verify the output.

Task scoring breakdown:
- Tasks 1–7: 1 point each (7 total) — simple SELECT, WHERE, ORDER BY
- Tasks 8–11: 2 points each (8 total) — multi-table JOIN, GROUP BY, HAVING
- Tasks 12–13: 3 points each (6 total) — nested queries, complex multi-table investigations
- Task 14: 4 points — full investigation reconstruction
- **Total: 25 points**

![SQL queries](images/07_sql_queries.png)

*Fig. 2 — Examples of the 14 SQL queries written for task 15: from simple SELECT to multi-table LEFT JOINs and the fiftyville-investigation-style queries that reconstruct a sequence of events from witness records*

Example — task 15.8 (movies):

```sql
SELECT name
FROM people
LEFT JOIN stars ON people.id = stars.person_id
LEFT JOIN movies ON stars.movie_id = movies.id
WHERE title = 'Toy Story';
```

This is a 3-table LEFT JOIN chain that reads people → their roles → the movies they were in, filtered to the Toy Story title.

The fiftyville investigation (task 14) is a recreated "CS50-style" mystery where multiple tables (people, bank_accounts, bakery_security_logs, courthouse_security_logs, atm_transactions, phone_calls, flights, airports) must be joined to identify the culprit. Practices building complex investigative queries.

> Note: The `movies.db` (77 MB) and `fiftyville.db` reference databases are NOT included in this folder — they are part of the assignment source dataset and can be re-downloaded from CS50 if needed. The query files are in the folder.

---

## Full-stack web (task 16)

![Flask routes](images/07_flask_routes.png)

*Fig. 3 — Flask app routes (`app.py`): GET/POST handling for the input form and output page, with SQLite parameterized inserts*

The capstone of the course year. `task16_web/` contains a complete Flask web application — a Spotify-themed music recommendation site.

**Architecture:**
- `app.py` — Flask backend with three routes:
  - `/` and `/index.html` — landing page
  - `/input_page.html` — form (mood dropdown + genre dropdown + username + checkbox + submit)
  - `/output_page.html` — displays recommendation, embedded Spotify iframe, and saves the lookup to SQLite
- `sql_connection.py` — SQLite layer:
  - `create_db_table()` — initial schema setup on first run
  - `insert_data(...)` — parameterized INSERT (no SQL injection)
  - `retrieve_all_data()` — SELECT all rows
  - `try_query_add()` / `try_query_retrieve()` — generic query interface
- `templates/` — Jinja2 templates: `head.html` (shared header), `index.html`, `input_page.html`, `output_page.html`, `form_example.html` (reference)
- `static/style.css` — custom CSS extending Bootstrap
- `static/images/` — assets (Spotify icon, profile photo)
- `data_files/custom_db.db` — SQLite database file

**Stack:** Python + Flask + Jinja2 + SQLite + Bootstrap + custom CSS + JavaScript

**Database design:** generic `demo` table with 5 INT fields and 5 STRING fields — proves the concept of a flexible schema even though only 5 string fields are actively used (username, mood, genre, track_title, spotify_url).

**Recommendation engine:** simple two-key dictionary `recommendations[mood][genre]` returning `(track_title, spotify_url)`. Easy to extend.

`README(AI usage).md` — Documents the AI usage during development (Daniel's own reflection from the time of submission): which problems were AI-assisted, why, and what was verified manually before committing.

---

## Files & folder structure

Each `taskNN_*/` subfolder contains the original source files for that task — exactly as they were committed to and graded by GitHub Classroom. Folders may include:
- Source code (`*.py`, `*.c`, `*.cpp`, `*.h`)
- Test files (often `test_1.py`, `test_2.py`, ...)
- README from the assignment (`README.md`)
- Lesson materials (`lesson.py` where present)
- Build outputs (cleaned via `.gitignore` for C tasks)

---

## How to run a task

### Python tasks (01-09)
```bash
cd task04_text-analysis
python main.py
```

### C tasks (10-14)
```bash
cd task14_memory-allocation
gcc -Wall -o read main.c
./read plates.txt
```

For task 14, to verify zero memory leaks:
```bash
valgrind --leak-check=full ./read plates.txt
```

### SQL task (15)
```bash
cd task15_db
# Requires movies.db / fiftyville.db (excluded from repo, see note above)
python 8.py
```

### Web task (16)
```bash
cd task16_web
pip install flask
flask run
# Visit http://127.0.0.1:5000 in browser
```

---

## Skills demonstrated

- **Python** — fundamentals through API requests
- **C / C++** — fundamentals, arrays, linked lists, algorithms
- **Dynamic memory management in C** — `malloc`/`free`, clean error recovery, valgrind-verified
- **Data structures & algorithms** — sorting (bubble, selection), searching (linear, binary), linked lists
- **SQL (SQLite)** — SELECT, JOIN, LEFT JOIN, GROUP BY, complex multi-table queries
- **Flask** — routes, GET/POST, Jinja templates
- **Bootstrap + custom CSS** — responsive UI with custom Spotify-themed styling
- **JavaScript** — basic frontend interactivity
- **REST / JSON APIs** — HTTP request, JSON parsing
- **GitHub Classroom workflow** — autograded assignment submissions
- **Parameterized SQL queries** — SQL injection avoidance

---

## Latvian summary (LV)

Šis ir 16 progresīvu programmēšanas uzdevumu komplekts no RTU programmēšanas kursa (GitHub Classroom, 2024./2025.):

- **Python pamati (01–09)** — ievads/izvads, datu tipi, cikli, virkņu apstrāde (Coleman-Liau lasāmības indekss), funkcijas, saraksti, vārdnīcas, ārējās bibliotēkas (FIGlet), API pieprasījumi (Game of Thrones JSON)
- **C / C++ (10–13)** — pirmais C kods, masīvi un tipa konversijas, algoritmi: bubble sort ar saistītajiem sarakstiem, selection sort, linear & binary search
- **Dinamiskā atmiņa C (14)** — `malloc`/`fread`/`free` lietojums, korektais kļūdu apstrādes ceļš (atbrīvošana atmiņas piešķiršanas neveiksmes gadījumā), **valgrind verifikācija**
- **SQL (15)** — 14 SQL pieprasījumi pret SQLite datu bāzēm (movies.db + fiftyville.db) — no SELECT/WHERE līdz vairāku tabulu JOIN izmeklēšanas vaicājumiem. Kopā 25 punkti.
- **Pilna tīmekļa aplikācija (16)** — Spotify stila mūzikas rekomendāciju vietne ar Flask + SQLite + Jinja + Bootstrap + custom CSS + JS. Datu bāzes glabāšana ar parametrizētiem vaicājumiem (drošība pret SQL injekciju), dinamiska Spotify iframe iebūvēšana.

Visu uzdevumu pirmkods atrodas `taskNN_*/` apakšmapēs ar oriģinālo struktūru no GitHub Classroom — visi 16 ir izpildīti un automātiski novērtēti.
