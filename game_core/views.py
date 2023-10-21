from django.shortcuts import render

def game_page(request):
	return render(request, 'index.html')