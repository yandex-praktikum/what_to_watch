# what_to_watch/opinions_app.py

import csv
from datetime import datetime
from random import randrange

import click
from flask import Flask, abort, flash, redirect, render_template, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# # Задаётся конкретное значение для конфигурационного ключа
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # Всесто MY SECRET KEY придумайте и впишите свой ключ
# app.config['SECRET_KEY'] = 'MY SECRET KEY'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# class Opinion(db.Model):
#     # ID — целое число, первичный ключ
#     id = db.Column(db.Integer, primary_key=True)
#     # Название фильма — строка длиной 128 символов, не может быть пустым
#     title = db.Column(db.String(128), nullable=False)
#     # Мнение о фильме — большая строка, не может быть пустым,
#     # должно быть уникальным
#     text = db.Column(db.Text, unique=True, nullable=False)
#     # Ссылка на сторонний источник — строка длиной 256 символов
#     source = db.Column(db.String(256))
#     # Дата и время — текущее время,
#     # по этому столбцу база данных будет проиндексирована
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     added_by = db.Column(db.String(64))


# Класс формы опишите сразу после модели Opinion
# class OpinionForm(FlaskForm):
#     title = StringField(
#         'Введите название фильма',
#         validators=[DataRequired(message='Обязательное поле'),
#                     Length(1, 128)]
#     )
#     text = TextAreaField(
#         'Напишите мнение',
#         validators=[DataRequired(message='Обязательное поле')]
#     )
#     source = URLField(
#         'Добавьте ссылку на подробный обзор фильма',
#         validators=[Length(1, 256), Optional()]
#     )
#     submit = SubmitField('Добавить')


# @app.cli.command('load_opinions')
# def load_opinions_command():
#     """Функция загрузки мнений в базу данных."""
#     # Открывается файл
#     with open('opinions.csv', encoding='utf-8') as f:
#         # Создаётся итерируемый объект, который отображает каждую строку
#         # в качестве словаря с ключами из шапки файла
#         reader = csv.DictReader(f)
#         # Для подсчёта строк добавляется счётчик
#         counter = 0
#         for row in reader:
#             # Распакованный словарь можно использовать
#             # для создания объекта мнения
#             opinion = Opinion(**row)
#             # Изменения нужно зафиксировать
#             db.session.add(opinion)
#             db.session.commit()
#             counter += 1
#     click.echo(f'Загружено мнений: {counter}')



# # Тут декорируется обработчик и указывается код нужной ошибки
# @app.errorhandler(404)
# def page_not_found(error):
#     # В качестве ответа возвращается собственный шаблон
#     # и код ошибки
#     return render_template('404.html'), 404
#
# @app.errorhandler(500)
# def internal_error(error):
#     # В таких случаях можно откатить незафиксированные изменения в БД
#     db.session.rollback()
#     return render_template('500.html'), 500

# @app.route('/')
# def index_view():
#     # Определяется количество мнений в базе данных
#     quantity = Opinion.query.count()
#     # Если мнений нет,
#     if not quantity:
#         # то возвращается сообщение
#         abort(404)
#     # Иначе выбирается случайное число в диапазоне от 0 и до quantity
#     offset_value = randrange(quantity)
#     # И определяется случайный объект
#     opinion = Opinion.query.offset(offset_value).first()
#
#     return render_template('opinion.html', opinion=opinion)
#
#
# @app.route('/add', methods=['GET', 'POST'])
# def add_opinion_view():
#     form = OpinionForm()
#     # Если ошибок не возникло, то
#     if form.validate_on_submit():
#         text = form.text.data
#         # Если в БД уже есть мнение с текстом, который ввёл пользователь,
#         if Opinion.query.filter_by(text=text).first() is not None:
#             # вызвать функцию flash и передать соответствующее сообщение
#             flash('Такое мнение уже было оставлено ранее!')
#             # и вернуть пользователя на страницу «Добавить новое мнение»
#             return render_template('add_opinion.html', form=form)
#         # нужно создать новый экземпляр класса Opinion
#         opinion = Opinion(
#             title=form.title.data,
#             text=form.text.data,
#             source=form.source.data
#         )
#         # Затем добавить его в сессию работы с базой данных
#         db.session.add(opinion)
#         # И зафиксировать изменения
#         db.session.commit()
#         # Затем перейти на страницу добавленного мнения
#         return redirect(url_for('opinion_view', id=opinion.id))
#     # Иначе просто отрисовать страницу с формой
#     return render_template('add_opinion.html', form=form)
#
#
#
# # Тут указывается конвертер пути для id
# @app.route('/opinions/<int:id>')
# # Параметром указывается имя переменной
# def opinion_view(id):
#     # Теперь можно запрашивать мнение по id
#     # Метод get заменён на метод get_or_404()
#     opinion = Opinion.query.get_or_404(id)
#     # И передавать его в шаблон
#     return render_template('opinion.html', opinion=opinion)



if __name__ == '__main__':
    app.run()

# # what_to_watch/opinions_app.py
#
# from datetime import datetime
# from random import randrange
#
# from flask import Flask, redirect, render_template, url_for
# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, TextAreaField, URLField
# from wtforms.validators import DataRequired, Length, Optional
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = 'MY SECRET KEY'
#
# db = SQLAlchemy(app)
#
#
# class Opinion(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(128), nullable=False)
#     text = db.Column(db.Text, unique=True, nullable=False)
#     source = db.Column(db.String(256))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#
#
# class OpinionForm(FlaskForm):
#     title = StringField(
#         'Введите название фильма',
#         validators=[DataRequired(message='Обязательное поле'),
#                     Length(1, 128)]
#     )
#     text = TextAreaField(
#         'Напишите мнение',
#         validators=[DataRequired(message='Обязательное поле')]
#     )
#     source = URLField(
#         'Добавьте ссылку на подробный обзор фильма',
#         validators=[Length(1, 256), Optional()]
#     )
#     submit = SubmitField('Добавить')
#
#
# @app.route('/')
# def index_view():
#     quantity = Opinion.query.count()
#     if not quantity:
#         return 'В базе данных записей нет.'
#     offset_value = randrange(quantity)
#     opinion = Opinion.query.offset(offset_value).first()
#     return render_template('opinion.html', opinion=opinion)
#
#
# @app.route('/add', methods=['GET', 'POST'])
# def add_opinion_view():
#     form = OpinionForm()
#     if form.validate_on_submit():
#         opinion = Opinion(
#             title=form.title.data,
#             text=form.text.data,
#             source=form.source.data
#         )
#         db.session.add(opinion)
#         db.session.commit()
#         return redirect(url_for('opinion_view', id=opinion.id))
#     return render_template('add_opinion.html', form=form)
#
#
# @app.route('/opinions/<int:id>')
# def opinion_view(id):
#     opinion = Opinion.query.get_or_404(id)
#     return render_template('opinion.html', opinion=opinion)
#
#
# if __name__ == '__main__':
#     app.run()
