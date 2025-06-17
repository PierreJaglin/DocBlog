from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def article(request, article_id):
    # In a real application, you would fetch the article from the database
    # using the article_id. Here we just return a placeholder response.
    if article_id in ['1', '2', '3']:
        return render(request, f"blog/article_{article_id}.html")
    else:
        return render(request, 'blog/article_not_found.html', status=404)