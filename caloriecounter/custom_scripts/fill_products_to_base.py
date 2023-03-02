# Перенос данных из csv в бд. Файл csv должен находиться в данной директории
import os
import csv
import sqlite3
from dotenv import load_dotenv

load_dotenv()


def main():
    n = 0
    csv_file_path = os.getenv('CSV_FILE_PATH', default=None)
    db_path = os.getenv('DB_PATH')
    with open(csv_file_path, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 
        for row in reader:
            if n == 0:
                n = 1
                continue
            connect = sqlite3.connect(db_path)
            cursor = connect.cursor()
            sqlite_insert_with_param = """INSERT INTO calories_products (name, calories, proteins, fats, carbohydrates)
                                        VALUES (?, ?, ?, ?, ?)"""
            data_tuple = (
                row[0],
                row[1] if row[1] not in (0, '', None) else 0,
                row[2] if row[2] not in (0, '', None) else 0,
                row[4] if row[4] not in (0, '', None) else 0,
                row[3] if row[3] not in (0, '', None) else 0
            )
            cursor.execute(sqlite_insert_with_param, data_tuple)
            connect.commit()
            cursor.close()


if __name__ == '__main__':
    main()
