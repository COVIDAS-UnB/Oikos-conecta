## Parte dos códigos foram obtidos nesse site: https://www.statsandr.com/blog/covid-19-in-belgium/

library('readxl')
file.choose()

confirmados <- read_xlsx("/home/leticia/Downloads/casos_confirmados.xlsx")
recuperadoss <- read_xlsx("/home/leticia/Downloads/casos_recuperados.xlsx")

dados['total_casos'] = dados["Casos confirmados"] + dados["Casos recuperados"]

dados['variacao'] = c(0,diff(dados$total_casos))

1 + mean((dados$variacao/dados["Casos confirmados"])[-1,])


SIR <- function(time, state, parameters) {
  par <- as.list(c(state, parameters))
  with(par, {
    dS <- -beta * I * S / N
    dI <- beta * I * S / N - gamma * I
    dR <- gamma * I
    list(c(dS, dI, dR))
  })
}

library(dplyr)

infectados <- confirmados$`Casos confirmados`
N <- 54762
recuperados <- c(rep(0, length(infectados)-length(recuperadoss$caso)),recuperadoss$`Casos recuperados`)

init <- c(
  S = N - infectados[1],
  I = infectados[1],
  R = 0
)

Day = (1:length(infectados))
RSS <- function(parameters) {
  names(parameters) <- c("beta", "gamma")
  out <- ode(y = init, times = Day, func = SIR, parms = parameters)
  fit <- out[, 3]
  sum((infectados - fit)^2)
}

# now find the values of beta and gamma that give the
# smallest RSS, which represents the best fit to the data.
# Start with values of 0.5 for each, and constrain them to
# the interval 0 to 1.0

# install.packages("deSolve")
library(deSolve)

Opt <- optim(c(0.5, 0.5),
             RSS,
             method = "L-BFGS-B",
             lower = c(0, 0),
             upper = c(1, 1)
)

# check for convergence
Opt$message
Opt_par <- setNames(Opt$par, c("beta", "gamma"))
Opt_par

## Levar isso pro universo do IF
n = 35
i = (infectados[length(infectados)]/N) * n
s = n-1

r0 = Opt_par[1]/Opt_par[2]

r0 * (s/n) * i
3.5*(s*i)/n

fitted_cumulative_incidence <- data.frame(ode(
  y = init, times = t,
  func = SIR, parms = Opt_par
))
