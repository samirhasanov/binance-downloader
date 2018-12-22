Binance Downloader
==================

Python tool to download Binance Candlestick (k-line) data from REST API

Parallel Downloads (dev branch): [![Build Status](https://travis-ci.com/anson-vandoren/binance-downloader.svg?branch=parallel_downloads)](https://travis-ci.com/anson-vandoren/binance-downloader)

Instalation
-----------

### LINUX
- clone repository
```console
$ git clone https://github.com/bullsignals/binance-downloader.git
$ cd binance-downloader
```
- activate your virtual enviroment and install dependencies (using python >= 3.5). If you don't know about virtual environments see   https://github.com/anderson89marques/about_python/blob/master/virtualenv.md

```console
$ source /path-to-virtual-env/bin/activate
$ pip install -r requirements.txt
$ flit install --symlink --python python
```

### WINDOWS

- clone repository
```console
$ git clone https://github.com/bullsignals/binance-downloader.git
$ cd binance-downloader
```
- activate your virtual enviroment and install dependencies (using python >= 3.5). If you don't know about virtual environments see   https://github.com/anderson89marques/about_python/blob/master/virtualenv.md

```console
$ source /path-to-virtual-env/bin/activate
$ pip install -r requirements.txt
``` 

To execute  ```'flit install --symlink --python python'``` you need run command prompt as admin. 
You can do that by:
> Go to start -> All Programs -> Acessories -> Right click on Command Prompt and
> select "Run as administrator"

Then go to project directory, activate you virtual environment e execute the command.
```console
$ flit install --symlink --python python
```
Now you can run the kline-binance command line. You don't need execute the command prompt as admin before do that.

Using binance downloader cli
-----------------------------

- Help
```console
$ kline-binance -h

usage: binance [-h] --interval INTERVAL [--symbol SYMBOL] [--limit LIMIT]
               [--start START] [--end END] [--output OUTPUT]

Python tool to download Binance Candlestick (k-line) data from REST API

optional arguments:
  -h, --help            show this help message and exit
  --interval INTERVAL, -i INTERVAL
                        frequence interval in minutes(m); hours(h); days(d);
                        weeks(w); months(M); all possibles values: 1m 3m 5m
                        15m 30m 1h 2h 4h 6h 8h 12h 1d 3d 1w 1M
  --symbol SYMBOL, -s SYMBOL
                        pair. default: 'ETHBTC'.
  --limit LIMIT, -l LIMIT
                        quantity of items downloaded;
  --start START, -st START
                        start period to get data. format: dd/mm/yy
  --end END, -e END     start period to get data. format: dd/mm/yy
  --output OUTPUT, -o OUTPUT
                        File Name. default: binance. 
```

- Downloading data
```console
$ kline-binance -i 1m -l 1500 -st 01/01/2016 -e 05/04/2018
```

License
-------
This code is under MIT License. See LICENSE file for detail.
