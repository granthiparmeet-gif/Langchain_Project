

set -ex



pip check
pytest -k 'not (test_failures or test_failure_after_loading_additional_anchors)' tests/
exit 0
