<div align="center">

[← back to portfolio](../README.md)

# 💻 Project 07

[![Tech1](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge)](#)
[![Tech2](https://img.shields.io/badge/-C/C++-00599C?style=for-the-badge)](#)
[![Tech3](https://img.shields.io/badge/-SQL-003B57?style=for-the-badge)](#)

</div>

---

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

*Fig. 3 — Flask app routes (`app.py`): GET/POST handling for th