from logger import logging
import sys
from exceptions import CustomException

try:
    print(1/0)
except Exception as e:
    print(CustomException(e, sys))
