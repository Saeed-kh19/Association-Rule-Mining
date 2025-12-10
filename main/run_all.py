from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.BLUE + "Step 1: Loading dataset")
import loading

print(Fore.BLUE + "Step 2: Checking invalid records")
import invalid_records

print(Fore.BLUE + "Step 3: Datatype conversion")
import datatype_conversion

print(Fore.BLUE + "Step 4: Handling missing values")
import missing

print(Fore.BLUE + "Step 5: Feature engineering")
import feature_engineering

print(Fore.BLUE + "Step 6: Preparing baskets")
import prepare_baskets

print(Fore.BLUE + "Step 7: Association EDA")
import eda_association

print(Fore.BLUE + "Step 8: Time series preparation")
import prepare_timeseries

print(Fore.BLUE + "Step 9: Time series EDA")
import eda_timeseries

print(Fore.BLUE + "Step 10: Running Apriori algorithm")
import run_apriori

print(Fore.BLUE + "Step 11: Running Time Series Forecasting")
import run_timeseries

print(Fore.BLUE + "Step 12: Running 14-Day Forecast")
import run_forecast

print(Fore.BLUE + Style.BRIGHT + "\nAll steps executed successfully!")
