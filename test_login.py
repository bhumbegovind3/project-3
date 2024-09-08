def test_username():
    print('this is  username')

def test_password():
    print('this is password')

# op

# ============================= test session starts =============================
# collecting ... collected 2 items
#
# test_login.py::test_username PASSED                                      [ 50%]this is  username
#
# test_login.py::test_password PASSED                                      [100%]this is password
#
#
# ============================== 2 passed in 0.02s ==============================


# #################   terminal and cmd output   ########

#   C:\Users\HP\PycharmProjects\PythonProject2_Sele>python -m pytest   ## this is the comand  = python -m pytest

# ============================== test session starts ==============================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# collected 3 items
#
# test_login.py ..                                                           [ 66%]
# test_signup.py .                                                           [100%]
#
# =============================== 3 passed in 0.05s ===============================

################  -k   ###################################

#
# C:\Users\HP\PycharmProjects\PythonProject2_Sele>python -m pytest .\test_login.py -k test_username  (## this comand == python -m pytest .\test_login.py -k test_username
# give all the detail information of test cses
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# collected 2 items / 1 deselected / 1 selected
#
# test_login.py .                                                                                                                                                  [100%]
#
# =================================================================== 1 passed, 1 deselected in 0.01s ===================================================================

################    -v   #################################
 
#
# C:\Users\HP\PycharmProjects\PythonProject2_Sele> python -m pytest -v .\test_login.py   (#this is the comand = python -m pytest -v .\test_login.py
# give mi which are pass anf which are fail

# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0 -- C:\Users\HP\AppData\Local\Programs\Python\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# collected 2 items
#
# test_login.py::test_username PASSED                                                                                                                              [ 50%]
# test_login.py::test_password PASSED                                                                                                                              [100%]
#
# ========================================================================== 2 passed in 0.03s ==========================================================================

###############   -sv    ####################################
# give all detail and which are pass and which are fail
# C:\Users\HP\PycharmProjects\PythonProject2_Sele> python -m pytest -sv .\test_login.py
# ========================================================================= test session starts =========================================================================
# platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0 -- C:\Users\HP\AppData\Local\Programs\Python\Python312\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\HP\PycharmProjects\PythonProject2_Sele
# collected 2 items
#
# test_login.py::test_username this is  username
# PASSED
# test_login.py::test_password this is password
# PASSED
#
# ========================================================================== 2 passed in 0.02s ==========================================================================
