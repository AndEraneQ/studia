import sys
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from models.fire_station import FireStation
from models import Event
from observers.logger import Logger
from iteration.iterator import Iterator
from strategy.strategy import FireResponseStrategy, HazardResponseStrategy

sys.path.append(str(Path(__file__).resolve().parents[1]))

class Map:
    STATION_LOCATIONS = {
        "JRG1": [50.0599179817761, 19.943109097898308],
        "JRG2": [50.03367378422457, 19.935677587243156],
        "JRG3": [50.07558843771017, 19.887066835538878],
        "JRG4": [50.037607106477815, 20.005775043445905],
        "JRG5": [50.092112896692576, 19.920375568078363],
        "JRG6": [50.01600677090119, 20.01560115206121],
        "JRG7": [50.09403344711918, 19.977527923870664],
        "JRG_Skawina": [49.968341021285674, 19.79928999293016],
        "JRG_PSP": [50.07711317778578, 20.032658871795807],
        "LSB_Balice": [50.07327060533678, 19.80488126069325]
    }

    LATITUDE_RANGE = (49.95855025648944, 50.154564013341734)
    LONGITUDE_RANGE = (19.688292482742394, 20.02470275868903)

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.fig.suptitle("Simulation", fontsize=10)
        self.ax.set_xlim(self.LONGITUDE_RANGE)
        self.ax.set_ylim(self.LATITUDE_RANGE)

        self.fire_stations = self.create_stations()
        self.logger = Logger(self.fire_stations)
        self.fire_dispatch_strategy = FireResponseStrategy()
        self.hazard_dispatch_strategy = HazardResponseStrategy()
        self.events = []

        self.step = 0
        self.event_frequency = 4

    def create_stations(self):
        return [FireStation(name, loc) for name, loc in self.STATION_LOCATIONS.items()]

    def start(self, num_steps=10000):
        self.animation = FuncAnimation(self.fig, self.animate_step, frames=num_steps, interval=500, repeat=False)
        plt.show()

    def animate_step(self, frame):
        self.step += 1
        self.generate_event_if_needed()
        self.update_simulation_state()
        self.render_map()

    def generate_event_if_needed(self):
        if self.step % self.event_frequency == 0:
            event = Event()
            event.generate_random_event()
            self.logger.log_event(event)
            vehicles_assigned = self.dispatch_vehicles(event)
            self.events.append(event)

    def dispatch_vehicles(self, event):
        if event.event_type == "PZ":
            return self.fire_dispatch_strategy.assign_vehicles_to_event(event, self.fire_stations)
        elif event.event_type == "MZ":
            return self.hazard_dispatch_strategy.assign_vehicles_to_event(event, self.fire_stations)
        else:
            return []

    def update_simulation_state(self):
        event_iterator = Iterator(self.events)

        for event in event_iterator:
            if not event.is_complete:
                event.update()
        for event in self.events:
            if event.is_complete:
                print(f"\nVehicles from {event.event_location} go back to the station")
                for vehicle in event.assigned_vehicles:
                    vehicle.complete_assigned_task()

        self.clean_up_completed_events()
        self.refresh_vehicle_states()

    def clean_up_completed_events(self):
        self.events = [event for event in self.events if not event.is_complete]

    def refresh_vehicle_states(self):
        for station in self.fire_stations:
            for vehicle in station.vehicles:
                vehicle.update_vehicle_state()

    def render_map(self):
        self.ax.clear()
        self.ax.set_xlim(self.LONGITUDE_RANGE)
        self.ax.set_ylim(self.LATITUDE_RANGE)

        for station in self.fire_stations:
            x, y = station.station_location
            self.ax.plot(y, x, 'ro', color='green', label="Fire Stations:")

        for event in self.events:
            if not event.is_complete:
                x, y = event.event_location
                if event.event_type == "PZ":
                    self.ax.plot(y, x, 'o', color='red')
                elif event.event_type == "MZ":
                    self.ax.plot(y, x, 'o', color='orange')
                elif event.event_type == "AF":
                    self.ax.plot(y, x, 'o', color='blue')

        self.ax.legend(
        handles=[
            plt.Line2D([1], [1], marker='o', color='w', markerfacecolor='green', markersize=10, label="Fire Stations"),
            plt.Line2D([1], [1], marker='o', color='w', markerfacecolor='red', markersize=10, label="PZ"),
            plt.Line2D([1], [1], marker='o', color='w', markerfacecolor='orange', markersize=10, label="MZ"),
            plt.Line2D([1], [1], marker='o', color='w', markerfacecolor='blue', markersize=10, label="AF")
        ],
        loc="upper center",
        bbox_to_anchor=(0.5, -0.05),
        ncol=4
        )
        plt.draw()
