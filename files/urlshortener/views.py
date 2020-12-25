from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import url_form
from .models import Url
import random, string, numbers
# Create your views here.

def Home(request):
	obj = Url.objects.all()
	obj = obj[::-1][0:2]
	return render(request, 'home.html', {'obj':obj})


def create(request):
	if request.method == "POST":
		form = url_form(request.POST)
		if form.is_valid():
			original_url = form.cleaned_data['original_url']
			obj = Url.objects.filter(original_url= original_url)
			if obj:
				return render(request, 'createUrl.html', {'form': form, 'short_url':obj[0].shorten_url})
			random_charlist = list(string.ascii_letters)
			random_charlist.append([1,2,3,4,5,6,7,8,9,0])
			random_chars = ''
			for i in range(6):
				random_chars += random.choice(random_charlist)
			while len(Url.objects.filter(shorten_url= random_chars)) != 0:
				for i in range(6):
					random_chars += random.choice(random_charlist)

			s = Url(original_url= original_url, shorten_url= random_chars)
			s.save()
			return render(request, 'createUrl.html', {'form': form, 'short_url':random_chars})

	else:
		form = url_form()
	return render(request, 'createUrl.html', {'form': form})

def redirect(request, url):
	obj = Url.objects.filter(shorten_url = url)
	if obj:
		obj[0].visited = obj[0].visited + 1
		obj[0].save()
		return HttpResponseRedirect(obj[0].original_url)
		# return render(request, 'pagenotfound.html')
	else:
		return render(request, 'pagenotfound.html')