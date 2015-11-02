import webbrowser

class Video:
	def __init__(self, title, duration):
		self.title = title
		self.duration = duration

class Movie(Video):
	""" Test Doc """

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_duration):
		Video.__init__(self, movie_title, movie_duration)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
	def __init__(self, show_title, season, episode, tv_station, show_duration):
		Video.__init__(self, show_title, show_duration)
		self.season = season
		self.episode = episode
		self.station = tv_station

	def get_local_list(self):
		print "yo"
