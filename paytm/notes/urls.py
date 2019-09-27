from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from knox import views as knox_views
from .views import LoginView, NotesListView, NotesDeleteView, notesAdd


urlpatterns = [
    url(r'^api/v1/getAllNotes$', views.getAllNotes, name="getAllNotes"),
    # url(r'^api/login$', views.login, name="login"),
    url(r'^login$', LoginView.as_view(), name='knox_login'),
    url(r'^logout$', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('list/', login_required(NotesListView.as_view()), name="notes_list"),
    url(r'^delete/(?P<pk>\d+)', login_required(NotesDeleteView.as_view()), name="notes_del"),
    path('add/', login_required(views.notesAdd), name="notes_add"),
]