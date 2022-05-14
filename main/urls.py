from main.views import table_view, answer_view
from django.urls import path

urlpatterns = [
    path('', table_view),
    path('answer/<int:cat_numb>/<int:price>/<int:mode>/', answer_view, name="answer"),
]
