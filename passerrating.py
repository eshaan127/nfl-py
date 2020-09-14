# Made by Eshaan Kumar on 9/13/2020
# Last updated 9/13/2020 by Eshaan Kumar

# Get user inputs
att_var = int(input("Number of passing attempts: "))
comp_var = int(input("Number of completions: "))
yd_var = int(input("Passing yards: "))
td_var = int(input("Touchdown passes: "))
int_var = int(input("Interceptions: "))
tdoveratt_var = td_var/att_var
ydsperatt_var = yd_var / att_var
comppercent = comp_var/att_var

# NFL/CFL function
def nfl():
    '''passer rating for nfl or cfl quarterbacks'''
    var_a = (comp_var/att_var - 0.3) * 5
    if var_a < 0:
        var_a = 0
    if var_a > 2.375:
        var_a = 2.375
    var_b = (yd_var/att_var - 3) * 0.25
    if var_b < 0:
        var_b = 0
    if var_b > 2.375:
        var_b = 2.375
    var_c = (td_var/att_var) * 20
    if var_c < 0:
        var_c = 0
    if var_c > 2.375:
        var_c = 2.375
    var_d = 2.375 - ((int_var/att_var) * 25)
    if var_d < 0:
        var_d = 0
    if var_d > 2.375:
        var_d = 2.375
    passerrating = ((var_a + var_b + var_c + var_d)/6) * 100
    if passerrating == 158.3:
        if int_var != 0:
            passerrating = 158.2
        if tdoveratt_var < 1.1875:
            passerrating = 158.2
        if ydsperatt_var < 12.5:
            passerrating = 158.2
        if comppercent < 7.75:
            passerrating = 158.2
    return passerrating
    if passerrating == 158.3:
        return "PERFECT PASSER RATING NO WAY GJ"

print(nfl())


