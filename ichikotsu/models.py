from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=256)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    available = models.BooleanField(default=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    
class Phase(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=256)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    available = models.BooleanField(default=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    name = models.CharField(max_length=256);
    mail_addres = models.EmailField();
    need_notification = models.BooleanField(default=True);
    available = models.BooleanField(default=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

class UserComposition(models.Model):
    ROLL_TYPES = (
        ('A', 'Administrator'),
        ('P', 'ProjectManager'),
        ('D', 'Developer'),
        ('O', 'Observer'),
        )
    roll_type = models.CharField(max_length=1, choices=ROLL_TYPES)
    available = models.BooleanField(default=True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)

class Issue(models.Model):
    def priority_validate(value):
        if value < 0 or value > 100:
            raise ValidationError(u'%s is out of range[0-100]' % value)

    phase = models.ForeignKey(Phase)
    reporter = models.ForeignKey(User)

    name = models.CharField(max_length=256)
    description = models.TextField()

    ISSUE_TYPES = (
        ('Q','Question'),
        ('T','Task'),
        ('B','Bug'),
        ('R','Risk'),
        )
    issue_type = models.CharField(max_length=1, choices=ISSUE_TYPES)

    priority = models.IntegerField(validators=[priority_validate])
    limit_date = models.DateTimeField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    close_date = models.DateTimeField(null=True)
    available = models.BooleanField(default=True)
    update_date = models.DateTimeField(auto_now=True)


class IssueAssociation(models.Model):
    parent = models.ForeignKey(Issue, db_column='parent_issue_id')
    child = models.ForeignKey(Issue, db_column='child_issue_id'))

class Activity(models.Model):
    user = models.ForeignKey(User)
    issue = models.ForeignKey(Issue)
    title = models.CharField(max_length=256)
    description = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    available = models.BooleanField(default=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
