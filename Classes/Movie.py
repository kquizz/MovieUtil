class movie:
    def __init__(self
                , title: str 
                ,budget: int
                ,revenue: int
                ,runtime: int
                ,tmdb_id: int
                ,imdb_id: int
                ,release_date: str
                ,poster_path: str):
        self.title = title
        self.budget = budget
        self.revenue = revenue
        self.runtime = runtime
        self.tmdb_id = tmdb_id
        self.imdb_id = imdb_id
        self.release_date = release_date
        self.poster_path = poster_path