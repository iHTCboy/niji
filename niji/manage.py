# import os, sys
# os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
# current_dir = os.path.dirname(__file__)
# sys.path.insert(0, current_dir)
#
# from django.test.utils import get_runner
# from django.conf import settings
#
# import django
# django.setup()
#
# from celery import Celery
# app = Celery('project_name')
#
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
#
# def runtests():
#     TestRunner = get_runner(settings)
#     test_runner = TestRunner(verbosity=1, interactive=True)
#     failures = test_runner.run_tests(['niji'])
#     sys.exit(bool(failures))


# if __name__ == "__main__":
#     runtests()
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
