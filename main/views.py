from django.http import HttpResponse
from django.shortcuts import render

from main.models import Question


def table_view(request):
    return render(request, 'table.html')


# cat_numb номер категории, price цена в баллах, mode 1 - выводить инпут, 0 - не выводить инпут
def answer_view(request, cat_numb, price, mode):
    context = {}
    # цепляем вопрос по полученным параметрам
    q = Question.objects.get(cat_numb=cat_numb, price=price)
    if q == []:
        return render(request, 'answer.html', {'mode': False, "message": "Вопрос не найден"})
    context['q_text'] = q.question
    if request.method == "POST":
        if request.POST['answer'] == q.answer:
            context['message'], context['success_message'] = q.success_mess, 1
        else:
            context['message'], context['fail_message'] = q.fail_mess, 1
    if request.method == "GET":
        # Если mode = 1, то пользователь еще не ответил, показываем ему инпут
        if mode == 1:
            context['mode'] = True
    return render(request, 'answer.html', context)