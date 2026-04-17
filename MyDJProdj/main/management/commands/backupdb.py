# main/management/commands/backupdb.py
import os
import shutil
import datetime
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создаёт резервную копию базы данных и удаляет старые бэкапы"

    def handle(self, *args, **kwargs):
        db_path = settings.DATABASES["default"]["NAME"]
        backup_dir = os.path.join(settings.BASE_DIR, "backups")
        os.makedirs(backup_dir, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        backup_file = os.path.join(backup_dir, f"db_{timestamp}.sqlite3")

        shutil.copy(db_path, backup_file)

        # Удаляем старые бэкапы (старше 7 дней)
        now = datetime.datetime.now()
        for filename in os.listdir(backup_dir):
            if filename.startswith("db_") and filename.endswith(".sqlite3"):
                full_path = os.path.join(backup_dir, filename)
                file_time = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
                if (now - file_time).days > 7:
                    os.remove(full_path)

        self.stdout.write(self.style.SUCCESS(f"Бэкап создан: {backup_file}"))
