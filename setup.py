from setuptools import setup, find_packages

setup(
    name='abadis',
    version='1.0',
    packages=find_packages(),
    license='MIT',
    description='website scraper abadis',
    long_description=open('README.md' , encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    author='dadashzadeh',
    author_email='webdadashzadeh@gmail.com',
    url='https://github.com/dadashzadeh/abadis',
    install_requires=['requests']
)