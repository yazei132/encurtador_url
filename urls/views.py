from django.shortcuts import render,redirect,get_object_or_404
from .forms import UrlForm
from .models import Url

def home(request):
    form = UrlForm
    short_url = None

    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.save()
            short_url = request.build_absolute_uri(f"/{url.short_code}")

    return render(request, 'urls/home.html', {'form': form, 'short_url': short_url})

def redirect_view(request, short_code):
    url = get_object_or_404(Url, short_code = short_code )
    return redirect(url.original_url)
    
