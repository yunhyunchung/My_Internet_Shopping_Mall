from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Piano, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .forms import CommentForm
from django.shortcuts import get_object_or_404

# 새 댓글 작성 & 저장
def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Piano, pk=pk)
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        return PermissionDenied

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
        context['comment_form'] = CommentForm
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

# 상품 등록 페이지
class PianoCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):  # UserPasses~와 CreateView 순서대로...
    model = Piano
    fields = ['title', 'content', 'head_image', 'price', 'category', 'star_rate', 'release_date', 'maker', 'category']

    # 이 클래스에 접근 가능한 사용자 설정
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        # 로그인 & 스태프 또는 슈퍼유저(관리자)
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user  # 로그인한 사용자를 작성자로 자동 입력
            return super(PianoCreate, self).form_valid(form)  # 새로 생성한 포스트 페이지 저장
        else:
            return redirect('/shopping/')


# 상품 수정 페이지
class PianoUpdate(LoginRequiredMixin, UpdateView):
    model = Piano
    fields = ['title', 'content', 'head_image', 'price', 'category', 'star_rate', 'release_date', 'maker', 'category']

    template_name = 'shopping/piano_update_form.html'

    # GET 방식의 요청인지 POST 방식의 요청인지 확인하는 함수
    def dispatch(self, request, *args, **kwargs):
        # 로그인한 방문자가 특정 포스트의 작성자가 맞는지 확인
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PianoUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied  # 403 오류 - 접근 권한 없음