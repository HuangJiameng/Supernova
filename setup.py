
from os import path
import setuptools, datetime
from setuptools import find_packages
NAME = "supernova"
today = datetime.date.today().strftime("%b-%d-%Y")
with open(path.join('supernova', '_date.py'), 'w') as fp :
    fp.write('date = \'%s\'' % today)
install_requires=["pytest", "pytest-xdist"]

def setup(scm=None):
    packages = find_packages()

    setuptools.setup(
        name=NAME,
        use_scm_version=scm,
        setup_requires=['setuptools_scm'],
        author="Yuzhi Zhang, Jiameng Huang",
        author_email="huangjm@dp.tech",
        description="Tutorial for Supernova.",
        url="https://github.com/HuangJiameng/Supernova",
        python_requires="~=3.8",
        packages=packages,
        keywords='Supernova',
        install_requires=install_requires,
        entry_points={'console_scripts': ['supernova= supernova.main:main']}
    )
try:
    setup(scm={'write_to': 'supernova/_version.py'})
except:
    setup(scm=None)

