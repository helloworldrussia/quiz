from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from main.models import Question


def start_view(request):
    request.session['score'] = 0
    context = {"background": "start.jpg", "score_off": 1}
    if request.method == "GET":
        context['first_text'] = 1
    if request.method == "POST":
        context['second_text'] = 1
        context["background"] = "fon.png"
    return render(request, 'start.html', context)


def clear_score(request):
    request.session['score'] = 0
    request.session['q_dict'] = {}
    return redirect('table')


# отображение главной таблицы с категориями и ценой вопросов
def table_view(request):
    try:
        q_dict = request.session['q_dict']
        if len(q_dict) == 30:
            return render(request, 'final.html', {"background": "fon.png", "score": request.session['score']})
    except:
        pass
    return render(request, 'table.html', {"background": "fon.png"})


# view страницы вопроса, на ней пользователь может ответить на вопрос и проверить результат
# cat_numb номер категории, price цена в баллах, mode 1 - выводить инпут для ввода ответа на впорос
def answer_view(request, cat_numb, price, mode):

    context = {}
    # цепляем вопрос по полученным параметрам
    try:
        q = Question.objects.get(cat_numb=cat_numb, price=price)
    except ObjectDoesNotExist:
        return render(request, 'answer.html', {'mode': False, "message": "Вопрос не найден"})

    try:
        question_code = f'{cat_numb}|{price}'
        a = request.session['q_dict'][question_code]
        return render(request, 'answer.html', {"background": f'{q.price}.png',
                                               'mode': False, "message": "Вы уже отвечали на этот вопрос"})
    except:
        pass

    context['q'] = q
    # При методе пост сравниваем полученный ответ с правильным и расширяем контекст
    if request.method == "POST":
        if request.POST['answer'] == q.answer:
            context['success_message'] = 1
            try:
                request.session['score'] += q.price
            except:
                request.session['score'] = q.price
        else:
            context['fail_message'] = 1
            try:
                request.session['score'] -= q.price
            except:
                request.session['score'] = 0 - q.price


        try:
            request.session['q_dict'][question_code] = 1
        except:
            request.session['q_dict'] = {question_code: 1}

    if request.method == "GET":
        # Если mode = 1, то пользователь еще не ответил, показываем ему инпут
        if mode == 1:
            context['mode'] = True
    # передаем название файла фона, который соотвествует вопросу
    context['background'] = f'{q.price}.png'
    return render(request, 'answer.html', context)
