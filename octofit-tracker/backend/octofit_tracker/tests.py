from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Team A')
        self.assertEqual(team.name, 'Team A')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        activity = Activity.objects.create(user=user, type='run', duration=30, distance=5.0)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)
        self.assertEqual(activity.distance, 5.0)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Cardio', description='Cardio session', duration=45)
        self.assertEqual(workout.name, 'Cardio')
        self.assertEqual(workout.duration, 45)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.user, user)
        self.assertEqual(leaderboard.score, 100)
