# coding: utf-8
from django.db import IntegrityError
from django.test import TestCase
from datetime import datetime
from nosvc.core.models import Meeting


class MeetingModelTest(TestCase):
    def setUp(self):
        self.obj = Meeting.objects.create(
            title='Meeting Title',
            slug='meeting-title',
            headline='Meeting headline.',
            about='About the meeting.',
            location='Meeting address.',
            when='Quarta, 11 de Dezembro de 2013 das 19h às 22h.',
            expiration='2014-01-01'
        )

    def test_create(self):
        self.assertEqual(1, self.obj.pk)

    def test_unicode(self):
        self.assertEqual('Meeting Title', unicode(self.obj))

    def test_timestamps(self):
        self.assertIsInstance(self.obj.created, datetime)
        self.assertIsInstance(self.obj.modified, datetime)

    def test_flags_default_value(self):
        self.assertFalse(self.obj.visible)
        self.assertFalse(self.obj.confirmed)
        self.assertFalse(self.obj.finished)

    def test_slug_is_unique(self):
        obj = Meeting(
            title='Meeting Title',
            slug='meeting-title',
            headline='Meeting headline.',
            about='About the meeting.',
            location='Meeting address.',
            when='Quarta, 11 de Dezembro de 2013 das 19h às 22h.',
            expiration='2014-01-01'
        )
        self.assertRaises(IntegrityError, obj.save)
