from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'banner':'We innovate ways that put technology to out-of-home ads.',
        'sub_banner':'It\'s a modern twist to the traditional.',
        'footer':'Mall Taman Palem, Parkiran Lantai 8',
        'address_top' : 'Jl. Kamal Raya Cengkareng Timur, Kec. Cengkareng',
        'address_bottom': ' Jakarta Barat DKI Jakarta, 11730',
    }
    return render(request, 'index.html', context)