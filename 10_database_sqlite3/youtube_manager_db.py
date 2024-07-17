import sqlite3

con = sqlite3.connect("youtube_videos.db")
cursor = con.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
"""
)


def list_all_videos():
    print("*" * 70)
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()

    if not rows:
        print("No videos yet")
    else:
        for row in rows:
            print(row)
    print("*" * 70)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)", (name, time))
    con.commit()
    print("Video added successfully !")


def update_video(video_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ?, WHERE id = ?",
        (new_name, new_time, video_id),
    )
    con.commit()
    print("Video updated successfully !")


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    con.commit()
    print("Video deleted successfully !")


def main():
    while True:
        print("\n")
        print("Youtube Manager App | SQLite3 Version")
        print("\n")
        print("1. List all videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        print("\n")
        choice = input("Enter your choice : ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter the video ID to update : ")
            new_name = input("Enter new video name : ")
            new_time = input("Enter new video time : ")
            update_video(video_id, new_name, new_time)
        elif choice == "4":
            video_id = input("Enter the video ID to delete : ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice, try again...")

    con.close()


if __name__ == "__main__":
    main()
