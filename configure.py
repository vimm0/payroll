import sqlite3


# conn = sqlite3.connect('example.db')
# c = conn.cursor()
#
# # Create table
# c.execute('''CREATE TABLE employee(date text, trans text, symbol text, qty real, price real)
# CREATE TABLE employee(date text, trans text, symbol text, qty real, price real)
# CREATE TABLE employee(date text, trans text, symbol text, qty real, price real)
# ''')
#
# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
#
# # Save (commit) the changes
# conn.commit()
#
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "payroll.db"
    employee = """CREATE TABLE employee(employeeid INTEGER PRIMARY KEY, name TEXT, position TEXT, salary REAL);"""
    attendance = """ CREATE TABLE attendance(attendanceid INTEGER, status TEXT, emp_name TEXT, FOREIGN KEY(emp_name) REFERENCES employee(employeeid));"""
    payroll = """CREATE TABLE payroll(payrollid INTEGER, payment REAL);"""
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, employee)
        create_table(conn, attendance)
        create_table(conn, payroll)
        # create tasks table
        # create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
