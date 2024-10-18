"""
This module contains view functions for the my_first_app Django application.
"""

from django.views.generic import TemplateView

car_listed = [
        {'title': 'Toyota Camry', 'year': 2021},
        {'title': 'Honda Accord', 'year': 2020},
        {'title': 'Ford Escape', 'year': 2019},
]

class CarListView(TemplateView):
    """
    CarLisView is a Django TemplateView that renders a list of cars.

    Attributes:
        template_name (str): The path to the template used to render the view.

    Methods:
        get_context_data(**kwargs):
            Adds a list of cars to the context data for rendering in the template.
            Args:
                **kwargs: Arbitrary keyword arguments.
            Returns:
                dict: The context data with the added car list.
    """
    template_name = 'my_first_app/car_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_list'] = car_listed
        return context


class CarDetailView(TemplateView):
    """
    CarDetailView is a Django TemplateView that renders the details of a car.
    Attributes:
        template_name (str): The path to the template used to render the view.
    Methods:
        get_context_data(**kwargs):
            Retrieves the context data for rendering the template.
            Args:
                **kwargs: Arbitrary keyword arguments.
            Returns:
                dict: Context data containing the car details.
    """
    template_name = 'my_first_app/car_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'car': car_listed[kwargs['id']]}
        return context
