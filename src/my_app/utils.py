import yt_dlp

def get_title_and_description(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = info.get('title', 'No title found')
        description = info.get('description', 'No description found')
        return title, description
