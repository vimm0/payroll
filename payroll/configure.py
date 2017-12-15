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


def create_table(conn, table_name):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(table_name)
        if table_name:
            from Input import name, position, salary, date
            c.execute("insert into employee (date, name, position, salary) values (?, ?, ?, ?)", (date, name, position, salary))
            # c.execute("insert into attendance (status, emp_name) values (?, ?, ?)", (status, salary))
            # c.execute("insert into payroll (date, payment, emp_name) values (?, ?, ?)", ( date, payment, name))
            # YYYY - MM - DD
        conn.commit()

    except Error as e:
        print(e)


def main():
    database = "payroll.db"
    employee = """CREATE TABLE employee(employeeid INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, name TEXT, position TEXT, salary REAL);"""
    # attendance = """ CREATE TABLE attendance(attendanceid INTEGER AUTOINCREMENT, status TEXT, emp_name TEXT, FOREIGN KEY(emp_name) REFERENCES employee(employeeid));"""
    # payroll = """CREATE TABLE payroll(payrollid INTEGER AUTOINCREMENT, date TEXT, payment REAL,  emp_name TEXT,FOREIGN KEY(emp_name) REFERENCES employee(employeeid));"""
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create table
        create_table(conn, employee)
        # create_table(conn, attendance)
        # create_table(conn, payroll)


    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
