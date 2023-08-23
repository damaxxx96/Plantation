# your_app/cron.py
from django_cron import CronJobBase, Schedule
from plant.models import Plant
from tree.models import Tree
from tasks import degrade_health


class DegradePlantHealthCronJob(CronJobBase):
    RUN_AT_TIMES = ["02:00"]  # Specify the time when the job should run
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "your_app.degrade_plant_health_cron_job"  # Unique identifier

    def do(self):
        degrade_health(Plant, 1, 2)


class DegradeTreeHealthCronJob(CronJobBase):
    RUN_AT_TIMES = ["03:00"]  # Specify the time when the job should run
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = "your_app.degrade_tree_health_cron_job"  # Unique identifier

    def do(self):
        degrade_health(Tree, 2, 3)
