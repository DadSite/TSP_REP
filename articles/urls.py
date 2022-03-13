from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("articles", views.posts, name="articles"),
    path("articles/<slug:posts>", views.post_inv, name="individual-articles"),
    path("about", views.about, name="about-page"),
    path("reading-list", views.reading_list, name="reading-list"),
    path("character-study", views.character_study, name="character-study"),
    path("privacy-policy", views.privacy_policy, name="privacy-policy")
]