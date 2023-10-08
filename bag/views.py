from django.shortcuts import render

def view_bag(request):
    # to view shopping bag page
    return render(request, 'bag/bag.html')
