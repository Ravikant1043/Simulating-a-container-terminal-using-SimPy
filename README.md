**Container-Terminal-Simulation-using-SimPy**

This Repositry contains a simulation task of how the vessels are approaching to the Terminal to Unload the containers with the help of trucks, Here i have used a "SIMPY" module of Python to achieve the task of simulation

**SIMPY**

Simpy is a simulation platform based on simple python, which provides us the environment which makes it possible to simulate the code.
With the help of the resources provided by the simpy its easy to handle the threads and syncronize the task.

**Features**

Vessel arrival process: Vessels arrive at the terminal following an exponential distribution with an average of 5 hours between arrivals.
Berthing/Docking operations: There are two available berths at the terminal. If both berths are occupied, incoming vessels join a waiting queue and if any of the vessel will be free the vessel will be docked/berthed at that berth.
Quay crane operations: Two quay cranes are responsible for unloading containers from vessels. Each crane takes 3 minutes to move one container. The cranes operates independently but cannot serve the same vessel simultaneously.
Truck transportation: Three trucks are given for transporting containers from quay cranes to yard blocks. Each truck takes 6 minutes to drop off a container and return to the quay crane in the time between the transporting of the containers if no crane is empty for unloading of the vessel so the crane will go in the wait state for the next truck to be free.
Logging system: The simulation includes a simple logging system that records events such as vessel arrival, departure, berthing, crane movements and truck operations. The log includes the current simulation time and on which vessel the operation is being performed.

**USAGE**

install the simpy package in your pc.
To start the simulation download the code and run it in any ide containing python (simpy modules)
