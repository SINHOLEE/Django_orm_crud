from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 사용자가 form 에서 전달한 정보를 꺼낸다.
    # new에서 보낸 정보는 어디에 있을까? request에 담겨져 있다.
    # GET()으로 받을 수 있다.
    print(request.GET)
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 해당 정보를 Aritcle 모델을 에용하여 새롭게 데이터를 저장한다,.
    Article.objects.create(title=title, content=content)

    # 사용자에게 저장이 완료되었다는 페이지를 보여준다.
    return render(request, 'articles/create.html')