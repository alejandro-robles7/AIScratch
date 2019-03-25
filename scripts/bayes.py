from pandas import read_csv

df = read_csv(r'data/playtennis.csv')


def calc(df, colname, attribute, target=1, targetcol= 'Play'):
    df = df[df[targetcol] == target]
    n = len(df)
    return sum(df[colname] == attribute) * 1.0 / n




dat = dict()

prob_yes = sum(df.Play == 1) * 1.0 /len(df)
prob_no = sum(df.Play == 0) * 1.0 /len(df)
prob = {'Yes': prob_yes, 'No': prob_no}



for k, v in df.drop(['Play','Day'], axis=1).iteritems():
    for attribute in v.unique():
        yes = calc(df, k, attribute)
        no = calc(df, k, attribute, 0)
        print "Prob(" + k + ' = ' + attribute + ' | ' + 'Play = Yes) = ' + str(yes)
        print "Prob(" + k + ' = ' + attribute + ' | ' + 'Play = No) = ' + str(no)
        print '-----------------------------------------------------------------'
        dat[attribute] = {'Yes': yes, 'No': no}


def calc_prob(outlook, temperature, humidity, wind):
    target = 'No'
    prob_of_no = dat[outlook][target] * dat[temperature][target] * dat[humidity][target] * dat[wind][target] * prob[target]
    target = 'Yes'
    prob_of_yes = dat[outlook][target] * dat[temperature][target] * dat[humidity][target] * dat[wind][target] * prob[target]
    if prob_of_yes >= prob_of_no:
        print 'Predict yes'
    else:
        print 'Pridict no'

    return {"Yes": prob_of_yes, "No": prob_of_no}


outlook = 'Sunny'
temperature = 'Cool'
humidity = 'High'
wind = 'Strong'
prob1 = calc_prob(outlook, temperature, humidity, wind)
