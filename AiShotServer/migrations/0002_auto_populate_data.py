# AiShotServer/migrations/0002_auto_populate_data.py
#python manage.py makemigrations --empty AiShotServer
from django.db import migrations

def populate_data(apps, schema_editor):
    Movie = apps.get_model('AiShotServer', 'Movie')
    Movie.objects.create(
        title="Avatar",
        overview="A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        release_date="2009-12-18",
        poster_path="/images/path/to/avatar.jpg",
        adult=False,
        original_language="en",
        original_title="Avatar",
        genre_ids=[12, 14, 28],
        backdrop_path="/images/path/to/avatar_backdrop.jpg",
        popularity=89.2,
        vote_count=19000,
        video=False,
        vote_average=7.8
    )

class Migration(migrations.Migration):
    dependencies = [
        ('AiShotServer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_data),
    ]