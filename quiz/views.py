from django.shortcuts import render, redirect

from .models import Comprehension, Question, Submission
# Create your views here.


def index(request):
    return redirect('display-comprehension')


def display_comprehension(request):
    comprehensions_read = request.session.get('comprehensions_read', [])
    comprehension_to_read = Comprehension.objects.exclude(pk__in=comprehensions_read).order_by('pk').first()

    if comprehension_to_read is None:
        return redirect('thanks')

    comprehensions_read.append(comprehension_to_read.id)
    request.session['comprehensions_read'] = comprehensions_read

    return render(request, 'quiz/display_comprehension.html', {'comprehension': comprehension_to_read})


def display_question(request):
    questions_read = request.session.get('questions_read', [])
    comprehensions_read = request.session.get('comprehensions_read', [])

    question_to_read = Question.objects.exclude(pk__in=questions_read).order_by('pk').filter(question_comprehension__in=comprehensions_read).first()

    if question_to_read is None:
        return redirect('display-comprehension')

    questions_read.append(question_to_read.id)
    request.session['questions_read'] = questions_read

    submission = Submission.objects.create(submission_question=question_to_read, submission_choice='X')

    return render(request, 'quiz/display_question.html', {'question': question_to_read, 'submission_id': submission.id})


def process_submission(request):
    if request.method != "POST":
        raise Exception('something bad')

    form_submission_id = request.POST.get('submission_id', None)
    if form_submission_id is None:
        raise Exception('something bad')

    submission = Submission.objects.get(pk=form_submission_id)

    if submission is None:
        raise Exception('something bad')

    form_submission_choice = request.POST.get('submission_choice', None)

    if form_submission_choice is None:
        raise Exception('something bad')

    submission.submission_choice = form_submission_choice
    submission.save()

    question = submission.submission_question

    remaining_questions = Question.objects.filter(question_comprehension=question.question_comprehension)

    if remaining_questions.count() != 0:
        return redirect('display-question')
    else:
        return redirect('display-comprehension')


def thanks(request):
    request.session.flush()
    return render(request, 'quiz/thanks.html')
