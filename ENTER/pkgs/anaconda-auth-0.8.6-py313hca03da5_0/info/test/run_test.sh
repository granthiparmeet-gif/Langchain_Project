

set -ex



pip check
python -c "from anaconda_auth import __version__; assert __version__ == '0.8.6'"
exit 0
