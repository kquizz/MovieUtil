import MovieUtil.Interfaces.IMovieLogic as IMovieLogic
import MovieUtil.Interfaces.IMovieCache as IMovieCache
import MovieUtil.Classes.Movie as Movie


class tmdbLogic(IMovieLogic.IMovieLogic):
    def __init__(self, movie_cache: IMovieCache):
        self.movie_cache = movie_cache

    def get_movie_id(self, movie_name):
        return  self.movie_cache.get_movie_dict(movie_name)['results'][0]['id']

    def get_movie_dict(self, movie_name):
        return  self.movie_cache.get_movie_dict(movie_name)['results'][0]

    def get_movie_info(self, movie_id: int):
        return self.movie_cache.get_movie_info(movie_id)

    def get_movie_object(self, movie_name: str):
        movie_id = self.get_movie_id(movie_name)
        movie = self.get_movie_info(movie_id)
#        return movie
        mov = Movie.movie(title = movie['title']
                    ,budget = movie['budget']
                    ,revenue = movie['revenue']
             ,runtime = movie['runtime']
             ,tmdb_id = movie['id']
             ,imdb_id = movie['imdb_id']
             ,release_date = movie['release_date']
             ,poster_path = movie['poster_path'])
        return mov
