from django.db import models
from django.contrib.auth.models import User
from forums.models import Topic

class Post(models.Model):
    scores = (
        (1, 'Ruim'),
        (2, 'Regular'),
        (3, 'Bom'),
        (4, 'Muito Bom'),
        (5, 'Otimo')
    )

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=500, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=scores, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    comment = models.TextField()
    visible = models.BooleanField(default=False)
    pub_data = models.DateTimeField(auto_now_add=True)


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)


class Quiz(models.Model):
    question = models.ManyToManyField('Question', through='RelQuizQuestion')
    nome = models.CharField(max_length=100)
    createde_at = models.DateTimeField(auto_now_add=True)

class RelQuizQuestion(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
class Question(models.Model):
    question = models.CharField(max_length=300)
    correct_option = models.ForeignKey('Option', on_delete=models.CASCADE,related_name='questionr', null=True, blank=True)
    users = models.ManyToManyField(User, through='Answer')

class Option(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    option = models.ForeignKey('Option', on_delete=models.CASCADE)