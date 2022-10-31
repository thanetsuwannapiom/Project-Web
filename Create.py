import psycopg2
try:
    connection = psycopg2.connect(user="webadmin",
                                    password= "VCNtps41396",
                                    host="node37019-thanet.proen.app.ruk-com.cloud",
                                    port="11235",
                                    database="postgres")
    
    connection.autocommit = True


    cursor = connection.cursor()

    sql = '''CREATE database project'''


    cursor.execute(sql)
    print("Datadase created successfully.........")


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")