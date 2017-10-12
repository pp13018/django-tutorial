import django
import os
import xlrd

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "package_root.settings")
    django.setup()
    from polls.models import Question, Choice
    from django.utils import timezone

    xls = xlrd.open_workbook("utils/questions.xlsx")
    sheet1 = xls.sheet_by_index(0)
    sheet2 = xls.sheet_by_index(1)
    nrows1 = sheet1.nrows-1
    ncols1 = sheet1.ncols
    nrows2 = sheet2.nrows - 1
    ncols2 = sheet2.ncols

    for row in range(1, nrows1 + 1):
        id = sheet1.cell(row, 0).value
        question_text = sheet1.cell(row, 1).value

        question = Question(id=int(id), question_text=question_text, pub_date=timezone.now())
        question.save()

    for row in range(1, nrows2 + 1):
        id = sheet2.cell(row, 0).value
        question_id = sheet2.cell(row, 1).value
        choice_text = sheet2.cell(row, 2).value
        print(id, choice_text)

        choice = Choice(id=int(id), question_id=question_id, choice_text=choice_text,)
        choice.save()

