# Steps

Steps below.

Important: Ensure that you have your ByBit API Key and Secret up dated on the config_execution_api.py file once downloaded.

## Step 1

Clone the repository

```shell
git clone https://github.com/CryptoWizardsNet/stat-arb-bybit.git statarb
```

Update your API details from ByBit on config_execution_api.py

## Step 2

Change directory

```shell
cd statarb
```

## Step 3

Create Python virtual environment

```shell
pyhton3 -m venv venv
```

Activate environment for Mac

```shell
source venv/bin/activate
```

Activate environment for Windows

```shell
source venv\Scripts\activate
```

## Step 4

Install from requirements.txt

```shell
pip3 install -r requirements.txt
```

or if that does not work, install as follows

```shell
pip3 install pybit==2.4.1 pandas statsmodels
```

## Step 5

Change directory and run a file. E.g.

```shell
cd strategy
```

```shell
python3 main_strategy.py
```

or

```shell
cd execution
```

```shell
python3 main_execution.py
```
