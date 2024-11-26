from src.simulation import Simulation

if __name__ == "__main__":
    sim = Simulation(10, 10, 50, True)
    sim.generatePopulation(20)
    sim.show_animation()
    



