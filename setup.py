try:
    from setuptools import setup
except:
    from distutils.core import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name = 'similar_text',
    packages = ['source'],
    version = '0.1',
    description = 'Calculates the similarity between two strings',
    long_description = readme,
    author = 'Sicheng Luo',
    author_email = 'i@lsich.com',
    url = 'https://github.com/luosch/similar_text',
    keywords = ['similar_text', 'similar', 'text'],
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ]
)