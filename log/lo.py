import sys
# 更換
package_path = r".\python-3.11.1\Lib\site-packages"
if package_path not in sys.path:
    sys.path.append(package_path)
import numpy as np
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# import logging

# logging.warning('%s before you %s', 'Look', 'leap!')

from loguru import logger
logger.debug("That's it, beautiful and simple logging!")