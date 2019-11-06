import MovieUtil.Interfaces.IMovieData as IMovieData
import MovieUtil.Interfaces.IMovieDataModule as IMovieDataModule

class tmdbData(IMovieData.IMovieData):
    def __init__(self, data_module: IMovieDataModule, key):
        self.data_module = data_module
        self.data_module.API_KEY = key

    def get_movie_dict(self, movie_name: str):
        return self.data_module.Search().movie(query=movie_name)

    def get_movie_info(self, movie_id: int):
        return self.data_module.Movies(movie_id).info()