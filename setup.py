import setuptools

# PRODUCTION setup.py: name, version, install_requires, packages only
with open('requirements.txt', encoding="utf-8") as file:
    install_requires = file.read().splitlines()
setuptools.setup(
    name='django-urls-templateview',
    version='1.0.2',
    install_requires=install_requires,
    packages=setuptools.find_packages()
)
