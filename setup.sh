VERSION=13.1.0

if [ ! -f pyenv/bin/activate ]; then
    # create a virtualenv
    curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-$VERSION.tar.gz
    tar xzf virtualenv-$VERSION.tar.gz
    python virtualenv-$VERSION/virtualenv.py --python=python3.4 pyenv
    rm -f -r virtualenv-$VERSION/
    rm -f -r virtualenv-$VERSION.tar.gz
fi

source pyenv/bin/activate

pip install -r requirements.txt > requirements.log

export PYTHONPATH=${PWD}:${PYTHONPATH}
