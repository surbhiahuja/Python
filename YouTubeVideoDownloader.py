from pytube import YouTube
link = "https://www.youtube.com/watch?v=ZaKzw9tULeM&list=PLjVLYmrlmjGfgBKkIFBkMNGG7qyRfo00W" 
youtube_1 = YouTube(link)

print(youtube_1.title)
print(youtube_1.thumbnail_url)

videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("Enter Streaming number: "))
videos[strm].download()
print('Successfully')

