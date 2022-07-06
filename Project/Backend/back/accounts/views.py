from typing_extensions import Self
from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import send_mail
from .models import *
from .text import *


def index(request):
    subject_main_text = MainText.objects.all()
    subject_concept_text = ConceptText.objects.all()
    subject_cases_text = CasesText.objects.all()
    subject_date_text = DateText.objects.all()
    subject_quest_text = QuestionText.objects.all()
    subject_last_text = LastText.objects.all()
    try:
        context = {

            'tittle_mainW': subject_main_text[0],
            'text_mainW': subject_main_text[1],
            'btn_mainW': subject_main_text[2],

            'first_title': subject_concept_text[0],
            'first_text': subject_concept_text[1],
            'second_title': subject_concept_text[2],
            'second_text': subject_concept_text[3],
            'thrid_title': subject_concept_text[4],
            'iqon_1': subject_concept_text[5],
            'iqon_2': subject_concept_text[6],
            'iqon_3': subject_concept_text[7],
            'iqon_4': subject_concept_text[8],

            'cases_title': subject_cases_text[0],
            'cases_text': subject_cases_text[1],
            'case_1': subject_cases_text[2],
            'case_2': subject_cases_text[3],
            'case_3': subject_cases_text[4],
            'case_4': subject_cases_text[5],
            'case_5': subject_cases_text[6],
            'case_6': subject_cases_text[7],
            'case_7': subject_cases_text[8],
            'case_8': subject_cases_text[9],

            'date_title': subject_date_text[0],
            'date_text': subject_date_text[1],
            'date_first': subject_date_text[2],
            'date_first_text': subject_date_text[3],
            'date_second': subject_date_text[4],
            'date_second_text': subject_date_text[5],
            'date_thrid': subject_date_text[6],
            'date_thrid_text': subject_date_text[7],
            'date_fourth': subject_date_text[8],
            'date_fourth_text': subject_date_text[9],
            'date_fifth': subject_date_text[10],
            'date_fifth_text': subject_date_text[11],

            'question_title': subject_quest_text[0],
            'question_1': subject_quest_text[1],
            'question_1_text': subject_quest_text[2],
            'question_2': subject_quest_text[3],
            'question_2_text': subject_quest_text[4],
            'question_3': subject_quest_text[5],
            'question_3_text': subject_quest_text[6],
            'question_4': subject_quest_text[7],
            'question_4_text': subject_quest_text[8],
            'question_5': subject_quest_text[9],
            'question_5_text': subject_quest_text[10],
            'question_6': subject_quest_text[11],
            'question_6_text': subject_quest_text[12],

            'btn_1': subject_last_text[0],
            'btn_2': subject_last_text[1],
            'btn_3': subject_last_text[2],
            'btn_4': subject_last_text[3],
            'btn_5': subject_last_text[4],
            'btn_6': subject_last_text[5],
            'last_text_1': subject_last_text[6],
            'last_text_2': subject_last_text[7],
            'last_text_3': subject_last_text[8],
            'last_text_4': subject_last_text[9],

        }
    except IndexError:
        templates()
        templates_images()
        templates_case1()
        templates_case2()
        templates_case3()
        templates_case4()
        templates_case5()
        templates_case6()
        templates_case7()
        templates_case8()

    return render(request, 'accounts/index.html', context)


def case1(request):
    form = AccForm()
    error = ''
    subject_case1_text = Case1.objects.all()
    data = ImageCase.objects.get(pk=1)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():

            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'

    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case1_text[0],
            'case_name': subject_case1_text[1],
            'case_btn_1': subject_case1_text[2],
            'case_btn_2': subject_case1_text[3],
            'case_btn_3': subject_case1_text[4],
            'case_btn_4': subject_case1_text[5],
            'case_btn_5': subject_case1_text[6],
            'case_comp_title': subject_case1_text[7],
            'case_comp_text': subject_case1_text[8],
            'case_text_1': subject_case1_text[9],
            'case_text_2': subject_case1_text[10],
            'case_text_3': subject_case1_text[11],
            'case_boss_name_1': subject_case1_text[12],
            'case_boss_job_1': subject_case1_text[13],
            'case_boss_comp_1': subject_case1_text[14],
            'case_boss_name_2': subject_case1_text[15],
            'case_boss_job_2': subject_case1_text[16],
            'case_boss_comp_2': subject_case1_text[17],
            'case_boss_name_3': subject_case1_text[18],
            'case_boss_job_3': subject_case1_text[19],
            'case_boss_comp_3': subject_case1_text[20],
            'case_reg': subject_case1_text[21],
            'case_btn_6': subject_case1_text[22],
            'case_btn_7': subject_case1_text[23],
            'case_lastText_1': subject_case1_text[24],
            'case_lastText_2': subject_case1_text[25],
            'case_lastText_3': subject_case1_text[26],
            'case_lastText_4': subject_case1_text[27],
            'case_lastText_5': subject_case1_text[28],

        }
    except IndexError:
        templates_case1()

    return render(request, 'accounts/case.html', context)


def case2(request):
    form = AccForm()
    error = ''
    subject_case2_text = Case2.objects.all()
    data = ImageCase.objects.get(pk=2)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'
    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case2_text[0],
            'case_name': subject_case2_text[1],
            'case_btn_1': subject_case2_text[2],
            'case_btn_2': subject_case2_text[3],
            'case_btn_3': subject_case2_text[4],
            'case_btn_4': subject_case2_text[5],
            'case_btn_5': subject_case2_text[6],
            'case_comp_title': subject_case2_text[7],
            'case_comp_text': subject_case2_text[8],
            'case_text_1': subject_case2_text[9],
            'case_text_2': subject_case2_text[10],
            'case_text_3': subject_case2_text[11],
            'case_boss_name_1': subject_case2_text[12],
            'case_boss_job_1': subject_case2_text[13],
            'case_boss_comp_1': subject_case2_text[14],
            'case_boss_name_2': subject_case2_text[15],
            'case_boss_job_2': subject_case2_text[16],
            'case_boss_comp_2': subject_case2_text[17],
            'case_boss_name_3': subject_case2_text[18],
            'case_boss_job_3': subject_case2_text[19],
            'case_boss_comp_3': subject_case2_text[20],
            'case_reg': subject_case2_text[21],
            'case_btn_6': subject_case2_text[22],
            'case_btn_7': subject_case2_text[23],
            'case_lastText_1': subject_case2_text[24],
            'case_lastText_2': subject_case2_text[25],
            'case_lastText_3': subject_case2_text[26],
            'case_lastText_4': subject_case2_text[27],
            'case_lastText_5': subject_case2_text[28],
        }
    except IndexError:
        templates_case2()
    return render(request, 'accounts/case.html', context)


def case3(request):
    form = AccForm()
    error = ''
    subject_case3_text = Case3.objects.all()
    data = ImageCase.objects.get(pk=3)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'
    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case3_text[0],
            'case_name': subject_case3_text[1],
            'case_btn_1': subject_case3_text[2],
            'case_btn_2': subject_case3_text[3],
            'case_btn_3': subject_case3_text[4],
            'case_btn_4': subject_case3_text[5],
            'case_btn_5': subject_case3_text[6],
            'case_comp_title': subject_case3_text[7],
            'case_comp_text': subject_case3_text[8],
            'case_text_1': subject_case3_text[9],
            'case_text_2': subject_case3_text[10],
            'case_text_3': subject_case3_text[11],
            'case_boss_name_1': subject_case3_text[12],
            'case_boss_job_1': subject_case3_text[13],
            'case_boss_comp_1': subject_case3_text[14],
            'case_boss_name_2': subject_case3_text[15],
            'case_boss_job_2': subject_case3_text[16],
            'case_boss_comp_2': subject_case3_text[17],
            'case_boss_name_3': subject_case3_text[18],
            'case_boss_job_3': subject_case3_text[19],
            'case_boss_comp_3': subject_case3_text[20],
            'case_reg': subject_case3_text[21],
            'case_btn_6': subject_case3_text[22],
            'case_btn_7': subject_case3_text[23],
            'case_lastText_1': subject_case3_text[24],
            'case_lastText_2': subject_case3_text[25],
            'case_lastText_3': subject_case3_text[26],
            'case_lastText_4': subject_case3_text[27],
            'case_lastText_5': subject_case3_text[28],
        }
    except IndexError:
        templates_case3()
    return render(request, 'accounts/case.html', context)


def case4(request):
    form = AccForm()
    error = ''
    subject_case4_text = Case4.objects.all()
    data = ImageCase.objects.get(pk=4)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'
    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case4_text[0],
            'case_name': subject_case4_text[1],
            'case_btn_1': subject_case4_text[2],
            'case_btn_2': subject_case4_text[3],
            'case_btn_3': subject_case4_text[4],
            'case_btn_4': subject_case4_text[5],
            'case_btn_5': subject_case4_text[6],
            'case_comp_title': subject_case4_text[7],
            'case_comp_text': subject_case4_text[8],
            'case_text_1': subject_case4_text[9],
            'case_text_2': subject_case4_text[10],
            'case_text_3': subject_case4_text[11],
            'case_boss_name_1': subject_case4_text[12],
            'case_boss_job_1': subject_case4_text[13],
            'case_boss_comp_1': subject_case4_text[14],
            'case_boss_name_2': subject_case4_text[15],
            'case_boss_job_2': subject_case4_text[16],
            'case_boss_comp_2': subject_case4_text[17],
            'case_boss_name_3': subject_case4_text[18],
            'case_boss_job_3': subject_case4_text[19],
            'case_boss_comp_3': subject_case4_text[20],
            'case_reg': subject_case4_text[21],
            'case_btn_6': subject_case4_text[22],
            'case_btn_7': subject_case4_text[23],
            'case_lastText_1': subject_case4_text[24],
            'case_lastText_2': subject_case4_text[25],
            'case_lastText_3': subject_case4_text[26],
            'case_lastText_4': subject_case4_text[27],
            'case_lastText_5': subject_case4_text[28],
        }
    except IndexError:
        templates_case4()
    return render(request, 'accounts/case.html', context)


def case5(request):
    form = AccForm()
    error = ''
    subject_case5_text = Case5.objects.all()
    data = ImageCase.objects.get(pk=5)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'
    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case5_text[0],
            'case_name': subject_case5_text[1],
            'case_btn_1': subject_case5_text[2],
            'case_btn_2': subject_case5_text[3],
            'case_btn_3': subject_case5_text[4],
            'case_btn_4': subject_case5_text[5],
            'case_btn_5': subject_case5_text[6],
            'case_comp_title': subject_case5_text[7],
            'case_comp_text': subject_case5_text[8],
            'case_text_1': subject_case5_text[9],
            'case_text_2': subject_case5_text[10],
            'case_text_3': subject_case5_text[11],
            'case_boss_name_1': subject_case5_text[12],
            'case_boss_job_1': subject_case5_text[13],
            'case_boss_comp_1': subject_case5_text[14],
            'case_boss_name_2': subject_case5_text[15],
            'case_boss_job_2': subject_case5_text[16],
            'case_boss_comp_2': subject_case5_text[17],
            'case_boss_name_3': subject_case5_text[18],
            'case_boss_job_3': subject_case5_text[19],
            'case_boss_comp_3': subject_case5_text[20],
            'case_reg': subject_case5_text[21],
            'case_btn_6': subject_case5_text[22],
            'case_btn_7': subject_case5_text[23],
            'case_lastText_1': subject_case5_text[24],
            'case_lastText_2': subject_case5_text[25],
            'case_lastText_3': subject_case5_text[26],
            'case_lastText_4': subject_case5_text[27],
            'case_lastText_5': subject_case5_text[28],
        }
    except IndexError:
        templates_case5()
    return render(request, 'accounts/case.html', context)


def case6(request):
    form = AccForm()
    error = ''
    subject_case6_text = Case6.objects.all()
    data = ImageCase.objects.get(pk=6)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'
    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case6_text[0],
            'case_name': subject_case6_text[1],
            'case_btn_1': subject_case6_text[2],
            'case_btn_2': subject_case6_text[3],
            'case_btn_3': subject_case6_text[4],
            'case_btn_4': subject_case6_text[5],
            'case_btn_5': subject_case6_text[6],
            'case_comp_title': subject_case6_text[7],
            'case_comp_text': subject_case6_text[8],
            'case_text_1': subject_case6_text[9],
            'case_text_2': subject_case6_text[10],
            'case_text_3': subject_case6_text[11],
            'case_boss_name_1': subject_case6_text[12],
            'case_boss_job_1': subject_case6_text[13],
            'case_boss_comp_1': subject_case6_text[14],
            'case_boss_name_2': subject_case6_text[15],
            'case_boss_job_2': subject_case6_text[16],
            'case_boss_comp_2': subject_case6_text[17],
            'case_boss_name_3': subject_case6_text[18],
            'case_boss_job_3': subject_case6_text[19],
            'case_boss_comp_3': subject_case6_text[20],
            'case_reg': subject_case6_text[21],
            'case_btn_6': subject_case6_text[22],
            'case_btn_7': subject_case6_text[23],
            'case_lastText_1': subject_case6_text[24],
            'case_lastText_2': subject_case6_text[25],
            'case_lastText_3': subject_case6_text[26],
            'case_lastText_4': subject_case6_text[27],
            'case_lastText_5': subject_case6_text[28],
        }
    except IndexError:
        templates_case6()
    return render(request, 'accounts/case.html', context)


def case7(request):
    form = AccForm()
    error = ''
    subject_case7_text = Case7.objects.all()
    data = ImageCase.objects.get(pk=7)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'
    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case7_text[0],
            'case_name': subject_case7_text[1],
            'case_btn_1': subject_case7_text[2],
            'case_btn_2': subject_case7_text[3],
            'case_btn_3': subject_case7_text[4],
            'case_btn_4': subject_case7_text[5],
            'case_btn_5': subject_case7_text[6],
            'case_comp_title': subject_case7_text[7],
            'case_comp_text': subject_case7_text[8],
            'case_text_1': subject_case7_text[9],
            'case_text_2': subject_case7_text[10],
            'case_text_3': subject_case7_text[11],
            'case_boss_name_1': subject_case7_text[12],
            'case_boss_job_1': subject_case7_text[13],
            'case_boss_comp_1': subject_case7_text[14],
            'case_boss_name_2': subject_case7_text[15],
            'case_boss_job_2': subject_case7_text[16],
            'case_boss_comp_2': subject_case7_text[17],
            'case_boss_name_3': subject_case7_text[18],
            'case_boss_job_3': subject_case7_text[19],
            'case_boss_comp_3': subject_case7_text[20],
            'case_reg': subject_case7_text[21],
            'case_btn_6': subject_case7_text[22],
            'case_btn_7': subject_case7_text[23],
            'case_lastText_1': subject_case7_text[24],
            'case_lastText_2': subject_case7_text[25],
            'case_lastText_3': subject_case7_text[26],
            'case_lastText_4': subject_case7_text[27],
            'case_lastText_5': subject_case7_text[28],
        }
    except IndexError:
        templates_case7()
    return render(request, 'accounts/case.html', context)


def case8(request):
    form = AccForm()
    error = ''
    subject_case8_text = Case8.objects.all()
    data = ImageCase.objects.get(pk=8)
    if request.method == 'POST':
        form = AccForm(request.POST)

        if form.is_valid():
            subject_firstName = form.cleaned_data["first_name"]
            subject_secondName = form.cleaned_data["second_name"]
            subject_number = form.data["phonenumber"]
            to_email = form.cleaned_data["email"]
            subject_flag = form.cleaned_data["flag"]
            subject_age = form.cleaned_data["age"]

            if subject_flag != True:
                error = 'Поставьте пользовательское соглашение!!!!'
            elif subject_age < 14 or subject_age > 100:
                error = 'Учавстовать можно только с 14 и до 100!!!!'
            else:
                form.save()

                send_mail(
                    'Хакатон 2022',
                    'Поздравляем, вы успешно зарегистрировались на хакатон от компании Fogstream.\n' + 'Наименование кейса: ' + '\n' + 'Ваше имя и фамилия: ' + subject_firstName + ' ' + subject_secondName + '\n' + 'Ваш номер телефона: ' + subject_number,
                    'yakovec.aleksandr@bk.ru',
                    [to_email],
                )
                return redirect('index')
        else:
            error = 'Не предвиденная ошибка (возможно вы ввели уже зарегирстрированный номер или email)'
    try:
        context = {
            'form': form,
            'error': error,

            'data': data,

            'case_title': subject_case8_text[0],
            'case_name': subject_case8_text[1],
            'case_btn_1': subject_case8_text[2],
            'case_btn_2': subject_case8_text[3],
            'case_btn_3': subject_case8_text[4],
            'case_btn_4': subject_case8_text[5],
            'case_btn_5': subject_case8_text[6],
            'case_comp_title': subject_case8_text[7],
            'case_comp_text': subject_case8_text[8],
            'case_text_1': subject_case8_text[9],
            'case_text_2': subject_case8_text[10],
            'case_text_3': subject_case8_text[11],
            'case_boss_name_1': subject_case8_text[12],
            'case_boss_job_1': subject_case8_text[13],
            'case_boss_comp_1': subject_case8_text[14],
            'case_boss_name_2': subject_case8_text[15],
            'case_boss_job_2': subject_case8_text[16],
            'case_boss_comp_2': subject_case8_text[17],
            'case_boss_name_3': subject_case8_text[18],
            'case_boss_job_3': subject_case8_text[19],
            'case_boss_comp_3': subject_case8_text[20],
            'case_reg': subject_case8_text[21],
            'case_btn_6': subject_case8_text[22],
            'case_btn_7': subject_case8_text[23],
            'case_lastText_1': subject_case8_text[24],
            'case_lastText_2': subject_case8_text[25],
            'case_lastText_3': subject_case8_text[26],
            'case_lastText_4': subject_case8_text[27],
            'case_lastText_5': subject_case8_text[28],
        }
    except IndexError:
        templates_case8()
    return render(request, 'accounts/case.html', context)
