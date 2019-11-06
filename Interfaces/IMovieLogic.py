import MovieUtil.Interfaces.IMovieCache as IMovieCache

class IMovieLogic:
    def __init__(self, movie_cache: IMovieCache):
        pass
    
    def get_movie_id(self, movie_name: str):
        pass

    def get_movie_object(self, movie_name: str):
        pass