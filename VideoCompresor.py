import os
import subprocess

def compress_videos(input_folder):
    videos = [f for f in os.listdir(input_folder) if f.endswith(('.mp4')) and  (f != "Nuevo" or f != "nuevo")]
    
    print("Compressing videos using VLC...")

    for video in videos:
        output_path = os.path.join(input_folder, f"coverted-{video}")
    vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"  # Ruta correcta a vlc.exe en tu sistema

    
    for video_file in videos:
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(input_folder, f"converted-{video_file}")

        vlc_cmd = [vlc_path, 
                   input_path, 
                   '--sout', 
                   f'#transcode{{vcodec=h264,acodec=mpga}}:std{{access=file,mux=ts,dst="{output_path}"}}', 
                   '--play-and-exit',
                   "--no-video"]
 
        vlc_process = subprocess.Popen(vlc_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        vlc_process.wait()  
        
    print("Compression completed.")

def rename_and_delete(input_folder, base_name):
    video_files = [f for f in os.listdir(input_folder) if f.endswith('.mp4')]
    print(video_files)

    for video in video_files:
        converted_video = "converted-" + video
        path_video = os.path.join(input_folder, video)
        path_converted_video = os.path.join(input_folder, converted_video)

        if os.path.exists(path_converted_video):
            if os.path.getsize(path_video) > os.path.getsize(path_converted_video):
                os.remove(path_video)
            elif os.path.getsize(path_video) < os.path.getsize(path_converted_video):
                os.remove(path_converted_video)
            elif os.path.getsize(path_video) == os.path.getsize(path_converted_video):
                print("Son del mismo tamaño")
                os.remove(path_converted_video)

    videos1 = [f for f in os.listdir(input_folder) if f.endswith(('.mp4')) and (f != "Nuevo" or f != "nuevo")]
    print(videos1)
    n = 0
    for video in videos1:
        old_path = os.path.join(input_folder, video)
        n +=1
        
        n1 = str(n)
        new_path = os.path.join(input_folder, base_name + n1 + '.mp4')
        os.rename(old_path, new_path)
        n1 = int(n1)

if __name__ == "__main__":
    input_folder = input("Introduce un directario: ")
    base_name = input("Introduce el nombre base: ")
    
    if os.path.exists(input_folder):
        compress_videos(input_folder)
        rename_and_delete(input_folder, base_name)
        print("Process completed.")
    else:
        print("Invalid folder path.")