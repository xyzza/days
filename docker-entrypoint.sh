#!/usr/bin/env sh

set -e

case "$1" in
    api-dev)
        exec python manage.py runserver 0.0.0.0:8000
        ;;
    tests)
        exec pytest tests
        ;;
    coverage)
        echo "running tests..."
        coverage run -m pytest -v -s tests
        echo "coverage report..."
        coverage report
        ;;
    analyze)
        echo "flake8..."
        flake8 days_project tests
        echo "mypy..."
        mypy days_project tests --show-error-codes --ignore-missing-imports
        echo "isort..."
        isort --check-only --diff days_project tests
        echo "black..."
        black --check days_project tests
        ;;
    makemigration)
        shift
        exec python manage.py makemigration "$@"
        ;;
    migrate)
        shift
        exec python manage.py migrate "$@"
        ;;
    downgrade)
        shift
        exec python manage.py migrate "$@" zero
        ;;
    format)
        echo "pautoflake..."
        pautoflake -r days_project tests
        echo "isort..."
        isort days_project tests
        echo "black..."
        black days_project tests
        ;;
    *)
        exec "$@"
esac
