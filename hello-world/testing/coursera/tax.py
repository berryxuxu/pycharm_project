def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    fv = present_value * (1+rate_per_period)**periods
    return fv

    # Put your code here.
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

for i in range(5, -1, -1):
    print i

lis1 = [1,2,3]
lis2 = [1,2,3]
print lis1 == lis2