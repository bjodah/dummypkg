dummypkg
========

Using ``pytest --pyargs pythonpackagename`` under a ``conda`` environment does not work.
This is a minimal example for reproducing this bug.


Steps to reproduce
------------------
Only ``dummypkg`` is downloaded from bjodah channel, rest from ``defaults``

::

   $ conda create -c bjodah -n dummy2 python=2.7 dummypkg pytest
   $ source activate dummy2
   $ python -m pytest --pyargs dummypkg
   ================================================================================================ test session starts ================================================================================================
   platform linux2 -- Python 2.7.11, pytest-2.8.5, py-1.4.31, pluggy-0.3.1
   rootdir: /home/chempy, inifile: 
   
   =========================================================================================== no tests ran in 0.00 seconds ============================================================================================
   ERROR: file or package not found: dummypkg

the same goes for python3.4. The weird thing is that the package is importable:

::

   $ which python
   /home/chempy/miniconda2/envs/dummy3/bin/python
   $ python -c "import dummypkg; print(dummypkg.__file__); from dummypkg.tests.test_core import test_f; test_f(); import pytest; print(pytest.__version__, pytest.__file__); pytest.main(['--pyargs', 'dummypkg'])"
   /home/chempy/miniconda2/envs/dummy3/lib/python3.4/site-packages/dummypkg-0.1.0-py3.4.egg/dummypkg/__init__.py
   2.8.5 /home/chempy/miniconda2/envs/dummy3/lib/python3.4/site-packages/pytest.py
   ================================================================================================ test session starts ================================================================================================
   platform linux -- Python 3.4.4, pytest-2.8.5, py-1.4.31, pluggy-0.3.1
   rootdir: /home/chempy, inifile: 
   
   =========================================================================================== no tests ran in 0.00 seconds ============================================================================================
   ERROR: file or package not found: dummypkg


deactivating our environment and using system provided python (Ubuntu 14.04) and `pip` everything works fine:

::

   $ source deactivate
   discarding /home/chempy/miniconda2/envs/dummy3/bin from PATH
   $ export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
   $ which python
   /usr/bin/python
   $ python -m pip install --upgrade --user pytest git+https://github.com/bjodah/dummypkg.git
   $ python -m pytest --pyargs dummypkg
   ================================================================================================ test session starts ================================================================================================
   platform linux2 -- Python 2.7.6, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
   rootdir: /home/chempy, inifile: 
   plugins: cov-1.8.0
   collected 1 items 
   
   .local/lib/python2.7/site-packages/dummypkg/tests/test_core.py .
   
   ============================================================================================= 1 passed in 0.00 seconds ==============================================================================================


(I've tried with pytest 2.6.2 & 2.8.5 as well and it works)

::

   $ python -c "import dummypkg; print(dummypkg.__file__); from dummypkg.tests.test_core import test_f; test_f(); import pytest; print(pytest.__version__, pytest.__file__); pytest.main(['--pyargs', 'dummypkg'])"
   /home/chempy/.local/lib/python2.7/site-packages/dummypkg/__init__.pyc
   ('2.8.7', '/home/chempy/.local/lib/python2.7/site-packages/pytest.pyc')
   ================================================================================================ test session starts ================================================================================================
   platform linux2 -- Python 2.7.6, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
   rootdir: /home/chempy, inifile: 
   plugins: cov-1.8.0
   collected 1 items 
   
   .local/lib/python2.7/site-packages/dummypkg/tests/test_core.py .
   
   ============================================================================================= 1 passed in 0.00 seconds ==============================================================================================
