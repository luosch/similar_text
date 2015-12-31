try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name = 'similar_text',
    packages = ['source'],
    version = '0.1',
    description = 'Calculates the similarity between two strings',
    long_description = open('README.md').read()
    author = 'Sicheng Luo',
    author_email = 'i@lsich.com',
    url = 'https://github.com/luosch/similar_text',
    download_url = 'https://github.com/luosch/mypackage/similar_text/0.1',
    keywords = ['similar_text', 'similar', 'text'],
    classifiers = [],
)