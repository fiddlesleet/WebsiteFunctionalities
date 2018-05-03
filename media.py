import webbrowser

class Video():
    def __init__(self, title, synopsis, thumbnail_url, video_url):
        self.title = title
        self.synopsis = synopsis
        self.thumbnail_url = thumbnail_url
        self.video_url = video_url

    # in python, all instance methods take in variable self
    def play_video(self):
        webbrowser.open(self.video_url)
