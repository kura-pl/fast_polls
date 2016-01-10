from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Choice, Question, Faq


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Faq)
admin.site.unregister((Group, User))
