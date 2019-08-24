import os
import sys
import pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


if __name__ == '__main__':
    pytest.main(["-s", "--alluredir=report/xml", "tests/"])