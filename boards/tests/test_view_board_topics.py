from django.urls import resolve, reverse
from django.test import TestCase
from ..views import board_topics
from ..models import Board

# Create your tests here.
class BoardTopicsTests(TestCase):
    def setUp(self):
        board = Board.objects.create(name='Django', description='Django board.')
        # print(board.id)
        self.valid_board_id = board.id
        self.invalid_board_id = board.id + 100

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': self.valid_board_id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': self.invalid_board_id})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/{}/'.format(self.valid_board_id))
        self.assertEquals(view.func, board_topics)

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.valid_board_id})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': self.valid_board_id})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
