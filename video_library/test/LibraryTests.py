import unittest
from unittest.mock import MagicMock


class Movie(object):
    def __init__(self, title, mail):
        self.mail = mail
        self.title = title


class Library(object):
    def __init__(self, imdb):
        self.imdb = imdb
        self.catalogue = []

    def donate(self, imdbId):
        movie = Movie(self.imdb.get_movie_info(imdbId))
        self.catalogue.append(movie)
        self.mail.send("New Movie", movie.title, "All Members")



class StubImdb(object):
    def __init__(self, title):
        self.title = title

    def get_movie_info(self, imdbID):
        return self.title


class Mail(object):
    def send(self, subject, movieTitle, distributionList):
        pass


class DonateMovieTests(unittest.TestCase):
    def test_donated_movie_added_to_catalogue(self):
        self.assertTrue(len(list(filter(lambda movie: movie.title == "ET", self.library.catalogue))) == 1)

    def test_members_emailed_about_new_movie(self):
        self.mockMail.send.assert_called_with("New Movie", "ET", "All Members")

    def setUp(self):
        imdb = StubImdb("ET")
        self.mockMail = Mail()
        self.mockMail.send = MagicMock()
        self.library = Library(imdb, self.mockMail)
        self.library.donate("tt123456")


if __name__ == '__main__':
    unittest.main()
