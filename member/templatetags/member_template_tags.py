from django import template

from ..models import Membership, News, Event, Gallery

register = template.Library()

@register.inclusion_tag('member/sidebar.html')
def entry_history():
    entries = Membership.objects.all()
    return {'entries': entries}


