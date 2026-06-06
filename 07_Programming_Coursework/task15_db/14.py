"""
Task:
 The town of Fiftyville has called upon you to solve the mystery of the stolen duck. 
 Authorities believe that the thief stole the duck and then, shortly afterwards, 
 took a flight out of town with the help of an accomplice. Your goal is to identify:

Who the thief is,
What city the thief escaped to, and
Who the thief’s accomplice is who helped them escape
All you know is that the theft took place on July 28, 2023 and that it took place on Humphrey Street.

How will you go about solving this mystery? The Fiftyville authorities have taken some of the town’s records from around 
the time of the theft and prepared a SQLite database for you, fiftyville.db, which contains tables of data from around the town. 
You can query that table using SQL SELECT queries to access the data of interest to you. Using just the information in the database, your task is to solve the mystery.

Expected result is both thief and accomplce are male.
Their names are connected with batman.

"""

import sqlite3
# pip install sqlite3
connection = sqlite3.connect("fiftyville.db")
cursor = connection.cursor()

# this is the only line that needs editing
#List of all query_code used to determine thief and his accomplice:

#query_code = "SELECT description FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street'"
#query_code = "SELECT name, transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%'"
#query_code = "SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 AND 25"
#query_code = "SELECT name, license_plate FROM people WHERE license_plate IN ('5P2BI95', '94KL13X', '6P58WS2', '4328GD8', 'G412CB7', 'L93JTIZ', '32W7JE', '0NTHK55')"
#query_code = "SELECT people.name FROM atm_transactions JOIN bank_accounts ON atm_transactions.account_number = bank_accounts.account_number JOIN people ON bank_accounts.person_id = people.id WHERE atm_transactions.year = 2021 AND atm_transactions.month = 7 AND atm_transactions.day = 28 AND atm_transactions.atm_location = 'Leggett Street' AND atm_transactions.transaction_type = 'withdraw'"
#query_code = "SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') AND year = 2021 AND month = 7 AND day = 29 ORDER BY hour, minute LIMIT 1)) AND name IN ('Bruce', 'Iman', 'Luca')"
#query_code = "SELECT p1.name AS caller_name, p2.name AS receiver_name, duration FROM phone_calls pc JOIN people p1 ON pc.caller = p1.phone_number JOIN people p2 ON pc.receiver = p2.phone_number WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60"
#query_code = "SELECT f.id, a.city, f.hour, f.minute FROM flights f JOIN airports a ON f.destination_airport_id = a.id WHERE f.year = 2021 AND f.month = 7 AND f.day = 29 ORDER BY f.hour, f.minute LIMIT 1"
#query_code = "SELECT people.name FROM passengers JOIN people ON passengers.passport_number = people.passport_number WHERE passengers.flight_id = 36"
print("Thief: Bruce")
print("Accomplice: Robin")




#cursor.execute(query_code)
result = cursor.fetchall()
for row in result:
    for item in row:
        print(item, end="\t")
    print()
connection.close()