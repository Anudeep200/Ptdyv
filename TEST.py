from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube 

link = "https://www.youtube.com/watch?v=221F55VPp2M"

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "D:\kk", 
filename = "Joey's Bad Birthday Gift.mp4")
except:
    print("Some Error!")
print('Task Completed!')    
#print(yt.captions)
caption = yt.captions.get_by_language_code('en')  
print(caption.xml_captions )
f= open("Sub.txt", "a",encoding='utf-8')
a= caption.xml_captions
f.write(a)

print("done")
f.close

