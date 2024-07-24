import simpy
import random


# given data
# decelaring the global variable
AVG_ARRIVAL_TIME = 5*60  
CONTAINERS_PER_VESSEL = 150  
PORT_COUNT = 2 
BERTH_CRANES = 2  
TRUCK_COUNT = 3 
CRANE_TIME = 3  
TRUCK_TIME = 6  


#class decelaration for the terminal
class Container_Terminal():
    #initiliaziation of the class 
    def __init__(self, env):
        self.env = env
        # allocation of all the varibles required by any of the port
        self.port = simpy.Resource(env, PORT_COUNT)
        self.crane = simpy.Resource(env, BERTH_CRANES)
        self.trucks = simpy.Resource(env, TRUCK_COUNT)
        
    # this code resembeles the use of docking the vessel at the port
    def dock_Vessel(self, vessel):
        with self.port.request() as request:
            # yielding the request for the port
            yield request
            print(f"Vessel {vessel} berthed at {self.env.now:.2f}")
            print(f"The Unloading of Vessel {vessel} has been successfully started at {self.env.now:.2f}\n")
            # calling the process to simulate for the process of vessel
            yield self.env.process(self.unload_vessel(vessel))

            # unloading successfully of the vessel
            print(f"\nVessel {vessel} --> The Vessel {vessel} is unloaded succesfully and had left the port at {self.env.now:.2f}\n")

    # unloading of the particular vessel -- unloading all the 150 containers of the vessel
    def unload_vessel(self, vessel):
        for i in range(CONTAINERS_PER_VESSEL):
            yield self.env.process(self.process_container(vessel, i + 1))


    def process_container(self, vessel, container_id):
        # checking the crane is empty or in use -- request for a crane for a vessel
        with self.crane.request() as crane_request:
            yield crane_request
            # requesting a truck for transfering the container
            with self.trucks.request() as truck_request:
                yield truck_request
                # time required to transfer the container
                yield self.env.timeout(CRANE_TIME)
                print(f"Vessel {vessel} --> Vessel {vessel} crane moved container {container_id} using truck at {self.env.now:.2f}")
                self.env.process(self.transport_container(vessel, container_id, 1, truck_request))

    def transport_container(self, vessel, container_id, truck_id, truck_request):
        yield self.env.timeout(TRUCK_TIME)
        print(f"Vessel {vessel} --> Truck moved container {container_id} of Vessel {vessel} at {self.env.now:.2f}")
        self.trucks.release(truck_request)


# this function is responsible for generating the new vessels for the simulator to run
# takes a random time and at an average of 5 hrs
def vessel_generator(env, terminal):
    vessel_id = 0
    # allocating the first two/one ports by the first two/one vessels
    for _ in range(PORT_COUNT):
        vessel_id += 1
        env.process(terminal.dock_Vessel(str(vessel_id)))


    while True:
        # creating a random waiting time for the arrival of each of the vessels

        # creating a random waiting time for the arrival of each of the vessels
        waiting_time = random.randint(AVG_ARRIVAL_TIME-50,AVG_ARRIVAL_TIME+50)
        yield env.timeout(waiting_time)
        vessel_id += 1
        env.process(terminal.dock_Vessel(str(vessel_id)))

# the main function of the program responsible for calling all the functions sequentially
def main(val):
    random.seed(42)
    env = simpy.Environment()
    terminal = Container_Terminal(env)
    env.process(vessel_generator(env, terminal))
    env.run(until=val)

print("Enter the time in minutes..... : ",end="")
SimulationTime = int(input())
main(SimulationTime)
