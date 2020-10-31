import unittest


class Movie(object):
    def __init__(self):
        self.copies = 0

    def add_copy(self):
        self.copies += 1


class Library(object):
    def __init__(self):
        self._catalogue = []

    def donate(self, movie):
        self._catalogue.append(movie)
        movie.add_copy()

    def contains(self, movie):
        return movie in self._catalogue


class LibraryTest(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.movie = Movie()
        self.library.donate(self.movie)

    def test_donated_movie_added_to_catalogue(self):
        self.assertTrue(self.library.contains(self.movie))

    def test_rental_copy_added_to_donated_movie(self):
        self.assertEqual(self.movie.copies, 1)


if __name__ == '__main__':
    unittest.main()
