from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Add a CSS class to a form field."""
    return field.as_widget(attrs={"class": css_class})

@register.filter(name='file_extension')
def file_extension(value, ext):
    """Check if the file name ends with the specified extension."""
    return value.lower().endswith(ext)

@register.filter(name='add_commas')
def add_commas(value):
    """Format numbers with commas as thousand separators."""
    try:
        value = float(value)
        return f"{value:,.0f}"
    except (ValueError, TypeError):
        return value

