import webbrowser

#this is the blueprint for Movie.  From here we create the template for storyline, title, trailer, and poser

class Movie():

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""this is the constructor method.  This is where we instantiate all of the 
		variables, in order to create an instance of movie."""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube



	def show_trailer(self):
		"""Show trailer is a function opens the webbrowser, and it runs the youtube trailer url
		through it"""
		webbrowser.open(self.trailer_youtube_url)