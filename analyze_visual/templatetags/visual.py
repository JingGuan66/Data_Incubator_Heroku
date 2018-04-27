from django import template

register = template.Library()

@register.filter
def in_state(things, state):
    return things.filter(county__state=state)
    
@register.filter
def in_visual_title(things, visual):
    if things.filter(visual=visual).first():
        return things.filter(visual=visual).first().title
    else:
        return None
    
@register.filter
def in_visual_description(things, visual):
    if things.filter(visual=visual).first():
        return things.filter(visual=visual).first().description
    else:
        return None