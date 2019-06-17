



TODO : comprendre comment utiliser {% block %}{% endblock %}




1)delete all the files in your migrations folder except __init__.py
2)drop database
3)create database
4)python makemigrations
5)python migrate

 python manage.py sqlmigrate polls 0001


$python3 manage.py inspectdb

 Delete sqlite table :

   $python manage.py dbshell
   drop table polls_people;


 Update database : (not working)

 Create Database entries:

   $python3 manage.py shell
   from polls.models import People
   from django.utils import timezone
   from datetime import datetime, timedelta
   People.objects.all()
   new_people = People(name="alfonse", surname="vivanloc", birth_date=timezone.now() + timedelta(days=30), member_type="A")
   new_people.save()


 If problems :

   python3 manage.py migrate --fake polls zero
   python3 manage.py migrate polls
   python3 manage.py inspectdb


Print in terminal :

    print("Atrus : AdherentView", flush=True)
