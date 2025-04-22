from AiShotServer.models import Movie


movie1 = Movie.objects.create(
    title="Movie Title 1",
    author="daixf",
    overview="This is an overview of movie 1.",
    release_date="2024-09-01",
    poster_path="/path/to/poster1.jpg",
    adult=False,
    original_language="en",
    original_title="Original Movie Title 1",
    genre_ids=[12, 14],
    backdrop_path="/path/to/backdrop1.jpg",
    popularity=87.5,
    vote_count=2500,
    video=False,
    vote_average=8.7
)

movie2 = Movie.objects.create(
    title="Movie Title 2",
    author="daixf",
    overview="This is an overview of movie 2.",
    release_date="2024-10-01",
    poster_path="/path/to/poster2.jpg",
    adult=False,
    original_language="en",
    original_title="Original Movie Title 2",
    genre_ids=[12, 16],
    backdrop_path="/path/to/backdrop2.jpg",
    popularity=75.4,
    vote_count=1897,
    video=False,
    vote_average=7.8
)
