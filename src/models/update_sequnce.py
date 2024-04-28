import psycopg2

from src.settings import settings


def update_sequence():
    cursor = None

    try:
        # Connect to the database
        connection = psycopg2.connect(settings.db_url)

        # Create a cursor
        cursor = connection.cursor()
        l_cursor = connection.cursor()

        # Execute the SQL script
        select_tables = """
            SELECT DISTINCT concat(tables.table_schema, '.', tables.table_name) AS table_name
            FROM information_schema.tables
            INNER JOIN information_schema.columns ON tables.table_name = columns.table_name
            WHERE tables.table_schema = 'public' AND columns.column_name = 'id'
        """

        cursor.execute(select_tables)

        for row in cursor.fetchall():
            table_name = row[0]
            print('processing started for ', table_name)

            sql_cmd = f'select pg_get_serial_sequence(\'{table_name}\', \'id\');'

            l_cursor.execute(sql_cmd)
            sequence_name = l_cursor.fetchone()[0]
            if not sequence_name:
                continue

            sql_cmd = f"""
                select max(id) 
                from {table_name}
            """
            # print(sql_cmd)
            l_cursor.execute(sql_cmd)
            table_max_id = l_cursor.fetchone()[0]

            if not table_max_id:
                continue

            sql_cmd = f'select setval(\'{sequence_name}\', COALESCE({table_max_id}, 0) + 1, false);'
            l_cursor.execute(sql_cmd)
            print('processing ended for ', table_name)

        connection.commit()
        print("Sequence updated successfully!")

    except psycopg2.Error as error:
        print("Error:", error)

    finally:
        if cursor in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


if __name__ == "__main__":
    update_sequence()
