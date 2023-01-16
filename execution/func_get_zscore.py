# from config_ws_connect import subs_public
# from config_ws_connect import ws_public
from config_execution_api import session_public, ticker_1, ticker_2
from func_calcultions import get_trade_details
from func_price_calls import get_latest_klines
from func_stats import calculate_metrics
import time

# Get latest z-score
def get_latest_zscore():

    # Get latest asset orderbook prices and add dummy price for latest
    # orderbook_1 = ws_public.fetch(subs_public[0]) # Removed as replacing WSS with REST API
    orderbook_1 = session_public.orderbook(symbol=ticker_1)

    # Return structured orderbook 1
    if "ret_msg" in orderbook_1.keys():
        if orderbook_1["ret_msg"] != "OK":
            return
        else:
            orderbook_1 = orderbook_1["result"]

    mid_price_1, _, _, = get_trade_details(orderbook_1)
    time.sleep(0.5) # Using to prevent overwhelming REST API with requests and getting blocked
    # orderbook_2 = ws_public.fetch(subs_public[1]) # Removed as replacing WSS with REST API
    orderbook_2 = session_public.orderbook(symbol=ticker_2)

    # Return structured orderbook 2
    if "ret_msg" in orderbook_2.keys():
        if orderbook_2["ret_msg"] != "OK":
            return
        else:
            orderbook_2 = orderbook_2["result"]

    mid_price_2, _, _, = get_trade_details(orderbook_2)
    time.sleep(0.5) # Using to prevent overwhelming REST API with requests and getting blocked

    # Get latest price history
    series_1, series_2 = get_latest_klines()

    # Get z_score and confirm if hot
    if len(series_1) > 0 and len(series_2) > 0:

        # Replace last kline price with latest orderbook mid price
        series_1 = series_1[:-1]
        series_2 = series_2[:-1]
        series_1.append(mid_price_1)
        series_2.append(mid_price_2)

        # Get latest zscore
        _, zscore_list = calculate_metrics(series_1, series_2)
        zscore = zscore_list[-1]
        if zscore > 0:
            signal_sign_positive = True
        else:
            signal_sign_positive = False

        # Return output
        return (zscore, signal_sign_positive)

    # Return output if not true
    return
