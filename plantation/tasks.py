# your_app/tasks.py
import time
from celery import shared_task
import random


@shared_task
def degrade_health(model_class, min_minutes, max_minutes):
    HEALTH_CHOICES = [
        choice[0] for choice in model_class._meta.get_field("health").choices
    ]

    instances = model_class.objects.all()
    for instance in instances:
        current_health = instance.health
        current_index = HEALTH_CHOICES.index(current_health)
        new_index = min(len(HEALTH_CHOICES) - 1, current_index + 1)
        instance.health = HEALTH_CHOICES[new_index]
        instance.save()

        print("Health of plant " + instance.species + " is now " + instance.health)
        sleep_time = random.randint(min_minutes * 60, max_minutes * 60)
        time.sleep(sleep_time)
