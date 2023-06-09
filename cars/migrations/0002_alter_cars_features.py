# Generated by Django 4.2.1 on 2023-05-22 18:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Bluetooth Connectivity', 'Bluetooth Connectivity'), ('Backup Camera', 'Backup Camera'), ('Navigation System', 'Navigation System'), ('Keyless Entry', 'Keyless Entry'), ('Leather Seats', 'Leather Seats'), ('Heated Seats', 'Heated Seats'), ('Sunroof/Moonroof', 'Sunroof/Moonroof'), ('Parking Sensors', 'Parking Sensors'), ('Emergency Braking', 'Emergency Braking'), ('Apple CarPlay', 'Apple CarPlay'), ('Android Auto', 'Android Auto'), ('Wireless Charging', 'Wireless Charging'), ('Dual-zone Climate Control', 'Dual-zone Climate Control'), ('USB Ports', 'USB Ports')], max_length=259),
        ),
    ]
