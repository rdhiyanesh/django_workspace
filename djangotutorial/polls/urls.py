from django.urls import path
from  . import views

app_name = "polls"
urlpatterns=[
        # eg: polls/
        path("", views.IndexView.as_view(), name="index"),
        #eg: polls/5/
        path("<int:pk>/", views.DetailView.as_view(), name="details"),
        #eg: polls/5/results/
        path("<int:pk>/results/", views.resultsView.as_view(), name="results"),
        #eg: polls/5/results/votes
        path("<int:question_id>/vote/", views.votes, name="votes"),
]