from apps.frontend.models import News, Page
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    news = News.objects.all()
    read_more = True if news.count() >= 8 else False
    return render_to_response("frontend/index.html",
        {"news_objects": news[:7], "read_more": read_more})


def news_list(request):
    # TODO: We need a pagination mech.
    news = News.objects.all()
    return render_to_response("frontend/news_list.html",
        {"news_objects": news})


def news_detail(request, slug):
    return render_to_response('frontend/news_detail.html', {
        'item': get_object_or_404(News, slug=slug)
    })


def page_detail(request, slug):
    return render_to_response('frontend/page_detail.html', {
        'item': get_object_or_404(Page, slug=slug)
    })
