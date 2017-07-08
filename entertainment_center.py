#importing the neccessary packages and main file
import media
import fresh_tomatoes

#instance 1
inception = media.Movie("Inception",
						"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
						"https://www.youtube.com/watch?v=YoHD9XEInc0",
						148,
						"Christopher Nolan")

#instance 2
interstellar = media.Movie("Interstellar",
						"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
						"https://www.youtube.com/watch?v=zSWdZVtXT7E",
						169,
						"Christopher Nolan")

#instance 3
drk_knight = media.Movie("Batman: The Dark Knight",
						"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
						"https://www.youtube.com/watch?v=EXeTwQWrcwY",
						152,
						"Christopher Nolan")

#instance 4
shw_rdmp = media.Movie("The Shawshank Redemption",
						"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
						"https://www.youtube.com/watch?v=NmzuHjWmXOc",
						142,
						"Frank Darabont")

#instance 5
the_intern = media.Movie("The Intern",
						"https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
						"https://www.youtube.com/watch?v=ZU3Xban0Y6A",
						121,
						"Nancy Meyers")

#instance 6
pulpfiction = media.Movie("Pulp fiction",
						"https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
						"https://www.youtube.com/watch?v=s7EdQ4FqbhY",
						178,
						"Quentin Tarantino")

#Defining list of movies which woiuld be passed to open movies page
movies = [ inception, interstellar, drk_knight, shw_rdmp, the_intern, pulpfiction ]

#Calling the fresh tomato function open movies with the list of movies as an argument
fresh_tomatoes.open_movies_page(movies)

