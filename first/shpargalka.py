'''
python manage.py runserver - запускает сервер, чтобы остановить - ctrl+c
python manage.py startapp news - создание нового приложения - нужно зарегестрировать в settings.py [INSTALLED_APPS]
после создания таблички в models.py нужно сделать миграцию:
	python manage.py makemigrations - чтобы создать миграция
	python manage.py migrate - чтобы применить миграцию
python manage.py createsuperuser - чтобы создать админа (pass = ffff1234)

пример передачи данных в шаблон:
	{% for el in values %}
		{% if el == 'Hello' %}
			{% filter lower %}
				<p>{{ el }}</p>
			{% endfilter %}
		{% endif %}
	{% endfor %}

	{% for el in obj %}
		<p>{{ el|upper }}</p>
	{% endfor %}

'''
