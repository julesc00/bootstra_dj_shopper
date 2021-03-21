from django.shortcuts import render


def home_view(request):
    content = {}

    return render(request, "app/index.html", content)
