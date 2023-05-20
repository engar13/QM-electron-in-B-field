# QM-electron-in-B-field
Python computation of an electron's spin probability of transition to the down state when inside a uniform magnetic field in the +Z direction with a little bit of X component.

The code generates a graph with the probability of flipping to the down state as a function of time, in three different ways:

1. Numerically computed probability.
2. Exact probability of transition given by analytical solution.
3. Aproximation given by time-dependent perturbation theory.

![image](https://github.com/engar13/QM-electron-in-B-field/assets/133209572/61255519-2c8c-4d39-abdc-5d25b3cace0c)

NOTE: Even though the Hamiltonian of the System is Time **In**dependent, we have a probability of changing state if we turn on and off the perturbation (during the time in which the perturbation is "on" the system is in a static state, whose exact spins and wavefunctions are no longer the spin up or down states and could be approximated using time independent perturbation theory) and only when the perturbation is turned "off" the spins up and down in the Z-axis are once again the eigenstates of the system and we might have had a transition to the "down" state even though we started with the "up" state.
