import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

REQ_FILE = os.path.join(os.path.dirname(__file__), 'requirements.txt')
INIT_FILE = os.path.join(os.path.dirname(__file__),
                         'src/PackageName/__init__.py')

def required_pkgs():
    # Pull required packages from the requirements.txt file
    with open(REQ_FILE) as rfile:
        return rfile.read().strip().split('\n')

def current_version():
    with open(INIT_FILE) as f:
        return re.search(r"__version__\s*=\s*['\"]([\d.]+)['\"]",
                         f.read()).groups()[0]

def license():
    with open(INIT_FILE) as f:
        return re.search(r"__license__\s*=\s*['\"]([\w. ]+)['\"]",
                         f.read()).groups()[0]

def author():
    with open(INIT_FILE) as f:
        return re.search(r"__author__\s*=\s*['\"]([\w. ]+)['\"]",
                         f.read()).groups()[0]


kwargs = {
    'name': 'PackageName',
    'packages': ['PackageName'],
    'package_dir': {'': 'src'},
    'version': current_version(),
    'author': author(),
    'install_requires': required_pkgs(),
    'license': license(),
}

setup(**kwargs)
