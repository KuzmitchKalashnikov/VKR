#!/usr/bin/env python
"
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('FLASK_SETTINGS_MODULE', 'plant_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import flask. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
