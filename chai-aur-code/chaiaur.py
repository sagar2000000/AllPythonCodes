import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="sagares123", database="hello")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS video (
               id INT AUTO_INCREMENT PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM video")
    videos = cursor.fetchall()
    if not videos:
        print("No videos found.")
    else:
        for video in videos:
            print(video)

def add_video(name, time):
    sql = "INSERT INTO video (name, time) VALUES (%s, %s)"
    val = (name, time)
    cursor.execute(sql, val)
    conn.commit()
    print("Successfully inserted")

def update_video(video_id, new_name, new_time):
    sql = "UPDATE video SET name = %s, time = %s WHERE id = %s"
    val = (new_name, new_time, video_id)
    cursor.execute(sql, val)
    conn.commit()
    print("Successfully updated")

def delete_video(video_id):
    sql = "DELETE FROM video WHERE id = %s"
    val = (video_id,)
    cursor.execute(sql, val)
    conn.commit()
    print("Successfully deleted")

def main():
    try:
        while True:
            print("\nYouTube manager app with DB")
            print("1. List Videos")
            print("2. Add Videos")
            print("3. Update Videos")
            print("4. Delete Videos")
            print("5. Exit app")
            choice = input("Enter your choice: ")

            if choice == '1':
                list_videos()
            elif choice == '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            elif choice == '3':
                video_id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id, name, time)
            elif choice == '4':
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            elif choice == '5':
                break
            else:
                print("Invalid Choice")

        conn.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
