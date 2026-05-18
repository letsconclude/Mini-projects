The command to pack code into a wheel file 

myproject/
 ├── mypackage/
 │   └── __init__.py
 ├── pyproject.toml
 └── README.md

sudo apt install python3 -y
git clone https://github.com/pypa/sampleproject.git
sudo apt install -y python3-venv
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install build setuptools wheel
python -m build --wheel
