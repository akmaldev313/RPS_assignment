from setuptools import setup

APP = ['rps.py']
OPTIONS = {
    'argvemulation':True,
}
setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires = ['py2app']
)