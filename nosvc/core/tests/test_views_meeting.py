# coding: utf-8
from django.test import TestCase


class MettingDetailTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/some-meeting/')

    def test_get(self):
        """
        GET / must return status code 200.
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Home must use template index.html
        """
        self.assertTemplateUsed(self.resp, 'core/meeting_detail.html')
