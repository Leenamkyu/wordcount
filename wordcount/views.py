from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')
    #render는 3개의 인자를 받을수 있다
    # 첫번째 인자: 고정적으로 request사용
    # 두번째 인자: template의 이름
    # 세번째 인자: 딕셔너리 자료형(선택적 사용)  

def about(request):
    return render(request,'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full':text, 'total':len(words), 'dictionary':word_dictionary.items()})    