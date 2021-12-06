from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Piano, Category

# 상품 목록 페이지
class PianoList(ListView):
    model = Piano
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PianoList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context

# 상품 상세 페이지
class PianoDetail(DetailView):
    model = Piano

    def get_context_data(self, **kwargs):
        context = super(PianoDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


# 해당 카테고리 안의 post들을 보여주는 페이지
def category_page(request, slug):
    category = Category.objects.get(slug=slug)

    return render(request, 'shopping/piano_list.html',
                  {
                      'piano_list': Piano.objects.filter(category=category),
                      'categories': Category.objects.all(),
                      'category': category,
                      'category_piano_count': Piano.objects.filter(category=category).count(),
                  }
                  )
