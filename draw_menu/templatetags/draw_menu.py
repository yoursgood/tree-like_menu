from django import template

from ..models import Menu

register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, slug):  # takes slug as argument
    """Draws menu"""
    try:
        menu = Menu.objects.prefetch_related('items__items__items__items').get(slug=slug)
        return {'menu': menu, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'context': context}
