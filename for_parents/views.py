from django.shortcuts import render

# Create your views here.
def for_parents(request):
    return render(request, 'for_parents.html')