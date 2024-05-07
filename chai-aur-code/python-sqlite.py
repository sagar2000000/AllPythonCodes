import mysql.connector
try:
 conn = mysql.connector.connect(host="localhost", user="root",password="sagares123",  database="hi")
 cursor=conn.cursor()
 if conn.is_connected:
   print('connected sucessfully')
 
 cursor.execute("""
             CREATE TABLE IF NOT EXISTS vid(
                id INT PRIMARY KEY AUTO_INCREMENT,
                 name VARCHAR(255) NOT NULL,
                 time VARCHAR(255) NOT NULL
                 
                 
             )
         """)


 def list_videos():
   rows=cursor.execute("SELECT * FROM vid")
   for i in rows:
    print(i)
  
 def add_video(name,time):
   sql="INSERT INTO vid(name,time) VALUES(%s,%s)"
   val=(name,time)
   cursor.execute(sql,val)
   conn.commit()
except mysql.connector.Error as e:
                print("Error inserting user:", e)
def main():
 try:
   while True:
    print("1.List videos")
    print("2.Add videos")
    print("3.Update videos")
    print("4.Delete videos")
    print("5.exit ")
    choice=input("Enter a comchaimnad")
    match(choice):
      case "1":
        list_videos()
  
      case "2":
        name=input("Enter video name to add")
        time=input("length of video")
        add_video(name,time)
 except  mysql.connector.Error as e:
    print(e)
      
    #  case "3":
    #    video_id=int(input("enter video id to edit"))
    #    new_name=input("Enter video name to add")
    #    new_time=input("length of video")
    #    update_video(video_id,new_name,new_time)
 
    #  case "4":
    #    vid_id=int(input("enter video id to delete"))
    #    del_vid(vid_id)


  

if __name__=="__main__":
  main()

    
        
