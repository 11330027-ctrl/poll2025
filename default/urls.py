from django.urls import path
from .views import poll_list, PollList, PollView, pollvote, PollCreate, PollEdit ,OptionCreate, OptionEdit, PollDelete, OptionDelete

urlpatterns = [
    path("", poll_list),
    path("list", PollList.as_view(), name='poll_list'),
    path("<int:pk>/", PollView.as_view(), name='poll_view'),
    path('<int:oid>/vote/', pollvote.as_view(), name='poll_vote'),
    path('add', PollCreate.as_view(), name='poll_create'),
    path("<int:pk>/edit", PollEdit.as_view(), name="poll_edit"),
    path("<int:pid>/add", OptionCreate.as_view(), name="option_create"),
    path("<int:oid>/modify", OptionEdit.as_view(), name="option_edit"),
    path("<int:pk>/delete)",PollDelete.as_view(), name='poll_delete'),
    path("<int:pk>/remove", OptionDelete.as_view(), name='option_delete'),
]
