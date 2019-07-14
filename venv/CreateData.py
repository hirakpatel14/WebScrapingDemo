import db_connection as dbConn


class Create:
    def func_CreateData(self):

        # Get the sql connection
        connection = dbConn.getConnection()

        name = input('Enter Name = ')
        gender = input('Enter Gender = ')
        email = input('Enter Email= ')

        try:
            query = "Insert Into tblEmployee(Name, Gender, Email) Values(?,?,?)"
            cursor = connection.cursor()

            # Execute the sql query
            cursor.execute(query, [name, gender, email])

            # Commit the data
            connection.commit()
            print('Data Saved Successfully')

        except:
            print('Something wrong, please check')

        finally:
            # Close the connection
            connection.close()