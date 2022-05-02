
import psycopg2
from config import config
from data import ui
import re


def get_columns(table, cursor):
    cur1 = cursor
    columns = []
    query = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}'";
    cur1.execute(query)
    columns.append(cur1.fetchall())
    return columns

def get_column_name(col):
    i = 0
    while(col[0][i][0] != 'email'):
        i+=1
    return col[0][i][0]

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
       
        
	    # execute a statement
        print("Connection established :)")


        # Getting column name => email
        col = get_columns('wingspan_user', cur)
        col_name = get_column_name(col)

        #checking the value in column - email
        
        qu = f"select {col_name} from wingspan_user"
        cur.execute(qu)
        email_list = cur.fetchall()
        if len(email_list) == 0:
            # Insert whole row
            st = ''
        else:
            check = 0
            for i in ui:
                for j in i:
                    existing_email = re.findall(".*@.*", j)
                    if(len(existing_email) != 0):
                        for email_ in email_list:
                            if(email_[0] == existing_email):
                                # update
                                check = 1
                        if(check == 0):
                            # insert whole row
                            st = ''





        





	    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
