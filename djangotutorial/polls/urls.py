from django.urls import path
from  . import views

app_name = "polls"
urlpatterns=[
        # eg: polls/
        path("", views.index, name="index"),
        #eg: polls/5/
        path("<int:question_id>/", views.details, name="details"),
        #eg: polls/5/results/
        path("<int:question_id>/results/", views.results, name="results"),
        #eg: polls/5/results/votes
        path("<int:question_id>/vote/", views.votes, name="votes"),
]