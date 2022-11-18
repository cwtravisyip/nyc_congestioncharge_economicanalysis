def run_cba(dis_rate = 0.05, charge = 14, elas = 0.5,avg_dis=17.8,cost_drive = 1.55, time_cost =32.86):
    """
    conduct cost-benefit analysis.
    The function return all the identified cost and benefits in a dictionary
    """
    # determine the percentage change in traffic flow with respect to price
    delta_traffic = elas *charge/(avg_dis*cost_drive) #default set as 0.5*14/(17.8 * 1.55) =0.2537
    delta_mil = delta_traffic * 717000 * 17.8 *260 *2

    # determine the common ratio for perpetual calculation (discount rate)
    cm = 1/(1+dis_rate)
    
    # determine the annual cost and benefit in million
    B_timesaving  = (0.1471 * delta_traffic) * (717000* 260*2) *(4/6)*time_cost  /1000000
    B_reliability = B_timesaving /3
    #CO2
    co2 =  411* delta_mil * (0.033/1000) / 1000000
    #NOx
    nox =   0.00007 *delta_mil * (81/1000) / 1000000
    B_pollution   = (co2 + nox) 

    # accident
    B_accident    = delta_traffic * 0.1513 * 4290

    # cost
    C_operational = 38.9*1.24*3.998 
    C_subsidy     = 95

    # upfront investment
    C_investment  = 200*1.32*1.619 

    # aggregate npv of benefit and cost
    agg_ben = (B_timesaving + B_reliability + B_pollution + B_accident) /  (1-cm)
    agg_cos = (C_operational + C_subsidy) / (1-cm) +C_investment
    BRC = agg_ben / agg_cos
    BRC_dummy = BRC >= 1

    dict = {    'Discount Rate':dis_rate,
                'Charge':charge,
                'Elasticity':elas,
                'B_timesaving':B_timesaving,
                'B_reliability':B_reliability,
                'B_pollution':B_pollution,
                'B_accident':B_accident,
                'C_operational':C_operational,
                'C_investment':C_investment,
                'C_subsidy': C_subsidy,
                'Benefit-Cost Ratio':BRC,
                'Benefit-Cost Ratio - Dummy':BRC_dummy}
    #list =  [[dis_rate,charge,elas,B_timesaving,B_reliability,B_pollution,B_accident,C_operational,C_investment,C_subsidy, BRC]]
    
    return dict
                