from setuptools import setup


setup(
    name='nosespec',
    version = '0.1',
    modules = ['nosespec.py'],
    author = 'Anatoly Kudinov',
    author_email = 'zz@rialabs.org',
    description = 'Spec plugin for nosetests',
    entry_points = {
        'nose.plugins.0.10': [
            'spec = nosespec:SpecPlugin'
            ]
        },
  )
