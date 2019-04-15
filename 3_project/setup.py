from setuptools import setup

setup(
    name='project',
    version='0.1',
    py_modules=['project'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        project=project:main
    ''',
)