from abc import ABCMeta, abstractmethod
from datetime import date
from typing import Awaitable, Dict, List

import pandas as pd

from liualgotrader.common.types import TimeScale


class DataAPI(metaclass=ABCMeta):
    def __init__(self, ws_uri: str, ws_messges_handler: Awaitable):
        self.ws_uri = ws_uri
        self.ws_msgs_handler = ws_messges_handler

    @abstractmethod
    def get_symbol_data(
        self,
        symbol: str,
        start: date,
        end: date = date.today(),
        scale: TimeScale = TimeScale.minute,
    ) -> pd.DataFrame:
        ...

    @abstractmethod
    def get_symbols(self) -> List[Dict]:
        ...

    @abstractmethod
    def get_symbols_data(
        self,
        symbols: List[str],
        start: date,
        end: date = date.today(),
        scale: TimeScale = TimeScale.minute,
    ) -> Dict[str, pd.DataFrame]:
        ...
