import os
import sys
import pytest
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

if __name__ == '__main__':
    pytest.main(["-s", "--alluredir=report/xml", "tests/"])