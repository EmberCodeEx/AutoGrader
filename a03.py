### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget, bashir_budget):
    small_budget = 0
    if ali_budget > bashir_budget:
        small_budget = bashir_budget
    else:
        small_budget = ali_budget
    
    for i in range(1, small_budget+1):
        if((ali_budget % i == 0) and (bashir_budget % i == 0)):
            hcf = i 
    return hcf

#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget, bashir_budget):
    if type(ali_budget) == float or type(bashir_budget) == float:
        if type(ali_budget) == int or type(bashir_budget) == int:
            ali_budget = (int(10*ali_budget-0.5)+1) / 10.0
            bashir_budget = (int(10*bashir_budget-0.5)+1) / 10.0
            small_budget = 0
            large_budget = 0
            if ali_budget > bashir_budget:
                small_budget = bashir_budget
                large_budget = ali_budget
            else:
                small_budget = ali_budget
                large_budget = bashir_budget
        
            large_budget_sales = large_budget * 3 / 2
            small_budget_sales = small_budget * 2
            large_budget_profit = large_budget_sales - large_budget
            small_budget_profit = small_budget_sales - small_budget
            if large_budget_profit > small_budget_profit:
                return int(large_budget_profit)
            else:
                return int(small_budget_profit)
        else:
            return "Not Possible"
    else:
        return "Not Possible"

#### End OF MARKER


