from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_nav_active(context, path):
    """Проверяет активна ли ссылка"""
    if path in context.request.get_full_path():
        return 'active'
    return None


@register.inclusion_tag('templatetags/dropdown.html', takes_context=True)
def draw_dropdown(context, item):
    """Отрисовка выпадающего списка"""
    full_path = context.request.get_full_path()
    return {'item': item, 'full_path': full_path}
