# @GET("/3/discover/movie?language=en&sort_by=popularity.desc")

# @GET("/3/discover/tv?language=en&sort_by=popularity.desc")
# @Immutable
# DiscoverMovieResponse(
#   val page: Int,
#   val results: List<Movie>,
#   val total_results: Int,
#   val total_pages: Int
# ) 

# Movie(
#   var page: Int,
#   var keywords: List<Keyword>? = ArrayList(),
#   var videos: List<Video>? = ArrayList(),
#   var reviews: List<Review>? = ArrayList(),
#   val poster_path: String?,
#   val adult: Boolean,
#   val overview: String,
#   val release_date: String?,
#   val genre_ids: List<Int>,
#   val id: Long,
#   val original_title: String,
#   val original_language: String,
#   val title: String,
#   val backdrop_path: String?,
#   val popularity: Float,
#   val vote_count: Int,
#   val video: Boolean,
#   val vote_average: Float
# )
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from AiShotServer.models import Movie, Review, Video 
from django.db import models as dbm
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from AiShotServer.serializers import ReviewSerializer, VideoSerializer


@require_GET
def discover_movies(request):
    language = request.GET.get('language', 'en')
    sort_by = request.GET.get('sort_by', 'popularity.desc')

    # Query the database for movies
    movies = Movie.objects.filter(original_language=language)

    # Sort the movies if needed
    if sort_by == 'popularity.desc':
        movies = movies.order_by('-popularity')
        
    # Prepare the JSON response
    results = []
    for movie in movies:
       
        result = {
            "id": movie.id,
            "userId":movie.user.pk,
           # "user_avatar":movie['user_avatar'],
            "title": movie.title,
            "overview": movie.overview,
            "release_date": movie.release_date,
            "poster_path": movie.poster_path,
            "adult": movie.adult,
            "original_language": movie.original_language,
            "original_title": movie.original_title,
            "genre_ids": movie.genre_ids,
            "backdrop_path": movie.backdrop_path,
            "popularity": movie.popularity,
            "vote_count": movie.vote_count,
            "video": movie.video,
            "vote_average": movie.vote_average,
            "author":movie.author
        }
        if isinstance(movie.user.avatar, dbm.ImageField):
            print('build the user_avatar')
            result['user_avatar'] = request.build_absolute_uri(movie.user.avatar.url)
        else:
            result['user_avatar'] = request.build_absolute_uri('/media/avatars/default_avatar.jpg')  
        
        results.append(result)
    print(results)
    response_data = {
        "page": 1,
        "results": results,
        "total_results": movies.count(),
        "total_pages": 1  # For simplicity, assume all results fit on one page
    }
    return JsonResponse(response_data)


@api_view(['GET'])
def fetch_videos(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        print(movie.genre_ids)
        print( Video.objects.all())
        videos = Video.objects.filter(movie_id=movie_id)
        video_serializer = VideoSerializer(videos, many=True)

        # Structure the response to match the ShopListResponse
        response_data = {
            "id": movie_id,
            "results": video_serializer.data
        }

        return Response(response_data)

    except Video.DoesNotExist:
        return Response({"error": "Video not found"}, status=404)
    
    
@api_view(['GET'])
def fetch_reviews(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
        print(movie.genre_ids)
        print( Video.objects.all())
        reviews = Review.objects.filter(movie_id=movie_id)
        review_serializer = ReviewSerializer(reviews, many=True)

        # Structure the response to match the ShopListResponse
        response_data = {
            "id": movie_id,
            "results": review_serializer.data
        }
        print(f"{response_data}")
        return Response(response_data)

    except Video.DoesNotExist:
        return Response({"error": "review not found"}, status=404)