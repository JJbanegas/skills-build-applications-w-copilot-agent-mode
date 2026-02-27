from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Test Team'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserProfileTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
    def test_create_user(self):
        url = reverse('userprofile-list')
        data = {'name': 'Test User', 'email': 'test@example.com', 'team_id': self.team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = UserProfile.objects.create(name='Test User', email='test@example.com', team=self.team)
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'user_id': self.user.id, 'type': 'Run', 'duration': 30, 'date': '2026-02-27'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Test Workout', 'description': 'Test Desc', 'suggested_for_ids': [self.team.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
    def test_create_leaderboard(self):
        url = reverse('leaderboard-list')
        data = {'team_id': self.team.id, 'points': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
