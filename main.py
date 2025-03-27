# Runs the program and shows the graph

import matplotlib.pyplot as plt
from simulator import simulate_portfolio
from config import *

def main():
    results, var_95 = simulate_portfolio()
    
    # Draw the graph
    plt.figure(figsize=(10, 6))
    plt.hist(results, bins=50, color='blue', alpha=0.7)
    plt.axvline(var_95, color='red', linestyle='dashed', linewidth=2, label='95% Worst Case')
    plt.axvline(INITIAL_MONEY, color='green', linestyle='dashed', linewidth=2, label='Starting Money')
    plt.title('Possible Future Values of Your Money')
    plt.xlabel('Final Amount ($)')
    plt.ylabel('Number of Simulations')
    plt.legend()
    plt.show()
    
    print(f"Starting money: ${INITIAL_MONEY:,.2f}")
    print(f"After {YEARS} years, in 95% of cases, you won't lose more than: ${INITIAL_MONEY - var_95:,.2f}")

if __name__ == "__main__":
    main()