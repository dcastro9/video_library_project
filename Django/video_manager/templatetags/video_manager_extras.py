from django.template import Library

register = Library()

@register.filter
def get_reverse_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return range(1, value +1)[::-1]

@register.filter
def get_value_from_five(value):
  """
    Filter - returns a list of values from 5 up to the given value but
    not inclusive of that value, starting at 5 and going downwards.
  """
  return range(value+1,6)[::-1]