

set -ex



pip check
python -m unittest discover --buffer -s=tests
exit 0
