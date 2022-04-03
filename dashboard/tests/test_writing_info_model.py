from django.test import TestCase
from dashboard.models import WritingInfo
from unittest import skip
from datetime import datetime 

class WritingInfoModel(TestCase):

  def test_it_has_attribute_fields(self):
    writing = WritingInfo.objects.create(id = 1, writing_id = 1, word_count = 100, time_spent = 200,)

    self.assertIsInstance(writing.id, int)
    self.assertIsInstance(writing.writing_id, int)
    self.assertIsInstance(writing.word_count, int)
    self.assertIsInstance(writing.time_spent, int)
    self.assertIsInstance(writing.created_at, datetime)