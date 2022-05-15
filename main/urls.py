from main.views import table_view, answer_view, clear_score
from django.urls import path

urlpatterns = [
    path('', table_view, name='table'),
    path('clear-score/', clear_score, name='clear-score'),
    path('answer/<int:cat_numb>/<int:price>/<int:mode>/', answer_view, name="answer"),
]
