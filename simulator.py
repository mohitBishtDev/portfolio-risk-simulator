# Does the math and simulations

import numpy as np
from config import *

def simulate_portfolio():
    results = []
    
    for _ in range(NUM_SIMULATIONS):
        current_money = INITIAL_MONEY
        
        for year in range(YEARS):
            # Random returns for each investment
            returns = np.random.normal(MEAN_RETURNS, VOLATILITIES)
            # Mix them based on weights
            portfolio_return = np.dot(WEIGHTS, returns)
            # Update money
            current_money *= (1 + portfolio_return)
        
        results.append(current_money)
    
    results.sort()
    var_95 = results[int(0.05 * NUM_SIMULATIONS)]
    
    return results, var_95