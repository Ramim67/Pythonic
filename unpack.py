'''
def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

#coins = [100, 50, 25]
coins = {"galleons": 100, "sickles": 50, "knuts":25}
#print(total(galleons=100, sickles=50, knuts=25), "knuts")
#print(total(*coins), "knuts")

#print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
print(total(**coins), "knuts")
'''

def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)

