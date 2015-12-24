from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    """
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    """
    list_display = ('title', 'pub_date', 'authors_mail')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)