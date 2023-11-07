set -euo pipefail

cd src
python transpile_tropo.py
cd $OLDPWD
cd tropoloco
poetry build
pip install dist/*.tar.gz
cd $OLDPWD