import numpy as np # importação da biblioteca numpy

alpha = (3 + np.sqrt(5)) / 2 # cálculo do alpha
beta = (3 - np.sqrt(5)) / 2 # cálculo do beta
omega = np.log(alpha) # cálculo do omega
i_0 = 0.185408 # corrente inicial
V = 45 # tensão aplicada
R = 150 # resistência

for n in range(0,6): # 0 ≤ n ≤ 6
    # equação final da corrente
    i_n =(i_0*np.cosh(omega*n))+((i_0/2)-(V/R))*(2/np.sqrt(5))*np.sinh(omega*n) 
    # mostra os valores para cada valor de n
    print(f"i({n}) = {i_n:.5f}" ) 


