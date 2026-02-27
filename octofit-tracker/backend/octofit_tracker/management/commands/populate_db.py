from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        Activity.objects.all().delete()
        UserProfile.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        tony = UserProfile.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = UserProfile.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = UserProfile.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = UserProfile.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Crear actividades
        Activity.objects.create(user=tony, type='Correr', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, type='Nadar', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce, type='Ciclismo', duration=60, date=timezone.now())
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=timezone.now())

        # Crear workouts
        w1 = Workout.objects.create(name='Entrenamiento Marvel', description='Rutina intensa para héroes Marvel')
        w2 = Workout.objects.create(name='Entrenamiento DC', description='Rutina poderosa para héroes DC')
        w1.suggested_for.add(marvel)
        w2.suggested_for.add(dc)

        # Crear leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=80)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
