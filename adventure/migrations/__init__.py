import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

  initial = True

  dependencies = [
    migrations.swappable_dependency(settings.AUTH_USER_MODEL),
  ]

  operations = [
    migrations.CreateModel(
      name='Items',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'))
      ],
    ),

    migrations.CreateModel(
      name='Player',
      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('username', models.CharField(max_length=30)),
        ('currentRoom', models.IntegerField(default=0)),
        ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
        ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
      ],
    ),

    migrations.CreateModel(
        name='Maps',
        fields=[
            ('id', models.AutoField(auto_created=True, primar_key=True, serialize=False, verbose_name='ID')),
            ('player_id', models.Intege)
        ],
  ]
