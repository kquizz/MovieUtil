from unittest import TestCase, mock
import unittest

import Classes.tmdbData as tmdbData


class test_tmdbData(TestCase):

    def test_get_movie_dict(self):
        mock_movie_data_module = unittest.mock.MagicMock()

        mock_movie_data_module.Search.return_value.movie.return_value = 'Test2'

        tmdb = tmdbData.tmdbData(mock_movie_data_module, '')

        self.assertEqual(tmdb.get_movie_dict(''), 'Test2')

if __name__ == "__main__":
    unittest.main()



       # mock_complex.movie.return_value = 'Test2'
        #b = ComplexClass.ComplexClass(mock_complex)
        #self.assertEqual(b.Search().movie(query=''), 'Test2')