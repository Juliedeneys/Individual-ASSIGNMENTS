
#%%
from Ses11ex import checkout_white

def testvalues():
    assert checkout_white(["Guitar"]) == 1000
    assert checkout_white(["Guitar","Guitar Strings","Guitar Strings","Guitar"]) == 1020
    assert checkout_white(['Guitar','Guitar', 'Pick box']) == 2005
    assert checkout_white([]) == 'Your shopping cart is empty.'
    
from Ses11ex import checkout_blue

def testvalues2():
    assert checkout_blue(["Guitar","Guitar Strings","Guitar Strings","Guitar"]) == 1020
    assert checkout_blue([]) == 'Your shopping cart is empty.'
    assert checkout_blue(["Pick Box", "Guitar","Insurance","Insurance", "Priority mail", "Priority mail"])

from Ses11ex import checkout_black

def testvalues3():
    assert checkout_black(["Guitar", "Insurance"], 'silver') == 985
    assert checkout_black(["Guitar", "Insurance"], 'gold') == 954.75
    assert checkout_black(["Guitar", "Insurance"], 'normal') == 1005
    