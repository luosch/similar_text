similar_text
============

.. image:: https://img.shields.io/pypi/v/similar_text.svg
    :target: https://pypi.python.org/pypi/similar_text

.. image:: https://img.shields.io/pypi/dm/similar_text.svg
        :target: https://pypi.python.org/pypi/similar_text.svg

:code:`similar_text` can calculate the similarity between two strings

Installation
------------

To install similar_text, simply:

.. code-block:: bash

    $ pip install similat_text


Usage
-----

.. code-block:: python

    >>> from similar_text import similar_text
    >>> similar_text('luosicheng', 'lsc')
    46
    >>> similar_text('lsc', 'luosicheng')
    46
