from MovieUtil.imports import * 

class kqmu:
    def __init__(self):
        self.pp = pprint.PrettyPrinter(depth=6)
        data = tmdbData.tmdbData(tmdb, 'c36c3e845c8f5d1614362572d6778551')
        cache = tmdbCache.tmdbCache(data)
        self.logic = tmdbLogic.tmdbLogic(cache)
    def get_movie_object(self, movieName:str):
        return self.logic.get_movie_object(movieName)


if __name__== "__main__":
    mov = kqmu().get_movie_object('the bourne')
    pprint.pprint(mov.__dict__)

#json.dumps(mov.__dict__)

#print(mov.title + ' has an IMDB id of: ' + mov.tmdb_id)