
##########   skip marker ##############
# import logging
# import pytest
# logging.basicConfig(level=logging.DEBUG) ## debug and debug ke uppar wale sab level yetil
#
# def test_add():
#     assert 1+1==2 ## print yeavji logging ##  use print instead of logging
# @pytest.mark.skip
#
# def test_sub():
#     assert 1-1==1

# C:\Users\HP\PycharmProjects\PythonProject2_Sele\test_mark.py
# Testing
# started
# at
# 10: 20
# AM...
# Launching
# pytest
# with arguments C:\
#     Users\HP\PycharmProjects\PythonProject2_Sele\test_mark.py - -no - header - -no - summary - q in C:\Users\HP\PycharmProjects\PythonProject2_Sele
#
# == == == == == == == == == == == == == == = test
# session
# starts == == == == == == == == == == == == == == =
# collecting...collected
# 2
# items
#
# test_mark.py::test_add
# PASSED[50 %]
# test_mark.py::test_sub
# SKIPPED(unconditional
# skip)                      [100 %]
# Skipped: unconditional
# skip
#
# == == == == == == == == == == == == 1
# passed, 1
# skipped in 0.02
# s == == == == == == == == == == == == =
#
# Process
# finished

###########    cmd or termianl  %%%%%%%%%%%#########

# PS C:\Users\HP\PycharmProjects\PythonProject2_Sele> python -m pytest test_mark.py
# ==================================================================== test session starts ====================================================================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# plugins: html-4.0.2, metadata-3.0.0
# collected 2 items
#
# test_mark.py .s                                                                                                                                        [100%]
#
# =============================================================== 1 passed, 1 skipped in 0.01s ================================================================

######################  skip if marker    ####################
#
# import pytest
#
# def test_add():
#     assert 1+1==2      ## print yeavji logging ##  use print instead of logging
#
# @pytest.mark.skipif
#
# def test_sub():
#     assert 1-1==1

#op ==
 ########    cmd    ##################
#
# C:\Users\HP\PycharmProjects\PythonProject2_Sele>python -m pytest test_mark.py
# ================================================= test session starts =================================================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# plugins: html-4.0.2, metadata-3.0.0
# collected 2 items
#
# test_mark.py .s                                                                                                  [100%]
#
# ============================================ 1 passed, 1 skipped in 0.02s =============================================
########################################################################
###################   x fail marker   ##################

# import pytest
#
# def test_add():
#     assert 1+1==2      ## print yeavji logging ##  use print instead of logging
#
# @pytest.mark.xfail
#
# def test_sub():
#     assert 1==1
 #op===   ###########     cmd    ###########
# PS C:\Users\HP\PycharmProjects\PythonProject2_Sele> python -m pytest test
# _mark.py
# ========================= test session starts ==========================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# plugins: html-4.0.2, metadata-3.0.0
# collected 2 items
#
# test_mark.py .X                                                   [100%]
#
# ===================== 1 passed, 1 xpassed in 0.02s =============

#############    custmize marker  ######################################################################
#  run specific set test caseses
import pytest

import pytest
@pytest.mark.set1
def test_add():
    assert 1 + 1 == 2  # Corrected the assertion

def test_sub():
    assert 1 - 1 == 0  # Corrected the assertion

@pytest.mark.set2
def test_mul():
    assert 1 * 1 == 1  # Corrected the assertion

@pytest.mark.set1
def test_div():
    assert 1 / 1 == 1  # Corrected the assertion

@pytest.mark.set2
def test_sum():
    l1 = [1, 2, 3, 4]  # Corrected the list declaration
    sum1 = 0
    for i in l1:
        sum1 = sum1 + i

    assert sum1 == 10
# op    ###########   cmd    ##################### use cmand==   pytest -sv test_mark.py -m set1
# PS C:\Users\HP\PycharmProjects\PythonProject2_Sele> python pytest -sv test_mark.py -m set1  pytest
# C:\Users\HP\AppData\Local\Programs\Python\Python312\python.exe: can't open file 'C:\\Users\\HP\\PycharmProjects\\PythonProject2_Sele\\pytest': [Errno 2] No su
# ch file or directory
# PS C:\Users\HP\PycharmProjects\PythonProject2_Sele> pytest -sv test_mark.py -m set1
# ==================================================================== test session starts ====================================================================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0 -- C:\Users\HP\AppData\Local\Programs\Python\Python312\python.exe
# cachedir: .pytest_cache
# metadata: {'Python': '3.12.0', 'Platform': 'Windows-10-10.0.19045-SP0', 'Packages': {'pytest': '7.4.3', 'pluggy': '1.3.0'}, 'Plugins': {'html': '4.0.2', 'meta
# data': '3.0.0'}}
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# plugins: html-4.0.2, metadata-3.0.0
# collected 5 items / 3 deselected / 2 selected
#
# test_mark.py::test_add PASSED
# test_mark.py::test_div PASSED

# ===================================================================== warnings summary ======================================================================
# test_mark.py:116
#   C:\Users\HP\PycharmProjects\PythonProject2_Sele\test_mark.py:116: PytestUnknownMarkWarning: Unknown pytest.mark.set1 - is this a typo?  You can register cus
# tom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.set1
#
# test_mark.py:123
#   C:\Users\HP\PycharmProjects\PythonProject2_Sele\test_mark.py:123: PytestUnknownMarkWarning: Unknown pytest.mark.set2 - is this a typo?  You can register cus
# tom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.set2
#
# test_mark.py:127
#   C:\Users\HP\PycharmProjects\PythonProject2_Sele\test_mark.py:127: PytestUnknownMarkWarning: Unknown pytest.mark.set1 - is this a typo?  You can register cus
# tom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.set1
#
# test_mark.py:131
#   C:\Users\HP\PycharmProjects\PythonProject2_Sele\test_mark.py:131: PytestUnknownMarkWarning: Unknown pytest.mark.set2 - is this a typo?  You can register cus
# tom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
#     @pytest.mark.set2
#
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
# ======================================================== 2 passed, 3 deselected, 4 warnings in 0.02s ======================================
