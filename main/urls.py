from main.views import table_view, answer_view, clear_score, start_view
from django.urls import path

urlpatterns = [
    path('', start_view, name='start'),
    path('table/', table_view, name='table'),
    path('clear-score/', clear_score, name='clear-score'),
    path('answer/<int:cat_numb>/<int:price>/<int:mode>/', answer_view, name="answer"),
]
