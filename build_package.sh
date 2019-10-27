
THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

python setup.py clean --all
rm -rf $THIS_DIR/dist
python setup.py sdist bdist_wheel
