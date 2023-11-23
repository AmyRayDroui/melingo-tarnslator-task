import csv
from django.core.management.base import BaseCommand
from django.db import models
from translator.models import Entry, Example

def create_model_instance(model_class, data):
    model_instance = model_class()
    for field, value in data.items():
        setattr(model_instance, field, value)
    model_instance.save()
    return model_instance

class Command(BaseCommand):
    help = 'Import data from two CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('entries_csv_file', type=str, help='Path to the Entries CSV file')
        parser.add_argument('examples_csv_file', type=str, help='Path to the Examples CSV file')


    def handle(self, *args, **options):
        entries_file_path = options['entries_csv_file']
        examples_file_path = options['examples_csv_file']
        Example.objects.all().delete()
        Entry.objects.all().delete()
        try: 
            self.import_csv(entries_file_path, Entry)
            self.import_csv(examples_file_path, Example)
        except:
            self.stdout.write('fail')
        else:
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        
    def import_csv(self, csv_file_path, model):
        model_fields = model._meta.get_fields()
        field_names = tuple(field.name for field in model_fields if not field.is_relation)
        
        # get a dict with foreign key as key and foreign model as 
        foreign_keys = {field.name:model._meta.get_field(field.name).related_model for field in model_fields if isinstance(field, models.ForeignKey)}
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                foreign_data = {}
                if foreign_keys:
                    # retrieve foreign object from foreign model 
                    foreign_data = {foreign_key:foreign_keys[foreign_key].objects.get(**{foreign_key:row[foreign_key]}) for foreign_key in foreign_keys.keys() if foreign_keys[foreign_key].objects.filter(**{foreign_key:row[foreign_key]}).exists()}
                    if any(key not in foreign_data for key in foreign_keys.keys()):
                        continue
                main_data = {field: row[field] for field in field_names}
                main_data.update(foreign_data)
                model.objects.create(**main_data)
