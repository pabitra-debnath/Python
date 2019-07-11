import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="7788",
                                  host="127.0.0.1",
                                  database="testdbb")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    #print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    #cursor.execute("SELECT version();")
    #record = cursor.fetchone()
    #print("You are connected to - ", record,"\n")

    '''sql_select_query = """select * from role"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    print(record)
    '''
    postgres_insert_query = """ INSERT INTO role (id, role, orderr, version, "createdBy", "createdOn", "updatedBy", "updatedOn") VALUES (1, 'super-user', 'fgh', 'rj', 'jcob', null, 'KK', null)"""
    #record_to_insert = (1, 'super-user', 'fgh', 'rj', 'jcob', null, 'KK', null)
    cursor.execute(postgres_insert_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
