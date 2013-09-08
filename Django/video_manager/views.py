import logging
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from video_manager.models import Rating
from video_manager.models import Video

def vote(request):
    if request.method == 'POST' and request.user.is_authenticated():
        # TODO(dcastro): Use get instead of filter throughout this page.
        videos = Video.objects.filter(filename=request.POST['video'])
        # Makes sure the video exists and there is only one with that filename.
        try:
            video = videos[0]
        except IndexError:
            logging.error("Video: " + request.POST['video'] + " not found.")
            return HttpResponse("Video was not found.")

        rating = int(request.POST['vote'])
        if (rating < 1 or rating > 5):
            logging.error("Rating input out of bounds.")
            return HttpResponse("Rating invalid.")

        # Check if object has previously been rated.
        existing_rating = Rating.objects.filter(user=request.user,
                                                video=video)
        if (len(existing_rating) == 1):
            existing_rating[0].rating = rating
            existing_rating[0].save()
        else:
            new_rating = Rating(user=request.user, video=video, rating=rating)
            new_rating.save()
        return HttpResponse("Success.")

def index(request):
    rated_list = []
    rated_videos = []
    
    if request.user.is_authenticated():
        user = request.user

        # Format ratings to pre-set already rated videos.
        ratings_query = Rating.objects.filter(user=request.user)
        for rating in ratings_query:
            rated_videos.append(rating.video.filename)
            user_rating = {"video":rating.video.filename,"rating":rating.rating}
            rated_list.append(user_rating)
    else:
        user = None

    videos = Video.objects.all()
    data = {"user":user,
            "videos":videos,
            "rated_videos": rated_videos,
            "ratings":rated_list}

    data.update(csrf(request))
    return render_to_response("index.html", data,
                              context_instance=RequestContext(request))