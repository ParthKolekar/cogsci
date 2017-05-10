from django.db import models

# Create your models here.


class Comprehension(models.Model):
    comprehension_text = models.TextField()

    def __str__(self):
        return "{:.25}...".format(self.comprehension_text)
    __repr__ = __str__


class Question(models.Model):
    question_comprehension = models.ForeignKey(Comprehension)
    question_text = models.TextField()
    question_answer = models.CharField(
         choices=(
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
            ('X', 'Not Submitted')
        ),
        max_length=255
    )

    def __str__(self):
        return "{:.25}... - {!s:.25}".format(self.question_text, self.question_comprehension)
    __repr__ = __str__


class Submission(models.Model):
    submission_created = models.DateTimeField(auto_now_add=True)
    submission_submitted = models.DateTimeField(auto_now=True)
    submission_question = models.ForeignKey(Question)
    submission_choice = models.CharField(
        choices=(
            ('A', 'Option A'),
            ('B', 'Option B'),
            ('C', 'Option C'),
            ('D', 'Option D'),
            ('X', 'Not Submitted')
        ),
        max_length=255
    )

    def __str__(self):
        return "{!s:.25}... - {:.25}".format(self.submission_question, self.submission_choice)
    __repr__ = __str__
