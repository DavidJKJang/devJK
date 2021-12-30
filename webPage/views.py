from django.shortcuts import render

# Create your views here.
from django.views import View


class MainIndex(View):
	@staticmethod
	def get(request):
		context = {}
		return render(request, 'index.html', context)
