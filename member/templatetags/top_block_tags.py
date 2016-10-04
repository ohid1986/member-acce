from django import template

from ..models import News, Gallery

register = template.Library()



@register.inclusion_tag('member/latest_news.html')
def get_latest_news():
    news_list = News.objects.order_by('-pub_date')[:1]
    return {'news_list': news_list}

@register.inclusion_tag('member/latest_event.html')
def get_latest_event():
    gallery_list = Gallery.objects.order_by('-pub_date')[:1]
    return {'gallery_list': gallery_list}