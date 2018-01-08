import media
import fresh_tomatoes


"""This page lists the movies with their information
and opens the fresh_tomatoes.py page to create the website"""
# These are the lists of what is to be included with the movie
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print(toy_story.storyline)

avatar = media.Movie(
    "Avatar", "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "http://www.youtube.com/watch?v=-9ceBgWV8io")
# print(avatar.storyline)
# avatar.show_trailer()

star_wars = media.Movie(
  "Star Wars: The Last Jedi",
  "'Rey developes her newly discovered abilities', \
  'with the guidance of Luke Skywalker'",
  "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
  "https://www.youtube.com/watch?v=Q0CbN8sfihY")
# star_wars.show_trailer()

school_of_rock = media.Movie(
    "School Of Rock",
    "Down and out rock star becomes a music teacher",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

movies = [toy_story, avatar, star_wars, school_of_rock]

fresh_tomatoes.open_movies_page(movies)

# print(media.Movie.valid_ratings)
# print(media.Movie.__doc__)
# running this page activates the movie trailer website with the-
# supporting files
