сохраните все введенные команды в отдельном файле, что бы потом вы могли легко их повторить.

3) В вашем приложении qa  в файле models.py определите следующие модели обладающие следующими полями (названия моделей и полей важны!)

Question - вопрос
title - заголовок вопроса
text - полный текст вопроса
added_at - дата добавления вопроса
rating - рейтинг вопроса (число)
author - автор вопроса
likes - список пользователей, поставивших "лайк"

Answer - ответ
text - текст ответа
added_at - дата добавления ответа
question - вопрос, к которому относится ответ
author - автор ответа

В качестве модели пользователя - используйте django.contrib.auth.models.User  из стандартной системы авторизации Django.

4) С помощью команды manage.py syncdb  создайте необходимые таблицы для ваших моделей