import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N #  constant contact rate 
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I 
    return dSdt, dIdt, dRdt

# Model Simulation.
def sir_calc(S0, I0, R0, N, beta, gamma, t):
    # Initial conditions
    y0 = S0, I0, R0
    
    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T

    return S, I , R

# No prevention case: 
# Total population, N.
N = 30
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 =  1, 1.34
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.702, 0.52
# A grid of time points (in days)
t = np.linspace(0, 80, 80)
# SIR no prevention 
S, I, R = sir_calc(S0, I0, R0, N, beta, gamma, t)

# 0.7% nbr students case: 
# Total population, N.
N = 30*0.7
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 =  1, 1.34
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.502, 0.52
# A grid of time points (in days)
t = np.linspace(0, 80, 80)
# SIR 10% reduction
S3, I3, R3 = sir_calc(S0, I0, R0, N, beta*0.7, gamma, t)

# 0.5% nbr students case: 
# Total population, N.
N = 30*0.5
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 =  1, 1.34
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.502, 0.52
# A grid of time points (in days)
t = np.linspace(0, 80, 80)
# SIR 10% reduction
S1, I1, R1 = sir_calc(S0, I0, R0, N, beta*0.5, gamma, t)


# 0.3% nbr students case: 
# Total population, N.
N = 30*0.3
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 =  1, 1.34
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.502, 0.52
# A grid of time points (in days)
t = np.linspace(0, 80, 80)
# SIR 10% reduction
S2, I2, R2 = sir_calc(S0, I0, R0, N, beta*0.3, gamma, t)

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, I/30 *100, 'r-', alpha=1, lw=2.2, label='Sem medidas')
ax.plot(t, I3/(30*0.7) *100, 'c-', alpha=1, lw=2.2, label='70%')
ax.plot(t, I1/(30*0.5) *100, 'b-', alpha=1, lw=2.2, label='50%')
ax.plot(t, I2/(30*0.3) *100, 'g-', alpha=1, lw=2.2, label='30%')

# Plot simulation results
# ax.plot(t, I/N, 'r', alpha=1, lw=2.4, label='Redução 10% vagas')
plt.autoscale(enable=True, axis='x', tight=True)
ax.set_xlabel('Dias de aula')
ax.set_ylabel('Porcentagem de alunos infectados por sala \n tendo por base 1 aluno infectado no primeiro dia de aula(%)')
ax.set_ylim(0,10)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(1)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()


