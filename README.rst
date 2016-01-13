similar_text
============

.. image:: https://img.shields.io/pypi/v/similar_text.svg
    :target: https://pypi.python.org/pypi/similar_text


:code:`similar_text` can calculate the similarity between two strings

Installation
------------

The tool works with Python 2 and Python 3. It can be installed with `pip` :

::

    pip install similar_text


Usage
-----

.. code-block:: python

    >>> from similar_text import similar_text
    >>> similar_text('luosicheng', 'lsc')
    46
    >>> similar_text('lsc', 'luosicheng')
    46
