# coding: utf-8
from django.test import TestCase


class MeetingDetailTest(TestCase):
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

    def test_html(self):
        html = (
            # Meeting
            'Meeting Title',
            '/media/meeting-banner.jpg',
            'Meeting headline.',
            'http://player.vimeo.com/video/1',
            'About the meeting.',
            # Host
            ('Host', 2),
            '/media/host-picture.jpg',
            '/users/1-host',
            'About the host.',
            # More on meeting
            'R$ 30,00',
            'Quarta, 11 de Dezembro de 2013 das 19h às 22h.',
            'Meeting address.',
            # Organizer
            '/media/organizer-picture.jpg',
            '/users/2-organizer/',
            'Organizer',
            # Guests
            '/users/3-guest/',
            '/media/guest-picture.jpg',
            'Guest',
        )
        self.assertContainsMany(self.resp, html)

    def assertContainsMany(self, response, iterable):
        for item in iterable:
            if isinstance(item, tuple):
                text, count = item
            else:
                text, count = item, 1
            self.assertContains(response, text, count)
