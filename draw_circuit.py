import numpy as np
from qiskit.circuit import Parameter
from chsh_inequality import makeInitial, makeCircuit

theta = Parameter('θ')

circuit = makeInitial(theta)
circuit.draw(output='mpl', filename="output/initial_state.png")

circuit = makeCircuit(theta, -np.pi/2, -np.pi/4)
circuit.draw(output='mpl', filename="output/term1.png")

circuit = makeCircuit(theta, -np.pi/2, np.pi/4)
circuit.draw(output='mpl', filename="output/term2.png")

circuit = makeCircuit(theta, 0, -np.pi/4)
circuit.draw(output='mpl', filename="output/term3.png")

circuit = makeCircuit(theta, 0, np.pi/4)
circuit.draw(output='mpl', filename="output/term4.png")



