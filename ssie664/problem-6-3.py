import numpy as np

def simulation(itr=None, P=None, L=None, i=None, N=None, AE=None, cdf=None):
    results_summary = []
    results_simulation = []
    
    case_01 = (((P-L)*i) / (((1 + i)**(N)) - 1)) + ((P*i))
    case_02 = (((P-L)*i) / (((1 + i)**(N)) - 1)) + ((P*i)+(AE))
    
    for each in range(itr):
        resultsi = dict()
        draw = np.random.uniform()

        if draw <= cdf:
            resultsi['draw'] = draw 
            resultsi['outcome'] = 'case_01' 
            resultsi['annual_cost'] = case_01 
            results_simulation.append(resultsi)
        else:
            resultsi['draw'] = draw 
            resultsi['outcome'] = 'case_02' 
            resultsi['annual_cost'] = case_02
            results_simulation.append(resultsi)
            
    freq_case_01 = [each['outcome'] for each in results_simulation].count('case_01') / itr
    freq_case_02 = [each['outcome'] for each in results_simulation].count('case_02') / itr
    
    resultsk = dict()
    resultsk['expected_value'] = (case_01 * freq_case_01) + (case_02 * freq_case_02)
    resultsk['case_01_freq'] = freq_case_01
    resultsk['case_02_freq'] = freq_case_02
    resultsk['case_01_cost'] = case_01
    resultsk['case_02_cost'] = case_02
    results_summary.append(resultsk)
    
    return results_summary, results_simulation

data_A = simulation(itr=100000, P=500000, L=0, i=0.1, N=40, AE=600000, cdf=0.85)
data_B = simulation(itr=100000, P=500000, L=0, i=0.1, N=40, AE=600000, cdf=0.95)
data_C = simulation(itr=100000, P=500000, L=0, i=0.1, N=40, AE=600000, cdf=0.99)

print('Expected Value of Project A: ${:,.2f}'.format(data_A[0][0]['expected_value']))
print('Expected Value of Project B: ${:,.2f}'.format(data_B[0][0]['expected_value']))
print('Expected Value of Project C: ${:,.2f}'.format(data_C[0][0]['expected_value']))
