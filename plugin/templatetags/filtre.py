from django import template

from plugin.models import Tache

register = template.Library()


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_duration(tache: Tache) -> str:
    return tache.duree_tache()
