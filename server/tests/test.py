import os
import sys

import pytest

if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sys.exit(pytest.main([dir_path, "-W", "ignore::DeprecationWarning"]))
