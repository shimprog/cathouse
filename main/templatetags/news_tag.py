from django import template
from main.models import News


register = template.Library()


@register.inclusion_tag('main/tags/newsblock.html')
def get_news_tag():
    newsblockss = News.objects.order_by('-id')[:3]
    return {"newsblockss": newsblockss}