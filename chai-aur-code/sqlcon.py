import mysql.connector
def main():
 try:
    conn = mysql.connector.connect(host="localhost", user="root",password="sagares123",  database="python")
    cursor=conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS student(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
                
                
            )
        """)
    while True:
       name = input("Enter name ")
       
       try:
                sql = "INSERT INTO student (name) VALUES (%s)"
                val = [name]
                cursor.execute(sql, val)
                conn.commit()
                print("User inserted successfully.")
       except mysql.connector.Error as e:
                print("Error inserting user:", e)
    cursor.close()
  
    conn.close()
    print("MySQL connection closed.")

 except mysql.connector.Error as e:
      print("Error connecting to MySQL database:", e)
if __name__=="__main__":
  main()
# import mysql.connector

# def main():
#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="sagares123",
#             database="python"
#         )
#         print("Connected to MySQL database!")

#         cursor = conn.cursor()

#         # Create table if not exists
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS users (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 name VARCHAR(255) NOT NULL,
#                 email VARCHAR(255) NOT NULL
#             )
#         """)
#         print("Table 'users' created successfully.")

#         while True:
#             name = input("Enter name (or type 'exit' to quit): ")
#             if name.lower() == "exit":
#                 break
#             email = input("Enter email: ")

#             try:
#                 sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
#                 val = (name, email)
#                 cursor.execute(sql, val)
#                 conn.commit()
#                 print("User inserted successfully.")
#             except mysql.connector.Error as e:
#                 print("Error inserting user:", e)

#         cursor.close()
#         conn.close()
#         print("MySQL connection closed.")

#     except mysql.connector.Error as e:
#         print("Error connecting to MySQL database:", e)
        
# if __name__ == "__main__":
#     main()
