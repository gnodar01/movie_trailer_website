import webbrowser


class Movie():
    '''The Movie class takes in movie title, movie storyline,
    a link for poster image, youtube trailer link and movie
    duration. There is a show_trailer instance method, which
    will open the youtube link in a browswer when called.'''

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, movie_duration):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = movie_duration

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
