"""Command Line Inteface"""
import argparse
from datetime import datetime

from binance.api import BinanceAPI
from binance.db import to_csv
from binance.utils import date_to_timestamp


def main():
    parser = argparse.ArgumentParser(
        description="Python tool to download Binance Candlestick (k-line) data from REST API"
    )
    parser.add_argument('--interval', '-i',
                        help="""frequence interval in minutes(m); hours(h); days(d); weeks(w); months(M);
             all possibles values: 
             1m 3m 5m 15m 30m 1h 2h 4h 6h 8h 12h 1d 3d 1w 1M""", required=True)
    parser.add_argument(
        '--symbol', '-s', help="pair. default: 'ETHBTC'.", default='ETHBTC')
    parser.add_argument(
        '--limit', '-l', help="quantity of items returned; max 500; default 500.")
    parser.add_argument(
        '--start', '-st', help="start period to get data. format: dd/mm/yy")
    parser.add_argument(
        '--end', '-e', help="start period to get data. format: dd/mm/yy")
    parser.add_argument('--output', '-o', help="File Name. default: binance.")

    args = parser.parse_args()
    kwargs = {}

    if args.limit:
        kwargs['limit'] = args.limit

    if args.start and args.end:
        kwargs['startTime'] = date_to_timestamp(args.start)
        kwargs['endTime'] = date_to_timestamp(args.end)

    symbol = args.symbol
    interval = args.interval
    binance = BinanceAPI(interval, symbol, kwargs)
    binance.consult()
    output = args.output if args.output else 'binance'
    to_csv(binance.klines, output)
    print("download finished succesfully.")