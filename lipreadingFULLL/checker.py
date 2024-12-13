import os

# SCRIPT FOR CHECKING DOWNLOAD OF VIDEOS AND ALIGNMENTS 
# I USED THIS SCRIPT TO FIND swiz9n.align , A FILE THAT WAS MISSING A CORRESPONDING VIDEO FILE
folder_path = "./merge"


video_extensions = {".mpg"} 
subtitle_extensions = {".align"} 

# Separate files into videos and subtitles based on extensions
video_files = set()
subtitle_files = set()

for file in os.listdir(folder_path):
    name, ext = os.path.splitext(file)
    if ext.lower() in video_extensions:
        video_files.add(name)
    elif ext.lower() in subtitle_extensions:
        subtitle_files.add(name)

# Find subtitles without corresponding videos
missing_videos = subtitle_files - video_files

# Output results
print("Subtitles without corresponding videos:")
for missing in missing_videos:
    print(f"{missing}")