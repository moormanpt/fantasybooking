from django import template

register = template.Library()


def only_new_world_odor(value):
    wrestlers = Wrestler.objects.filter(name='Triple H')
    return value(wrestlers)


register.filter('only_new_world_odor', only_new_world_odor)
