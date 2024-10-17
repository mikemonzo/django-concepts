from django.shortcuts import render

car_listed = [
        {'title': 'Toyota Camry', 'year': 2021},
        {'title': 'Honda Accord', 'year': 2020},
        {'title': 'Ford Escape', 'year': 2019},
]

# Create your views here.
def car_list(request):
    context = {'car_list': car_listed}
    return render(request, 'my_first_app/car_list.html', context)


def car_detail(request, id):
    context = {'car': car_listed[id]}
    return render(request, 'my_first_app/car_detail.html', context)