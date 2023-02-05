from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cheque_cycle/__init__.py
from cheque_cycle import __version__ as version

setup(
	name="cheque_cycle",
	version=version,
	description="Cheque Cycle",
	author="Brandimic",
	author_email="support@brandimic.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
