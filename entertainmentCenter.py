import media
import fresh_tomatoes


# Movie objects, instanciated from Movie class in media.py 
# Movie class takes in (Title, Description, Movie Poster/Image Link, YouTube Trailer Link, and Runtime)
munchausen = media.Movie(
    "The Adventures of Baron Munchausen",
    "An account of Baron Munchausen's supposed travels and \
    fantastical experiences with his band of misfits.",
    "https://upload.wikimedia.org/wikipedia/en/3/3d/Adventures_of_baron_munchausen.jpg", # noqa
    "https://www.youtube.com/watch?v=s2nt9yU1vEU",
    "2h 7m")

zero_theorem = media.Movie(
    "The Zero Theorem",
    "A reclusive computer genius working on a formula to \
    determine whether life holds any meaning.",
    "http://ia.media-imdb.com/images/M/MV5BMTc4NTIxMTE0OF5BMl5BanBnXkFtZTgwNTQ5NTYxMjE@._V1_SX640_SY720_.jpg", # noqa
    "https://www.youtube.com/watch?v=RyMSRRNHRos&feature=iv&src_vid=rae7_O_6EtU&annotation_id=annotation_1853691763", # noqa
    "1h 47m")

lost_children = media.Movie(
    "The City of Lost Children",
    "A scientist in a surrealist society kidnaps children to \
    steal their dreams, hoping that they slow his aging process.",
    "https://upload.wikimedia.org/wikipedia/en/4/40/City_of_lost_children_french_movie_poster.jpg",
    "https://www.youtube.com/watch?v=Pa7oVPru4J8",
    "1h 52m")

nightmare_before_christmas = media.Movie(
    "The Nightmare Before Christmas",
    "Jack Skellington, king of Halloween Town, discovers Christmas \
    Town, but doesn't quite understand the concept.",
    "https://upload.wikimedia.org/wikipedia/en/9/9a/The_nightmare_before_christmas_poster.jpg", # noqa
    "https://www.youtube.com/watch?v=wr6N_hZyBCk",
    "1h 16m")

big_fish = media.Movie(
    "Big Fish",
    "A son tries to learn more about his dying father by reliving \
    stories and myths he told about his life.",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Big-fish-movie-poster.jpg", # noqa
    "https://www.youtube.com/watch?v=M3YVTgTl-F0",
    "2h 5m")

dreams_may_come = media.Movie(
    "What Dreams May Come",
    "After dying in a car crash a man searches the afterlife for his wife.",
    "https://upload.wikimedia.org/wikipedia/en/9/91/Whatdreamsposter.jpeg",
    "https://www.youtube.com/watch?v=TPZpQsEFcKI",
    "1h 56m")

neverending_story = media.Movie(
    "The NeverEnding Story",
    "A troubled boy dives into a wonderous fantasy world through \
    the pages of a mysterious book.",
    "https://upload.wikimedia.org/wikipedia/en/9/9b/Neverendingstoryposter.jpg", # noqa
    "https://www.youtube.com/watch?v=UeFni9dOv7c",
    "1h 47m")

neverending_story_ii = media.Movie(
    "The NeverEnding Story II: The Next Chapter",
    "A young boy with a distant father enters a world of make-believe \
    and magic through a portal within an antique book.",
    "https://upload.wikimedia.org/wikipedia/en/8/87/Neverending_story_two_poster.jpg", # noqa
    "https://www.youtube.com/watch?v=Gg3pSz-P7IE",
    "1h 30m")

hook = media.Movie(
    "Hook",
    "What if Peter Pan grew up?",
    "http://ia.media-imdb.com/images/M/MV5BMTU2MzYzOTQyMF5BMl5BanBnXkFtZTcwNDM2NDU2MQ@@._V1_SX640_SY720_.jpg", # noqa
    "https://www.youtube.com/watch?v=48iCNTicD3o",
    "2h 24m")

# List of movies for the HTML generator
movies = [zero_theorem, hook, lost_children, big_fish, dreams_may_come,
 neverending_story, neverending_story_ii, nightmare_before_christmas, munchausen]

# Takes in list of movies, generates HTML, and opens in browser
fresh_tomatoes.open_movies_page(movies)
