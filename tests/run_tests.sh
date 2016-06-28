TEST_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source "${TEST_DIR}"/../pyenv/bin/activate
python -m pytest "${TEST_DIR}"/tests.py
