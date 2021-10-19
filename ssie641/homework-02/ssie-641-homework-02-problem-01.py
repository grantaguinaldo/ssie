import numpy as np
import matplotlib.pyplot as plt

def density(t=None, k=None, m=None, m0=None):
    return (t / (m*(m0 + t))) * np.exp(1-(k/m))

k_values = [each for each in range(1, 80)]
density_values_1 = [density(t=200000, k=each, m=10, m0=50) for each in k_values]
density_values_2 = [density(t=100000, k=each, m=5, m0=50) for each in k_values]
density_values_3 = [density(t=500000, k=each, m=50, m0=5000) for each in k_values]

plt.figure(figsize=(4, 7))
plt.semilogy(k_values, density_values_1, linestyle='dotted', color='black', label='Trial 1')
plt.semilogy(k_values, density_values_2, linestyle='solid', color='black', label='Trial 2')
plt.semilogy(k_values, density_values_3, linestyle='dashed', color='black', label='Trial 3')
plt.xlabel('(degrees) \n k', fontsize=14)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.ylabel('P(K) \n (unitless)', fontsize=14)
plt.title('Connectivity Distribution \n (Semi-Log Plot)', fontsize=14)
plt.legend()
plt.savefig('figure1.png', bbox_inches='tight')
# plt.show()