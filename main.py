#!/usr/bin/env python3

from binance import Client
from estimate import estimateNextVolume

client = Client()
coin = 'BTCUSDT'


def fetchKLines(symbol):
    return client.get_historical_klines(
        symbol, Client.KLINE_INTERVAL_1MINUTE, "1 hour ago UTC")


def main():
    klines = fetchKLines(coin)

    # @TODO fix this for the case whem there is only 1 kline
    interval = (klines[1][0] - klines[0][0]) / 1000

    volumes = [float(x[5]) for x in klines]

    avgVolume = estimateNextVolume(volumes)

    print(
        f"Historical data\n\tinterval: {interval} sec\n\tMax volume: {max(volumes)}\n\tMin volume: {min(volumes)}")
    print(f"Estimated volume per sec: {avgVolume / interval}")


if __name__ == "__main__":
    main()
