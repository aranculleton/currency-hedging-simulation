import pandas as pd
import matplotlib.pyplot as plt

def analyze_portfolio(results_path='results/hedging_results.csv', output_dir='results/visualizations'):
    results = pd.read_csv(results_path)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Calculate key metrics
    metrics = results.describe()
    metrics.to_csv(os.path.join(output_dir, 'hedging_metrics.csv'))
    
    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(results['static_hedged_value'], label='Static Hedge')
    plt.plot(results['dynamic_hedged_value'], label='Dynamic Hedge')
    plt.plot(results['unhedged_value'], label='Unhedged')
    plt.title('Portfolio Value under Different Hedging Strategies')
    plt.xlabel('Time')
    plt.ylabel('Portfolio Value')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, 'hedging_strategy_comparison.png'))
    plt.show()
    print(f"Analysis complete. Results saved to {output_dir}")

# Example usage
if __name__ == "__main__":
    analyze_portfolio()