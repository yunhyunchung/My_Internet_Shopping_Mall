from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os

class Category(models.Model):
    # 벨로시티(건반 터치 감도)
    # touch_response = models.CharField(max_length=10, unique=True)
    # 폴리포니
    # poly_phony = models.CharField(max_length=10, unique=True)

    # 건반타입 key type
    name = models.CharField(max_length=50, null=True, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True, allow_unicode=True)

    def __str__(self):  # 카테고리 이름 반환
        return self.name

    def get_absolute_url(self):  # 카테고리 url (slug 이용)
        return f'/shopping/category/{self.slug}/'

    # Meta로 모델의 복수형(-s) 알려주기
    class Meta:
        verbose_name_plural = 'Categories'


class Maker(models.Model):
    # 제조사명
    name = models.CharField(max_length=50, null=True, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True, allow_unicode=True)
    # 본사 주소
    address = models.CharField(max_length=100, null=True)
    # 연락처
    contact = models.CharField(max_length=30, null=True)
    # 인터넷 사이트 주소
    ip_address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/shopping/maker/{self.slug}/'


class Piano(models.Model):
    # 상품명
    title = models.CharField(max_length=30)
    # 간단한 상품 설명
    content = MarkdownxField()
    # 상품 이미지
    head_image = models.ImageField(upload_to='shopping/images/%Y/%m/%d/', blank=True)
    # 가격
    price = models.CharField(max_length=30)

    # 별점
    star_rate = models.CharField(max_length=30, null=True, help_text="format) (YOUR RATE) / 5  |  ex) <em>4.5 / 5</em>")
    # 제품 출시 년월
    release_date = models.DateTimeField(null=True, help_text="format) YYYY-MM-DD  |  ex) <em>2021-12-12</em>")
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # 작성자 (외래키)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # 제조사 모델(외래키)
    maker = models.ForeignKey(Maker, null=True, on_delete=models.SET_NULL)
    # 카테고리 모델(외래키)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}'

    # content에 마크다운 문법 적용해서 html로 만든다
    def get_content_markdown(self):
        return markdown(self.content)


class Comment(models.Model):
    post = models.ForeignKey(Piano, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/406/e123cd977b739d8a/svg/{self.author.email}'