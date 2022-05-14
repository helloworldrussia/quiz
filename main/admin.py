from django.contrib import admin

from main.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'cat_numb', 'price']


admin.site.register(Question, QuestionAdmin)