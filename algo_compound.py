#Algorand reward maximizer calculator

cap_init = float(input('Enter the initial Capital: ')) #Initial ALGO capital in your wallet
FEE = float(input("Enter Algorand transaction fee (i.e 0.001): ")) #Standard Algorand network fee
years = float(input('How many years do you plan to hodl ALGOS? ')) #Remember to Hodl!
APY = 0.01*years*float(input("Enter the current annual yield in % (i.e 6.02): ")) #APY according ALGO rewards calculator
N = 1 #number of times to composite

#We define a function to calculate the final capital after N times
def cap_final(N):
    CF = cap_init*((1+APY/N)**N)-N*FEE
    return CF

#Starting to search the maximum capital for different values of N
while N > 0:
    capfinal = cap_final(N)
    if cap_final(N+1) < capfinal:
        break
    else:
        N=N+1

print('If you don´t compound, you will get ', cap_final(1), 'ALGOS')
print('Best period to composite earnings is each ', years*365/N,'days')
print('Your capital after one year is nearly ', capfinal, ' ALGOS')
print('You can also composite monhtly and get ', cap_final(12.0*years), ' ALGOS')
print('Or even weekly and get ', cap_final(52*years), ' ALGOS')
print('Finally, if you compound daily you will get ', cap_final(365), ' ALGOS')
