import os
from . import models
from . import obs
from . import sps
from . import utils
import parrotpy
emul_loc =  os.path.join(parrotpy.__path__[0], '..', 'data',)