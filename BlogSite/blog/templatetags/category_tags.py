from django import template
from blog.models import BlogCategory

register = template.Library()

# Category snippets
@register.inclusion_tag('blog/categorias.html', takes_context=True)
def categories(context):
    return {
        'categories': BlogCategory.objects.all(),
        'request': context['request'],
    }