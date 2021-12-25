import asyncio
from datetime import date, datetime

import pytest

from liualgotrader.common.data_loader import DataLoader  # type: ignore
from liualgotrader.common.database import create_db_connection
from liualgotrader.common.market_data import (get_industries_tickers,
                                              get_market_industries,
                                              get_market_sectors,
                                              get_sectors_tickers,
                                              get_trading_day,
                                              get_trading_holidays,
                                              sp500_historical_constituents)
from liualgotrader.common.types import TimeScale
from liualgotrader.trading.alpaca import AlpacaTrader


@pytest.fixture
def event_loop():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db_connection())
    yield loop
    loop.close()


@pytest.mark.asyncio
@pytest.mark.devtest
async def test_get_market_industries():
    industry_list = await get_market_industries()

    print(industry_list)

    return True


@pytest.mark.asyncio
@pytest.mark.devtest
async def test_get_market_sectors():
    sector_list = await get_market_sectors()
    print(sector_list)

    return True


@pytest.mark.asyncio
@pytest.mark.devtest
async def test_get_market_sectors_symbols():
    sector_list = await get_market_sectors()

    l = await get_sectors_tickers(sector_list)
    print(f"sectors_tickers {l}")

    return True


@pytest.mark.asyncio
@pytest.mark.devtest
async def test_get_market_industries_symbols():
    industries_list = await get_market_industries()
    l = await get_industries_tickers(industries_list)
    print(l)

    return True


@pytest.mark.asyncio
@pytest.mark.devtest
async def test_sp500_historical_constituents():
    sp500_symbols = await sp500_historical_constituents(datetime.today())
    print(sp500_symbols)

    return True


@pytest.mark.asyncio
@pytest.mark.devtest
async def test_get_trading_holidays():
    holidays = await get_trading_holidays()

    print(holidays)

    return True


@pytest.mark.asyncio
@pytest.mark.devtest
async def test_get_trading_day():
    alpaca = AlpacaTrader()
    today = date.today()

    d1 = await get_trading_day(now=today, offset=1)
    print(d1)
    _df = alpaca.get_trading_days(d1, today)

    if len(_df.index) != 1:
        raise AssertionError("expected offset 1")

    d1 = await get_trading_day(now=today, offset=40)
    print(d1)
    _df = alpaca.get_trading_days(d1, today)

    if len(_df.index) != 40:
        raise AssertionError("expected offset 40")

    d1 = await get_trading_day(now=today, offset=100)
    print(d1)
    _df = alpaca.get_trading_days(d1, today)

    if len(_df.index) != 100:
        raise AssertionError("expected offset 100")

    d1 = await get_trading_day(now=today, offset=300)
    print(d1)
    _df = alpaca.get_trading_days(d1, today)

    if len(_df.index) != 300:
        raise AssertionError("expected offset 300")

    d1 = await get_trading_day(now=today, offset=1000)
    print(d1)
    _df = alpaca.get_trading_days(d1, today)
    if len(_df.index) != 1000:
        raise AssertionError("expected offset 1000")

    return True
