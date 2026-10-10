n = input("""pdf
jpg
png
mp3
mp4
Enter extension:"""))
match n:
    case "pdf":
        print("Document")
    case "jpg":
        print("Image")
    case "png":
        print("Image")
    case "mp3":
        print("Audio")
    case "mp4":
        print("Video")
    case _:
        print("Unknown File Type")
