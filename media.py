class Movie():

    """This class saves movie information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """Assigns input arguments to repective movie details"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
