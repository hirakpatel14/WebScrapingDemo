import db_connection as dbConn;


class Update:
    def func_UpdateData(self):
        # Get the SQL connection
        connection = dbConn.getConnection()

        id = input('Enter Employee Id = ')

        try:
            # Fetch the data which needs to be updated
            sql = "Select * From tblEmployee Where Id = ?"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print(item)
            print('ID\t\t Name\t\t\t Gender\t\t EmailID')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{}\t\t{} '.format(item[0], item[1], item[2], item[3]))
            print('-------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = input('Enter New Name = ')
            gender = input('Enter New Gender = ')
            email = input('Enter New EmailID = ')
            query = "Update tblEmployee Set Name = ?, Gender = ?, Email = ? Where Id =?"

            # Execute the update query
            cursor.execute(query, [name, gender, email, id])
            connection.commit()
            print('Data Updated Successfully')

        except:
            print('Something wrong, please check')

        finally:
            # Close the connection
            connection.close()