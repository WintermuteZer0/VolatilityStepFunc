import volatility.plugins.common as common
import volatility.utils as utils
import volatility.win32 as win32
from volatility.renderers.basic import Address


def lambda_handler(event,context):
    #TODO - Fill process list info processing code
    # 1 - Ensure output is written to file and S3 bucket

    def calculate(self):
        addr_space = utils.load_as(self._config)
        procs = win32.tasks.pslist(addr_space)
        return procs
