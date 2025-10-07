

set -ex



pip check
python -c "from importlib.metadata import version; assert(version('jsonpointer')=='3.0.0')"
pytest -vv tests.py
exit 0
