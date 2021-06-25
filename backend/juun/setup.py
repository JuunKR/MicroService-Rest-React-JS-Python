from setuptools import setup, find_packages


setup_requires = [
    ]




install_requires = [
    'django==3.2.4',
    ]




dependency_links = [
    'git+https://github.com/django/django.git@stable/1.6.x#egg=Django-1.6b4',
    ]




setup(
    name='Root App',
    version='0.1',
    description='Root App',
    author='root',
    author_email='root@root.com',
    packages=find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    dependency_links=dependency_links,
    scripts=['manage.py'],
    entry_points={
        'console_scripts': [
            'publish = juun.common.script:main',
            'publish = juun.crime.script:main',
            'publish = juun.gas_station.script:main',
            ],
        },
    )