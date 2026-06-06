import sqlite3
# pip install sqlite3
connection = sqlite3.connect("./data_files/custom_db.db", check_same_thread=False)
cursor = connection.cursor()

def create_db_table():
    query_code = """
        CREATE TABLE IF NOT EXISTS demo (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            int_field1 INTEGER NOT NULL,
            int_field2 INTEGER NOT NULL,
            int_field3 INTEGER NOT NULL,
            int_field4 INTEGER NOT NULL,
            int_field5 INTEGER NOT NULL,
            str_field1 TEXT NOT NULL,
            str_field2 TEXT NOT NULL,
            str_field3 TEXT NOT NULL,
            str_field4 TEXT NOT NULL,
            str_field5 TEXT NOT NULL
        )
        """
    cursor.execute(query_code)

def output_all_contents():
    query_code = "SELECT * FROM demo"
    cursor.execute(query_code)
    result = cursor.fetchall()
    for row in result:
        for item in row:
            print(item, end="\t")
        print()

def insert_demo_record():
    query_code = """
        INSERT INTO demo (
            int_field1, int_field2, int_field3, int_field4, int_field5,
            str_field1, str_field2, str_field3, str_field4, str_field5
        ) VALUES (
            1, 2, 3, 4, 5,
            "a", "b", "c", "d", "e"
        )
        """
    cursor.execute(query_code)
    connection.commit()

def remove_demo_record():
    query_code = "DELETE FROM demo"
    cursor.execute(query_code)
    connection.commit()

def drop_table():
    query_code = "DROP TABLE demo"
    cursor.execute(query_code)
    connection.commit()


def insert_data(v1,v2,v3,v4,v5,v6,v7,v8,v9,v10):
    query_code = """
        INSERT INTO demo (
            int_field1, int_field2, int_field3, int_field4, int_field5,
            str_field1, str_field2, str_field3, str_field4, str_field5
        ) VALUES (
            ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?
        )
        """
    cursor.execute(query_code, (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10))
    connection.commit()

def retrieve_all_data():
    query_code = "SELECT * FROM demo"
    cursor.execute(query_code)
    result = cursor.fetchall()
    return result

def try_query_add(query_code):
    cursor.execute(query_code)
    connection.commit()

def try_query_retrieve(query_code):
    cursor.execute(query_code)
    result = cursor.fetchall()
    return result

# # this is the only line that needs editing
# query_code = "SELECT * FROM demo"

# cursor.execute(query_code)
# result = cursor.fetchall()
# for row in result:
#     for item in row:
#         print(item, end="\t")
#     print()
# connection.close()
if __name__ == "__main__":
    create_db_table()
    insert_demo_record()
    insert_data(10,20,30,40,50,"aa","bb","cc","dd","ee")
    output_all_contents()
    remove_demo_record()
    drop_table()
    create_db_table()
    # connection.close()