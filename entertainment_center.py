import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life",
						"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A story about a bunch of tall funny dudes in a forest", 
					"http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
					"https://www.youtube.com/watch?v=d1_JBMrrYw8")

skyfall = media.Movie("Skyfall", "James Bond kicks some ass and drinks booze",
					"http://t2.gstatic.com/images?q=tbn:ANd9GcTSNSk0M1z_CZ1UKTnfE2nHmk4Oxqh_gKO0dAHZHwrfLX6D9Y4s",
					"https://www.youtube.com/watch?v=6kw1UVovByw")

girl_with_dragon = media.Movie("Girl with the dragon tattoo", "James Bond and Rooney Mara research a murder",
								"http://t0.gstatic.com/images?q=tbn:ANd9GcT3C9lPaq1RPyrr12irhuZewsNZUX1aXxvU0Llyoc7n3zDqN1Rj",
								"https://www.youtube.com/watch?v=DqQe3OrsMKI")

silence_lambs = media.Movie("The Silence of the Lambs", "Hannibal lectar helps solve a murder",
							"http://t3.gstatic.com/images?q=tbn:ANd9GcRCZLkDY7eSQu1ndh7m9JQkvzXVvW9VrBzT_anh5Lf4kT84-4ev",
							"https://www.youtube.com/watch?v=W6Mm8Sbe__o")
good_fellas = media.Movie("GoodFellas", "Mobsters commit crimes",
						"https://upload.wikimedia.org/wikipedia/en/7/7b/Goodfellas.jpg",
						"https://www.youtube.com/watch?v=qo5jJpHtI1Y")
#print(avatar.storyline)
#girl_with_dragon.show_trailer()
movies = [toy_story, avatar, skyfall, girl_with_dragon, silence_lambs, good_fellas]

fresh_tomatoes.open_movies_page(movies)