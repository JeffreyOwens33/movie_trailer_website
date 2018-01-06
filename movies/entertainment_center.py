import media
import fresh_tomatoes

#these are the definitions of the movies
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
#avatar.show_trailer()

star_wars = media.Movie("Star Wars: The Last Jedi",
                        "Rey developes her newly discovered abilities with the guidance of Luke Skywalker",
                        "https://upload.wikimedia.org/wikipedia/commons/6/60/Star_Wars_Episode_VIII_The_Last_Jedi_Word_Logo_-_White_teaser_poster_variant.svg",
                        "https://www.youtube.com/watch?v=Q0CbN8sfihY")
#star_wars.show_trailer()

school_of_rock = media.Movie("School Of Rock", "Down and out rock star becomes a music teacher",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

movies = [toy_story, avatar, star_wars, school_of_rock]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.valid_ratings)
#print(media.Movie.__doc__)
#running this page activates the movie trailer website with the supporting files

