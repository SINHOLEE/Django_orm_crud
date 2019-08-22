from django.db import models

# Create your models here.

# 장고가 기본적으로 제공하는 모델s가 가지고 있는 모델이라는 함수?를 가져온다.? 
# 게시판을 만들겁니다.
class Article(models.Model):
    # id(pk)는 기본적으로 처음 테이블이 생성될 때 자동으로 만들어 진다.
    # id = models.AutoField(primary_key=True)

    # 모든 filed는 기본적으로 not null 비어있으면 안된다.

    # CharField 에서는 max_length가 필수 인자다.
    title = models.CharField(max_length=20) # 클래스 변수(DB의 필드)
    content = models.TextField() # 클래스 변수(DB의 필드)
    created_at = models.DateTimeField(auto_now_add=True)  # 자동으로 지금 추가되었을 때 생성
    updated_at = models.DateTimeField(auto_now=True)  # 자동으로 시간을 찍어준다?

    def __str__(self):
        return f'{self.id}번 글 - {self.title} : {self.content}'