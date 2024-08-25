import pandas as pd
import numpy as np

def static_hedge(portfolio, fx_data, hedge_ratio=0.5):
    """ Apply a static hedge strategy where a fixed percentage of the exposure is hedged. """
    hedged_portfolio = portfolio.copy()
    hedged_portfolio['hedged_value'] = hedged_portfolio['value'] * (1 - hedge_ratio + hedge_ratio * fx_data['close'].mean())
    return hedged_portfolio

def dynamic_hedge(portfolio, fx_data, threshold=0.02):
    """ Apply a dynamic hedge strategy that adjusts based on FX volatility or other factors. """
    hedged_portfolio = portfolio.copy()
    volatility = fx_data['close'].pct_change().std()
    
    if volatility > threshold:
        hedge_ratio = 0.75  # More aggressive hedging during high volatility
    else:
        hedge_ratio = 0.25  # Less aggressive hedging during low volatility

    hedged_portfolio['hedged_value'] = hedged_portfolio['value'] * (1 - hedge_ratio + hedge_ratio * fx_data['close'].mean())
    return hedged_portfolio

def no_hedge(portfolio, fx_data):
    """ Portfolio value without hedging. """
    unhedged_portfolio = portfolio.copy()
    unhedged_portfolio['unhedged_value'] = unhedged_portfolio['value'] * fx_data['close'].mean()
    return unhedged_portfolio

def run_hedging_simulation(portfolio_path, fx_data_path, results_path='results/hedging_results.csv'):
    portfolio = pd.read_csv(portfolio_path)
    fx_data = pd.read_csv(fx_data_path, index_col='date', parse_dates=True)

    # Simulating different strategies
    static_result = static_hedge(portfolio, fx_data)
    dynamic_result = dynamic_hedge(portfolio, fx_data)
    unhedged_result = no_hedge(portfolio, fx_data)

    # Combining results
    combined_results = pd.DataFrame({
        'static_hedged_value': static_result['hedged_value'],
        'dynamic_hedged_value': dynamic_result['hedged_value'],
        'unhedged_value': unhedged_result['unhedged_value']
    })
    
    combined_results.to_csv(results_path)
    print(f"Hedging results saved to {results_path}")

# Example usage
if __name__ == "__main__":
    run_hedging_simulation('data/portfolio_data.csv', 'data/processed_data/USD_GBP.csv')