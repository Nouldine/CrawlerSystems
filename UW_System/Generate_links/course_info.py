
import mysql.connector 
from mysql.connector import Error


main_link = 'https://www.wisconsin.edu/transfer/wizards/?tis=edu.uwsa.tis.Wizards.JSP%252FdepartmentList.do%253Bjsessionid%253D1F66711060E286D89B93ED5E4F168BF8&reqType=C&reqType=C&tispage=1&fromInstitutionId=4690&toInstitutionId={}&submit=Next+Step' 

def connection():
     
     try: 
         mySQLconnection = mysql.connector.connect(host = 'localhost', database ='db', user ='user',  password ='password')

         sql_select_Query = "select * from campuses_info"
         
         campuse_info = mySQLconnection.cursor()
         campuse_info.execute(sql_select_Query)

         records = campuse_info.fetchall()

         print(" Number of rows: ", campuse_info.rowcount )
         print("Printing each row")

         info = []
          
         for row in records:

             #info.append(row)

             gen_links =  main_link.format(row[ 1 ])

             print  gen_links

             #print("instution Name:", row[ 0 ] )
             #print("Id:", row[ 1 ] )

         campuse_info.close

     except Error as e:
        
        print("Error while connection to Mysql",  e )

     finally:

        # Closing database connection.
        if(mySQLconnection.is_connected() ): 

            mySQLconnection.close()
            print("MySQL connection is closed")


connection()
