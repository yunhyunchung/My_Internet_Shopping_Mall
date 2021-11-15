from django.db import models

class Piano(models.Model):
    # 상품명
    title = models.CharField(max_length=30)
    # 간단한 상품 설명
    content = models.TextField()
    # 상품 이미지

    # 가격
    price = models.CharField(max_length=30)
    # 제조사 모델(외래키)

    # 카테고리 모델(외래키)

    def __str__(self):
        return f'[{self.pk}]{self.piano_name}'

    def get_absolute_url(self):
        return f'/shopping/{self.pk}'

class Maker(models.Model):
    # 제조사명
    maker_name = models.CharField(max_length=30)
    # 본사 주소
    address = models.CharField(max_length=100)
    # 연락처
    contact = models.CharField(max_length=30)
    # 인터넷 사이트 주소
    ip_address  = models.CharField(max_length=100)

class Category(models.Model):
    # 건반타입
    keytype = models.CharField(max_length=20)
    # 벨로시티(건반 터치 감도)
    touch_response = models.CharField(max_length=10)
    # 폴리포니
    poly_phony = models.CharField(max_length=10)