import os
from pytube import YouTube
from pytube.exceptions import VideoUnavailable, VideoPrivate
from config.config import WINDOWS_VIDEO_END_PATH
from termcolor import colored

def windows_download_video(use_youtube_links_file = False, only_audio = False):
    create_output_folder()

    if not use_youtube_links_file: manual_download_video(only_audio)
    else: auto_download_video(only_audio)   

def auto_download_video(only_audio = False):
    with open("config/youtube_links.txt", "r", encoding='utf-8') as links_file:
        for video_link in links_file:
            # Buscando o vídeo
            youtube_video = search_video(video_link)

            try:
                youtube_video_stream = choose_resolution(youtube_video)
                print(f"Baixando video com a resolução {youtube_video_stream.resolution} - ({round(youtube_video_stream.filesize_mb)} Mbs)...")

                # Baixar o vídeo no caminho de destino
                youtube_video_stream.download(output_path=WINDOWS_VIDEO_END_PATH)

                print(colored("Download successful!", "green"))
                print(colored("Next link...\n", "light_blue"))

            except Exception as e:
                print(colored(str(e), "yellow"))
                continue

        print(colored("Finished.", "green"))

def manual_download_video(only_audio = False):
    # Pegar o link do vídeo
    video_link = input("Digite o link do vídeo do YouTube: ")

    # Buscando o vídeo
    youtube_video = search_video(video_link)

    youtube_video_stream = choose_resolution(youtube_video)

    print(f"Baixando video com a resolução {youtube_video_stream.resolution} - ({round(youtube_video_stream.filesize_mb)} Mbs)...")

    # Baixar o vídeo no caminho de destino
    youtube_video_stream.download(output_path=WINDOWS_VIDEO_END_PATH)

def create_output_folder():
    print(colored("Creating output folder...", "light_blue"))
    # Criar pasta destino para os vídeos caso ela não exista
    os.makedirs(WINDOWS_VIDEO_END_PATH, exist_ok=True)
    print(colored("Output folder created successfully!", "green"))

def search_video(VIDEO_LINK):
    # Buscar o vídeo
    print(colored("Searching for the video...", "light_blue"))
    try:
        youtube_video_found = YouTube(VIDEO_LINK)

        if youtube_video_found:
            print(colored("Video found!", "green"))
            return youtube_video_found

    except (VideoUnavailable, VideoPrivate) as e:
        print(colored(f"ERRO: Vídeo indisponível: {e.error_string}", "red"))
        exit(1)

def choose_resolution(YOUTUBE_VIDEO):
    print(colored("Choosing the best resolution...", "light_blue"))

    # Pegar a melhor resolução do vídeo
    youtube_video_stream = YOUTUBE_VIDEO.streams.get_highest_resolution()

    print(colored(f"Best resolution found was {youtube_video_stream.resolution}", "yellow"))

    return youtube_video_stream

def auto_download_audio_only():
    with open("config/youtube_links.txt", "r", encoding='utf-8') as links_file:
        for video_link in links_file:
            # Buscando o vídeo
            youtube_video = YouTube(video_link)

            try:
                youtube_video_stream = youtube_video.streams.get_audio_only()
                print(f"Baixando áudio com a resolução {youtube_video_stream.abr}...")

                # Baixar o áudio no caminho de destino
                audio_file = youtube_video_stream.download(output_path=WINDOWS_VIDEO_END_PATH)

                # Renomear para formato MP3
                base, _ = os.path.splitext(audio_file)
                new_file = base + '.mp3'
                os.rename(audio_file, new_file)

                print(colored("Download successful!", "green"))
                print(colored("Next link...\n", "light_blue"))

            except Exception as e:
                print(colored(str(e), "yellow"))
                continue

        print(colored("Finished.", "green"))
