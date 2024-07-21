from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    def get(self, request):

        context = {
            'title': "Bosh sahifa"
        }
        return render(request, 'blog/index.html', context)
