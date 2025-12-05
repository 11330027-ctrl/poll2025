from django.urls import path
from .views import poll_list, PollList, PollView, pollvote

urlpatterns = [
    path("", poll_list),
    path("list", PollList.as_view(), name='poll_list'),
    path("<int:pk>/", PollView.as_view(), name='poll_view'),
    path('<int:pk>/vote/', pollvote.as_view(), name='poll_vote'),
]
