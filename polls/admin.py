from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)