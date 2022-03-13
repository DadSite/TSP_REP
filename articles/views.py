from django.shortcuts import render

def home_page(request):
    return render(request, "articles/index.html")

def posts(request):
    pass

def post_inv(request):
    pass

def articles(request):
    return render(request, "articles/articles.html")

def about(request):
    return render(request, "articles/about.html")

def reading_list(request):
    return render(request, "articles/reading-list.html")

def character_study(request):
    return render(request, "articles/character-study.html")

def privacy_policy(request):
    return render(request, "articles/privacy-policy.html")