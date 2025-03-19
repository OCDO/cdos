from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='cdos',
    author='Abril Azocar Guzman',
    author_email='a.azocar.guzman@fz-juelich.de',
    description='CDOS - Crystallographic Defect Ontology Suite',
    long_description=readme,
    long_description_content_type='text/markdown',
    download_url = 'https://github.com/ocdo/cdos',
)
