from populationmanager import PopulationManager
import pandas as pd
import random

SEED = random.randint(0, 999999999)
print("SEED:", SEED)
random.seed(SEED)

def generate_random_rates():
    terror_pressure_pE = random.uniform(0.0002, 0.0002)
    terror_pressure_pA = random.uniform(0.0002, 0.0002)
    violent_acts_vp = random.uniform(0.0, 0.01)
    violent_acts_nvp = random.uniform(0.0, 0.01)
    birth_rate = random.uniform(0.01, 0.02)
    death_rate = random.uniform(0.005, 0.01)
    immigration_rate = random.uniform(0.002, 0.004)
    emigration_rate = random.uniform(0.068, 0.102)

    return (
        terror_pressure_pE,
        terror_pressure_pA,
        violent_acts_vp,
        violent_acts_nvp,
        birth_rate,
        death_rate,
        immigration_rate,
        emigration_rate,
    )


t_max = 1000

k = 1
brasil = PopulationManager(total_population=208846892)
data = []

for key, value in brasil.previous.items():
    data.append({"type": key, "population": value, "t": 0})
print(brasil.previous)

for t in range(t_max):
    (
        terror_pressure_pE,
        terror_pressure_pA,
        violent_acts_vp,
        violent_acts_nvp,
        birth_rate,
        death_rate,
        immigration_rate,
        emigration_rate,
    ) = generate_random_rates()
    
    brasil.evolve(
        alpha_1=terror_pressure_pE,
        alpha_2=terror_pressure_pA,
        beta_1=violent_acts_vp,
        beta_2=violent_acts_nvp,
        birth_rate=birth_rate,
        death_rate=death_rate,
        immigration_rate=immigration_rate,
        emigration_rate=emigration_rate,
        k=k,
    )

    for key, value in brasil.previous.items():
        data.append({"type": key, "population": value, "t": t + 1})


print(brasil.previous)

df = pd.DataFrame(data, columns=["type", "population", "t"])

df.to_csv("outputs/{}.csv".format(SEED))