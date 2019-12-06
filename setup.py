import os
from setuptools import find_packages, setup
install_requires = [
    'allianceauth',
]
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='allianceauth-corpstats-two',
    version='0.0.0alpha1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    license='GNU General Public License v3 (GPLv3)',
    description='Alliance Auth Plugin',
    long_description=README,
    url='https://github.com/pvyParts/allianceauth-corpstats-two',
    author='ak',
    author_email='ak@ak.auth',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

