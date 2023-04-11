import os
import sys
from exceptions import CustomException
from logger import logging

from dataclasses import dataclass
import pandas as pd
import sqlalchemy


@dataclass
class DataLoaderConfig():
    sql_engine:str = ''
    raw_data_path:str = ''
    sql:str


class DataLoader:

    def __init__(self):
        self.config = DataLoaderConfig()
