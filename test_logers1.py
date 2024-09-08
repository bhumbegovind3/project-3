##########  in pytest use logers #########

import logging
logging.basicConfig(level=logging.DEBUG) ## debug and debug ke uppar wale sab level yetil

def test_login():
    logging.info('enter user name and password')  ## print yeavji logging ##  use print instead of logging

def test_logout():
    logging.critical('logout')
