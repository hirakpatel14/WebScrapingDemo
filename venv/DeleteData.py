import db_connection as dbConn;


class Delete:
    def func_DeleteData(self):
        # Get the SQL connection
        connection = dbConn.getConnection()

        id = input('Enter Employee Id = ')

        try:
            # Get record which needs to be deleted
            sql = "Select * From tblEmployee Where Id = ?"
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Gender\t\t EmailID')
            print('-------------------------------------------')
            print(' {}\t\t {} \t\t\t{}\t\t{} '.format(item[0], item[1], item[2], item[3]))
            print('-------------------------------------------')
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if  confirm in ('y','Y'):
                deleteQuery = "Delete From tblEmployee Where Id = ?"
                cursor.execute(deleteQuery, [id])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()