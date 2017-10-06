import django
import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "package_root.settings")
    django.setup()
    from polls.models import Question, Choice

    questions = Question.objects.all()
    print(questions)
