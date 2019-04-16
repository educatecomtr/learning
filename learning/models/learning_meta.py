from django.db import models


class LearningMeta(models.Model):

    class Meta:
        abstract = True
        app_label = 'learning'
        db_table = 'table_name'
