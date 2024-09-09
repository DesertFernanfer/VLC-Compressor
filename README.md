# VLC-Compressor
A python script that compress videos of a directory (.mp4) , rename and delete duplicate videos heavier

### Requirements
- VLC Media Player: Install VLC from the oficial page [here](https://www.videolan.org/vlc/download-windows.html) (avoid using the Microsoft Store version).
- Windows 10 or 11.
- Python: Make sure Python is installed on your computer (lastest versions are recommended).
- Permissions: Ensure the script has the necessary permissions to execute.

### Usage
 - Install the script
 - Update the script with to your vlc.exe path
 - Run the script using the following command:

```python VideoCompressor.py```

The script will ask you:
 + The path of you .mp4 videos (.mp4).
 +  A basename for your video

⚠️ The script will ignore other types of files and does not perform recursive directory searches.
#### Explanation
1.- The script will open VLC for each video and close it after procesing. (We recommend to execute in other Windows desktop to avoid interferences).

2.- There will be the originals videos and converted (-converted), will delete the heavior files.

3.- Videos will be renamed with the provided basename (basename1, basename2 ...).
