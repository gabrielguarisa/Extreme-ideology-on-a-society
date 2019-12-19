class PopulationManager:
    def __init__(self, total_population, sub_populations_names=["E", "N", "V", "A"]):
        self.previous = {}

        num_sub_populations = len(sub_populations_names)
        for name in sub_populations_names:
            self.previous[name] = int(total_population / num_sub_populations)

    def get_total_population(self):
        total = 0
        for _, value in self.previous.items():
            total += value
        return total

    def get_births(self, birth_rate):
        births = {}
        for name, value in self.previous.items():
            births[name] = birth_rate * value
        return births

    def get_deaths(self, death_rate):
        deaths = {}
        for name, value in self.previous.items():
            deaths[name] = death_rate * value
        return deaths

    def get_rates(self):
        total_population = self.get_total_population()
        rates = {}
        for name, value in self.previous.items():
            rates[name] = value / total_population
        return rates

    def evolve(
        self,
        alpha_1,
        alpha_2,
        beta_1,
        beta_2,
        birth_rate,
        death_rate,
        immigration_rate,
        emigration_rate,
        k,
    ):
        births = self.get_births(birth_rate)
        deaths = self.get_deaths(death_rate)
        rates = self.get_rates()

        new_sb = {}  # new subpopulations

        new_sb["E"] = int(
            self.previous["E"]
            + births["E"]
            + alpha_2 * immigration_rate
            - beta_1 * self.previous["E"] * rates["V"]
            - deaths["E"]
            - alpha_1 * emigration_rate
        )

        new_sb["N"] = int(
            self.previous["N"]
            + births["N"]
            - beta_2 * self.previous["N"] * rates["E"]
            - deaths["N"]
        )

        new_sb["V"] = int(
            self.previous["V"]
            + births["V"]
            + k * beta_1 * self.previous["A"] * rates["V"]
            - deaths["V"]
        )

        new_sb["A"] = int(
            self.previous["A"]
            + births["A"]
            + (1 - alpha_2) * immigration_rate
            + beta_1 * self.previous["E"] * rates["V"]
            + beta_2 * self.previous["N"] * rates["E"]
            - k * beta_1 * self.previous["A"] * rates["V"]
            - deaths["A"]
            - (1 - alpha_1) * emigration_rate
        )

        for name, value in new_sb.items():
            self.previous[name] = value

        return self.previous
