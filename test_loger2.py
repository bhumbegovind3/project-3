
### code will change 1 ####

##########  in pytest use logers #########

import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-%(levelname)s%(message)s')  ## debug and debug ke uppar wale sab level yetil


def test_username():
    logging.info('this is  username')
