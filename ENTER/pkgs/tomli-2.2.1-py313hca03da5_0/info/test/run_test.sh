

set -ex



pip check
python -c "from importlib.metadata import version; assert(version('tomli')=='2.2.1')"
exit 0
