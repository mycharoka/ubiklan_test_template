from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'banner':'We innovate ways that put technology to out-of-home ads.',
        'sub_banner':'It\'s a modern twist to the traditional.',
    }
    return render(request, 'index.html', context)