import MovieUtil.Interfaces.IMovieCache as IMovieCache
import MovieUtil.Interfaces.IMovieData as IMovieData 

class tmdbCache:
    def __init__(self, movie_data: IMovieData):
        self.movie_data = movie_data
        self.cache = {}

    def get_movie_dict(self, movie_name: str):
        if movie_name+'+movie_dict' not in self.cache:
            self.cache[movie_name+'+movie_dict'] = self.movie_data.get_movie_dict(movie_name)
        return self.cache[movie_name+'+movie_dict']

    def get_movie_info(self, movie_id: int):
        if str(movie_id)+'+movie_info' not in self.cache:
            self.cache[str(movie_id)+'+movie_info'] = self.movie_data.get_movie_info(movie_id)
        return self.cache[str(movie_id)+'+movie_info']
         