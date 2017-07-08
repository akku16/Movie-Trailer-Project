import webbrowser

class Movie():
	"""THis class contains all the neccessary fileds that would be present across all the different instances that would be created """
	def __init__(self, title, poster_link, trailer_link, duration, director):
		#Defining instance variables
		self.title = title
		self.poster_image_url = poster_link
		self.trailer_youtube_url = trailer_link
		self.duration = duration
		self.director = director


	def show_trailer(self):
		webbrowser.open(self.trailer_link)
