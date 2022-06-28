from django import template

from plugin.logic.services import duree_tache
from plugin.models import Tache

register = template.Library()


@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_duration(tache: Tache) -> str:
    return duree_tache(tache)
