from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.IndexView.as_view()),
    url(r'^index.html$',views.IndexView.as_view()),
    url(r'^page/(\d+)',views.IndexView.as_view()),
    url(r'^details/(\d+)',views.DetailsView.as_view()),
    url(r'^category/(\d+)',views.CategoryDetails.as_view()),
    url(r'^archive/(\d+)/(\d+)',views.ArchiveDetails.as_view()),
    url(r'^archive/',views.ArchiveDetails.as_view()),
    url(r'^makepost/',views.MakePost.as_view())
]