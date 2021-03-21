from time import sleep 

def videodownload():
    from pytube import YouTube 
    import os 
    yt = YouTube( 
    str(input("Enter the URL of the video you want to download: \n>> "))) 
    video = yt.streams.filter(resolution='720p').first() 
    print("Enter the destination (leave blank for current directory)") 
    destination = str(input(">> ")) or '.'
    print(yt.title + " is currently downloading!: \nThis may take a minute")
    video.download(output_path=destination) 
    print(yt.title + " has been successfully downloaded.")

def songdownload():
    from pytube import YouTube 
    import os 
    yt = YouTube( 
    str(input("Enter the URL of the song you want to download: \n>> "))) 
    video = yt.streams.filter(only_audio=True).first() 
    print("Enter the destination (leave blank for current directory)") 
    destination = str(input(">> ")) or '.'
    out_file = video.download(output_path=destination) 
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 
    print(yt.title + " has been successfully downloaded.")


def run_main():
    list_choices = ['Video-download-DLG: 1',
                    'Song-Download: 2']
                    

    print('============================')
    for item in list_choices:
        print(item)
    print('============================')

    user_choice = input('Enter number of selection: ')

    if user_choice == '1':
        videodownload()
    elif user_choice =='2':
        songdownload()
        
    sleep(2)
    run_main()
run_main()

