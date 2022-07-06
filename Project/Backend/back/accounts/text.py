from django.forms import ImageField
from .models import *


def templates():
    MainText.objects.create(text="FARCODE")
    MainText.objects.create(text="ХАКАТОН ЦИФРОВЫХ ПРОФЕССИЙ")
    MainText.objects.create(text="УЧАСТВОВАТЬ")

    ConceptText.objects.create(text="Что такое хакатон цифровых профессий?")
    ConceptText.objects.create(
        text="Это мероприятие, где команды, состоящие из молодых людей создают прототипы цифровых продуктов по техническому заданию от малого и среднего бизнеса (кейсы).")
    ConceptText.objects.create(text="Почему вам это нужно?")
    ConceptText.objects.create(
        text="Хакатон позволит вам получить крутой опыт командной разработки, новые и полезные знакомства, а также шанс попасть на стажировку или работу в IT-компанию или в IT-подразделение крупной корпорации.")
    ConceptText.objects.create(text="Как принять участие в хакатоне?")
    ConceptText.objects.create(text="Изучите кейсы, кликнув по ним")
    ConceptText.objects.create(text="Регистрируйтесь на понравившийся кейс")
    ConceptText.objects.create(text="Перед хакатоном будет укомплектована команда по навыкам")
    ConceptText.objects.create(text="Решаете кейс в дни проведения хакатона вместе со своей командой")

    CasesText.objects.create(text="Серьёзные проблемы требуют серьёзных решений")
    CasesText.objects.create(text="КЕЙСЫ ОТ ВЕДУЩИХ РОССИЙСКИХ КОМПАНИЙ")
    CasesText.objects.create(text="РАЗРАБОТКА ПРОГРАММЫ СЕРВЕРА НА DJANGO")
    CasesText.objects.create(text="ВЁРСТКА САЙТОВ ПО МАКЕТАМ (HTML + CSS)")
    CasesText.objects.create(text="РАЗРАБОТКА МОБИЛЬНОГО UI НА REACT-NATIVE")
    CasesText.objects.create(text="СОЗДАНИЕ WEB-ДИЗАЙНА")
    CasesText.objects.create(text="РАЗРАБОТКА МОБИЛЬНОГО ПРИЛОЖЕНИЯ НА IOS")
    CasesText.objects.create(text="РАЗРАБОТКА МОБИЛЬНОГО ПРИЛОЖЕНИЯ НА ANDROID")
    CasesText.objects.create(text="РАЗРАБОТКА UI НА ОДНОМ ИЗ JAVASCRIPT ФРЕЙМВОРКЕ")
    CasesText.objects.create(text="РАЗРАБОТКА ПРИЛОЖЕНИЙ ПОД WINDOWS 10 НА C++")

    DateText.objects.create(text="Что, а самое главное когда")
    DateText.objects.create(text="КЛЮЧЕВЫЕ ДАТЫ ХАКАТОНА")
    DateText.objects.create(text="15 ИЮЛЯ - 05 СЕНТЯБРЯ")
    DateText.objects.create(text="Онлайн регистрация на кейс")
    DateText.objects.create(text="05 СЕНТЯБРЯ 00:00")
    DateText.objects.create(text="Окончание приема заявок от участников хакатона")
    DateText.objects.create(text="ДО 15 СЕНТЯБРЯ")
    DateText.objects.create(text="Формирование команд на кейсы и приглашение на хакатон")
    DateText.objects.create(text="23-24 СЕНТЯБРЯ")
    DateText.objects.create(text="Старт 2-х дней хакатона + экспертная поддержка")
    DateText.objects.create(text="24 СЕНТЯБРЯ")
    DateText.objects.create(text="Финал для команд кейсов / подведение итогов")

    QuestionText.objects.create(text="Часто задаваемые вопросы и ответы")
    QuestionText.objects.create(text="ВОПРОС 1")
    QuestionText.objects.create(text="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Modi, quos?")
    QuestionText.objects.create(text="ВОПРОС 2")
    QuestionText.objects.create(
        text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam neque labore soluta consectetur repellendus sequi.")
    QuestionText.objects.create(text="ВОПРОС 3")
    QuestionText.objects.create(
        text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellat libero neque modi harum necessitatibus autem. Lorem ipsum dolor sit amet consectetur adipisicing elit. Vel deleniti temporibus quos omnis, voluptates beatae accusantium maxime vitae aperiam officiis ratione quod fugiat minus, enim unde odit! Perferendis, nemo deserunt maxime voluptates quaerat similique voluptas natus corrupti facilis quis a cupiditate blanditiis, hic autem harum impedit iste, in necessitatibus quisquam!")
    QuestionText.objects.create(text="ВОПРОС 4")
    QuestionText.objects.create(
        text="Lorem ipsum dolor, sit amet consectetur adipisicing elit. At, sequi? Consectetur magnam, veritatis nam nemo iste vero odit fugit quia!")
    QuestionText.objects.create(text="ВОПРОС 5")
    QuestionText.objects.create(text="Lorem ipsum dolor sit amet.")
    QuestionText.objects.create(text="ВОПРОС 6")
    QuestionText.objects.create(text="Lorem ipsum dolor sit amet.")

    LastText.objects.create(text="Главная")
    LastText.objects.create(text="О нас")
    LastText.objects.create(text="О концепции")
    LastText.objects.create(text="Кейсы")
    LastText.objects.create(text="Ключевые даты")
    LastText.objects.create(text="FAQ")
    LastText.objects.create(text="© 2022 Golomedov Andrey")
    LastText.objects.create(text="Контакты")
    LastText.objects.create(text="+ 7 (800) 500-27-34")
    LastText.objects.create(text="help@far-code.ru")


def templates_case1():
    Case1.objects.create(text="Case")
    Case1.objects.create(text="Разработка программы сервера на Django")
    Case1.objects.create(text="Записаться")
    Case1.objects.create(text="О компании")
    Case1.objects.create(text="Описание кейса")
    Case1.objects.create(text="Менторы кейса")
    Case1.objects.create(text="Регистрация")
    Case1.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case1.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case1.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case1.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case1.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case1.objects.create(text="Алексей Кунин")
    Case1.objects.create(text="CEO")
    Case1.objects.create(text="Optiacs")
    Case1.objects.create(text="Олег Никитин")
    Case1.objects.create(text="Co-founder")
    Case1.objects.create(text="Optiacs")
    Case1.objects.create(text="Ольга Лукьянова")
    Case1.objects.create(text="Co-founder")
    Case1.objects.create(text="Optiacs")
    Case1.objects.create(text="Регистрация на кейс")
    Case1.objects.create(text="Главная")
    Case1.objects.create(text="О нас")
    Case1.objects.create(text="FARCODE")
    Case1.objects.create(text="© 2022 Golomedov Andrey")
    Case1.objects.create(text="Контакты")
    Case1.objects.create(text="+ 7 (800) 500-27-34")
    Case1.objects.create(text="help@far-code.ru")


def templates_case2():
    Case2.objects.create(text="Case")
    Case2.objects.create(text="Вёрстка сайтов по макетам (HTML + CSS)")
    Case2.objects.create(text="Записаться")
    Case2.objects.create(text="О компании")
    Case2.objects.create(text="Описание кейса")
    Case2.objects.create(text="Менторы кейса")
    Case2.objects.create(text="Регистрация")
    Case2.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case2.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case2.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case2.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case2.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case2.objects.create(text="Алексей Кунин")
    Case2.objects.create(text="CEO")
    Case2.objects.create(text="Optiacs")
    Case2.objects.create(text="Олег Никитин")
    Case2.objects.create(text="Co-founder")
    Case2.objects.create(text="Optiacs")
    Case2.objects.create(text="Ольга Лукьянова")
    Case2.objects.create(text="Co-founder")
    Case2.objects.create(text="Optiacs")
    Case2.objects.create(text="Регистрация на кейс")
    Case2.objects.create(text="Главная")
    Case2.objects.create(text="О нас")
    Case2.objects.create(text="FARCODE")
    Case2.objects.create(text="© 2022 Golomedov Andrey")
    Case2.objects.create(text="Контакты")
    Case2.objects.create(text="+ 7 (800) 500-27-34")
    Case2.objects.create(text="help@far-code.ru")


def templates_case3():
    Case3.objects.create(text="Case")
    Case3.objects.create(text="Разработка мобильного UI на React-native")
    Case3.objects.create(text="Записаться")
    Case3.objects.create(text="О компании")
    Case3.objects.create(text="Описание кейса")
    Case3.objects.create(text="Менторы кейса")
    Case3.objects.create(text="Регистрация")
    Case3.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case3.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case3.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case3.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case3.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case3.objects.create(text="Алексей Кунин")
    Case3.objects.create(text="CEO")
    Case3.objects.create(text="Optiacs")
    Case3.objects.create(text="Олег Никитин")
    Case3.objects.create(text="Co-founder")
    Case3.objects.create(text="Optiacs")
    Case3.objects.create(text="Ольга Лукьянова")
    Case3.objects.create(text="Co-founder")
    Case3.objects.create(text="Optiacs")
    Case3.objects.create(text="Регистрация на кейс")
    Case3.objects.create(text="Главная")
    Case3.objects.create(text="О нас")
    Case3.objects.create(text="FARCODE")
    Case3.objects.create(text="© 2022 Golomedov Andrey")
    Case3.objects.create(text="Контакты")
    Case3.objects.create(text="+ 7 (800) 500-27-34")
    Case3.objects.create(text="help@far-code.ru")


def templates_case4():
    Case4.objects.create(text="Case")
    Case4.objects.create(text="Создание Web-дизайна")
    Case4.objects.create(text="Записаться")
    Case4.objects.create(text="О компании")
    Case4.objects.create(text="Описание кейса")
    Case4.objects.create(text="Менторы кейса")
    Case4.objects.create(text="Регистрация")
    Case4.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case4.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case4.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case4.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case4.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case4.objects.create(text="Алексей Кунин")
    Case4.objects.create(text="CEO")
    Case4.objects.create(text="Optiacs")
    Case4.objects.create(text="Олег Никитин")
    Case4.objects.create(text="Co-founder")
    Case4.objects.create(text="Optiacs")
    Case4.objects.create(text="Ольга Лукьянова")
    Case4.objects.create(text="Co-founder")
    Case4.objects.create(text="Optiacs")
    Case4.objects.create(text="Регистрация на кейс")
    Case4.objects.create(text="Главная")
    Case4.objects.create(text="О нас")
    Case4.objects.create(text="FARCODE")
    Case4.objects.create(text="© 2022 Golomedov Andrey")
    Case4.objects.create(text="Контакты")
    Case4.objects.create(text="+ 7 (800) 500-27-34")
    Case4.objects.create(text="help@far-code.ru")


def templates_case5():
    Case5.objects.create(text="Case")
    Case5.objects.create(text="Разработка мобильного приложения на IOS")
    Case5.objects.create(text="Записаться")
    Case5.objects.create(text="О компании")
    Case5.objects.create(text="Описание кейса")
    Case5.objects.create(text="Менторы кейса")
    Case5.objects.create(text="Регистрация")
    Case5.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case5.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case5.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case5.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case5.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case5.objects.create(text="Алексей Кунин")
    Case5.objects.create(text="CEO")
    Case5.objects.create(text="Optiacs")
    Case5.objects.create(text="Олег Никитин")
    Case5.objects.create(text="Co-founder")
    Case5.objects.create(text="Optiacs")
    Case5.objects.create(text="Ольга Лукьянова")
    Case5.objects.create(text="Co-founder")
    Case5.objects.create(text="Optiacs")
    Case5.objects.create(text="Регистрация на кейс")
    Case5.objects.create(text="Главная")
    Case5.objects.create(text="О нас")
    Case5.objects.create(text="FARCODE")
    Case5.objects.create(text="© 2022 Golomedov Andrey")
    Case5.objects.create(text="Контакты")
    Case5.objects.create(text="+ 7 (800) 500-27-34")
    Case5.objects.create(text="help@far-code.ru")


def templates_case6():
    Case6.objects.create(text="Case")
    Case6.objects.create(text="Разработка мобильного приложения на Android")
    Case6.objects.create(text="Записаться")
    Case6.objects.create(text="О компании")
    Case6.objects.create(text="Описание кейса")
    Case6.objects.create(text="Менторы кейса")
    Case6.objects.create(text="Регистрация")
    Case6.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case6.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case6.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case6.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case6.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case6.objects.create(text="Алексей Кунин")
    Case6.objects.create(text="CEO")
    Case6.objects.create(text="Optiacs")
    Case6.objects.create(text="Олег Никитин")
    Case6.objects.create(text="Co-founder")
    Case6.objects.create(text="Optiacs")
    Case6.objects.create(text="Ольга Лукьянова")
    Case6.objects.create(text="Co-founder")
    Case6.objects.create(text="Optiacs")
    Case6.objects.create(text="Регистрация на кейс")
    Case6.objects.create(text="Главная")
    Case6.objects.create(text="О нас")
    Case6.objects.create(text="FARCODE")
    Case6.objects.create(text="© 2022 Golomedov Andrey")
    Case6.objects.create(text="Контакты")
    Case6.objects.create(text="+ 7 (800) 500-27-34")
    Case6.objects.create(text="help@far-code.ru")


def templates_case7():
    Case7.objects.create(text="Case")
    Case7.objects.create(text="Разработка UI на одном из JavaScript фреймворке")
    Case7.objects.create(text="Записаться")
    Case7.objects.create(text="О компании")
    Case7.objects.create(text="Описание кейса")
    Case7.objects.create(text="Менторы кейса")
    Case7.objects.create(text="Регистрация")
    Case7.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case7.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case7.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case7.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case7.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case7.objects.create(text="Алексей Кунин")
    Case7.objects.create(text="CEO")
    Case7.objects.create(text="Optiacs")
    Case7.objects.create(text="Олег Никитин")
    Case7.objects.create(text="Co-founder")
    Case7.objects.create(text="Optiacs")
    Case7.objects.create(text="Ольга Лукьянова")
    Case7.objects.create(text="Co-founder")
    Case7.objects.create(text="Optiacs")
    Case7.objects.create(text="Регистрация на кейс")
    Case7.objects.create(text="Главная")
    Case7.objects.create(text="О нас")
    Case7.objects.create(text="FARCODE")
    Case7.objects.create(text="© 2022 Golomedov Andrey")
    Case7.objects.create(text="Контакты")
    Case7.objects.create(text="+ 7 (800) 500-27-34")
    Case7.objects.create(text="help@far-code.ru")


def templates_case8():
    Case8.objects.create(text="Case")
    Case8.objects.create(text="Разработка приложений под Windows 10 на C++")
    Case8.objects.create(text="Записаться")
    Case8.objects.create(text="О компании")
    Case8.objects.create(text="Описание кейса")
    Case8.objects.create(text="Менторы кейса")
    Case8.objects.create(text="Регистрация")
    Case8.objects.create(
        text="ООО «ОПТИАКС» - это IT-стартап, который разрабатывает системы для анализа данных на фондовых рынках. Используются собственные разработки в области машинного обучения, алгоритмических торговых систем, искусственного интеллекта.")
    Case8.objects.create(
        text="На текущий момент наш продукт - аналитические данные на финансовых рынках. Это продукт для компаний, которые специализируются на управлении активами фондовых рынков.")
    Case8.objects.create(
        text="Разрабатываемая технология относится к области предиктивной аналитики. Обладая знаниями не только в финансах, но и в математике, команда проекта создает самообучающуюся систему, позволяющую предсказывать доходность на фондовых биржах точнее традиционных инструментов. Создаваемая модель при разных вводных сможет прогнозировать доходность выше на 8-30% по бумагам компаний S&P500.")
    Case8.objects.create(
        text="При этом они создают не просто инструмент для хедж-фондов, использующих роботов для торговли. Основной продукт компании - мобильное приложение для управления финансовым портфелем на бирже с помощью искусственного интеллекта. Это приложение позволит людям без специальных знаний выбрать их инвестиционные приоритеты, подберет индивидуальную инвестиционную стратегию, покажет результаты тестирования и позволит отслеживать данную стратегию в реальном времени, либо использовать ее для автоматического управления брокерским счетом пользователя.")
    Case8.objects.create(
        text="Компания активно участвует в инновационных конкурсах и международных форумах в области информационных технологий. Технология была продемонстрирована на международной престижной конференции \"Fintech Finals\" (Гонконг). Проект компании стал победителем конкурса \"Startup Village by The Sea\" от Фонда \"Сколково\".")
    Case8.objects.create(text="Алексей Кунин")
    Case8.objects.create(text="CEO")
    Case8.objects.create(text="Optiacs")
    Case8.objects.create(text="Олег Никитин")
    Case8.objects.create(text="Co-founder")
    Case8.objects.create(text="Optiacs")
    Case8.objects.create(text="Ольга Лукьянова")
    Case8.objects.create(text="Co-founder")
    Case8.objects.create(text="Optiacs")
    Case8.objects.create(text="Регистрация на кейс")
    Case8.objects.create(text="Главная")
    Case8.objects.create(text="О нас")
    Case8.objects.create(text="FARCODE")
    Case8.objects.create(text="© 2022 Golomedov Andrey")
    Case8.objects.create(text="Контакты")
    Case8.objects.create(text="+ 7 (800) 500-27-34")
    Case8.objects.create(text="help@far-code.ru")


def templates_images():
    ImageCase.objects.create(title="case1", cover="cases\case1.jpg")
    ImageCase.objects.create(title="case2", cover="cases\case2.jpg")
    ImageCase.objects.create(title="case3", cover="cases\case3.jpg")
    ImageCase.objects.create(title="case4", cover="cases\case4.jpg")
    ImageCase.objects.create(title="case5", cover="cases\case5.jpg")
    ImageCase.objects.create(title="case6", cover="cases\case6.jpg")
    ImageCase.objects.create(title="case7", cover="cases\case7.jpg")
    ImageCase.objects.create(title="case8", cover="cases\case8.jpg")
