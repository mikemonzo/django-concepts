"""
This module contains view functions for the my_first_app Django application.
"""

from django.shortcuts import render

car_listed = [
        {'title': 'Toyota Camry', 'year': 2021},
        {'title': 'Honda Accord', 'year': 2020},
        {'title': 'Ford Escape', 'year': 2019},
]

# Create your views here.
def car_list(request):
    """
    View function to display a list of cars.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page displaying the list of cars.
    """
    context = {'car_list': car_listed}
    return render(request, 'my_first_app/car_list.html', context)


def car_detail(request, car_id):
    """
    View function to display the details of a specific car.

    Args:
        request (HttpRequest): The HTTP request object.
        car_id (int): The ID of the car to be displayed.

    Returns:
        HttpResponse: The rendered HTML page displaying the car details.
    """
    context = {'car': car_listed[car_id]}
    return render(request, 'my_first_app/car_detail.html', context)
