from pyramid.view import (
    view_config,
    view_defaults
)

from .forms import TestForm


@view_defaults(renderer='home.jinja2')
class TOYAPPView:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def home(self):
        return {
            'name': 'Home View'
        }

    @view_config(route_name='search_json', renderer='json')
    def search(self):
        form = TestForm().deserialize(self.request.POST)
        return {
            'choice1': form.get('choice1'),
            'choice2': form.get('choice2')
        }
