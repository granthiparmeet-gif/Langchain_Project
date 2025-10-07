

set -ex



pip check
pytest tests -vv -k "not (test_set_key_permission_error or test_set_key_unauthorized_file)"
exit 0
