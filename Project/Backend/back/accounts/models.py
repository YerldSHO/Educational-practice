from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Choices:
    choice = (
        ('Разработка программы сервера на Django', 'Разработка программы сервера на Django'),
        ('Вёрстка сайтов по макетам (HTML + CSS)', 'Вёрстка сайтов по макетам (HTML + CSS)'),
        ('Разработка мобильного UI на React-native', 'Разработка мобильного UI на React-native'),
        ('Создание Web-дизайна', 'Создание Web-дизайна'),
        ('Разработка мобильного приложения на IOS', 'Разработка мобильного приложения на IOS'),
        ('Разработка мобильного приложения на Android', 'Разработка мобильного приложения на Android'),
        ('Разработка UI на одном из JavaScript фреймворке', 'Разработка UI на одном из JavaScript фреймворке'),
        ('Разработка приложений под Windows 10 на C++', 'Разработка приложений под Windows 10 на C++'),
    )


class Accounts(models.Model):
    first_name = models.CharField('Фамилия', max_length=15)
    second_name = models.CharField('Имя', max_length=15)
    phonenumber = PhoneNumberField('Номер', unique=True, null=False, blank=False)
    email = models.EmailField('Email', max_length=254, unique=True)
    role = models.TextField('Роль')
    age = models.IntegerField('Возвраст')
    corp = models.CharField('Университет / Организация / Самостоятельно', max_length=254)
    choice = models.CharField('Выберите кейс', max_length=300, choices=Choices.choice)
    flag = models.BooleanField('Принял ли пользовательское соглашение')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Аккаунт участника'
        verbose_name_plural = 'Аккаунты участников'


class MainText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Основная страница'


class ConceptText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Страница концепции'


class CasesText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Страница кейсов'


class DateText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Страница дат'


class QuestionText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Страница вопросов'


class LastText(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Кнопки и конечная информация'


class Case1(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 1 кейса'


class Case2(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 2 кейса'


class Case3(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 3 кейса'


class Case4(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 4 кейса'


class Case5(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 5 кейса'


class Case6(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 6 кейса'


class Case7(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 7 кейса'


class Case8(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'текст'
        verbose_name_plural = 'Текст 8 кейса'


class ImageCase(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='static/src/images/cases')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'картинка'
        verbose_name_plural = 'Картинки кейсов'
