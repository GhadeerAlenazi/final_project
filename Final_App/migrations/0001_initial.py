# Generated by Django 2.2.3 on 2019-07-29 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('clinic', models.CharField(choices=[('Dintistry', 'Dintistry'), ('Pediatrics', 'Pediatrics'), ('Dermatology', 'Dermatology'), ('General Medicine', 'General Medicine'), ('Surgery', 'Surgery'), ('Physical Therapy', 'Physical Therapy'), ('Neurologists', 'Neurologists'), ('Other', 'Other')], default='Other', max_length=7)),
                ('Hospital', models.CharField(choices=[('King Faisal Hospital', 'King Faisal Hospital'), ('King Fahad Hospital', 'King Fahad Hospital'), ('King Khaled Hospital', 'King Khaled Hospital'), ('King Saud Hospital', 'King Saud Hospital')], default='King Saud Hospital', max_length=4)),
                ('phone', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=2)),
                ('City', models.CharField(choices=[('Riyadh', 'Riyadh'), ('Jeddah', 'Jeddah'), ('Dammam', 'Dammam')], default='Riyadh', max_length=3)),
                ('picture', models.ImageField(upload_to='doctors')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='0', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('Fname', models.CharField(max_length=100)),
                ('Lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='users')),
            ],
        ),
    ]