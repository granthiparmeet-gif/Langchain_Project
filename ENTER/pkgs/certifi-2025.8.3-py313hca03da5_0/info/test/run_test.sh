

set -ex



pip check
python -c "from importlib.metadata import version; assert(version('certifi')=='2025.8.3')"
pytest -vv certifi/certifi/tests
exit 0
