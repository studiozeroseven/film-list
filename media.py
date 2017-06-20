import webbrowser


class Movie:
    """This class is the blueprint for each film I will display"""

    def __init__(self, movie_title, movie_storyline, poster_image_url,
                 trailer_youtube_url, rating):
        self.title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = rating  # Added this in, not in original scope

    def show_trailer(self):  # This function opens trailer to play
        webbrowser.open(self.trailer_youtube_url)
