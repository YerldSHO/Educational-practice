from django.contrib import admin
from .models import *


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'phonenumber', 'email')
    list_display_links = ('id', 'first_name', 'second_name')


class MainTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class ConceptTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class CasesTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class DateTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class QuestionTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class LastTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case1Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case2Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case3Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case4Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case5Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case6Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case7Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class Case8Admin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    readonly_fields = ('id',)


admin.site.register(Accounts, AccountsAdmin)
admin.site.register(MainText, MainTextAdmin)
admin.site.register(ConceptText, ConceptTextAdmin)
admin.site.register(CasesText, CasesTextAdmin)
admin.site.register(DateText, DateTextAdmin)
admin.site.register(QuestionText, QuestionTextAdmin)
admin.site.register(LastText, LastTextAdmin)
admin.site.register(Case1, Case1Admin)
admin.site.register(Case2, Case2Admin)
admin.site.register(Case3, Case3Admin)
admin.site.register(Case4, Case4Admin)
admin.site.register(Case5, Case5Admin)
admin.site.register(Case6, Case6Admin)
admin.site.register(Case7, Case7Admin)
admin.site.register(Case8, Case8Admin)
admin.site.register(ImageCase, ImageAdmin)
