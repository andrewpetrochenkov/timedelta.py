import setuptools

setuptools.setup(
    name='timedelta',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
