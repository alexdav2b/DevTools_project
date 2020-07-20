import os

import Simulation

os.chdir("../Redis-x64-3.2.100")
os.startfile('redis-server.exe')
os.chdir("../src")

sim = Simulation.Simulation()
sim.run()
