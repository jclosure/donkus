try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': 'Joel Holder',
    'url': 'http://github.com/jclosure',
    'download_url': 'Where to download it.',
    'author_email': 'jclosure@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['donkus'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)




