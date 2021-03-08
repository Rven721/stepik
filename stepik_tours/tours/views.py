from django.shortcuts import render


def main_view(request):
    return render(request, 'index.html')


def departure_view(request):
    return render(request, 'departure.html')


def tour_view(request):
    return render(request, 'tour.html')
