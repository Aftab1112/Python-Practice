from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://<username>:<password>@cluster0.cik9i7j.mongodb.net/", tlsAllowInvalidCertificates = True)
db = client["ytmanager"]
video_collection = db["videos"]

def list_all_videos():
    print("*" * 70)
    videos = video_collection.find()
    
    if video_collection.count_documents({}) == 0 :
        print("No videos yet...")
    else :
        for video in videos :    
            print(f"ID : {video["_id"]}, Name : {video["name"]}, Time : {video["time"]}")
    print("*" * 70)

def add_new_video(name, time):
    video_collection.insert_one({"name": name, "time": time})
    print("Video added successfully !")

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id" : ObjectId(video_id)},
        {"$set" : {"name" : new_name, "time" : new_time}}
    )
    print("Video updated successfully !")

def delete_video(video_id):
    video_collection.delete_one({"_id" : ObjectId(video_id)})
    print("Video deleted successfully !")

def main():
    while True:
        print("\n")
        print("Youtube Manager App | MongoDB Version")
        print("\n")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        print("\n")
        choice = input("Enter a choice : ")

        if choice == "1":
            list_all_videos()
        elif choice == "2":
            name = input("Enter the video name : ")
            time = input("Enter the video time : ")
            add_new_video(name, time)
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

if __name__ == "__main__":
    main()
