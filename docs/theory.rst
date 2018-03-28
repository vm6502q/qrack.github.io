Theory
======

Foundational Material
---------------------

Broadly speaking, a certain amount of prerequisite knowledge is necessary to utilize and understand quantum computational algorithms and processes.  Someday this material may be substantially diminished by intelligently chosen abstractions, but today quantum systems are still heavily dependent on an understanding of the underlying mathematical principles.

It is well outside the scope of this document to cover that material, however a set of references have been collected here.  These materials provide a sufficient foundation for onboarding a new engineer or scientist.

Quantum Computational Basics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. [Susskind] `Modern Physics: Quantum Mechanics, by Dr. Leonard Susskind <https://www.youtube.com/watch?v=2h1E3YJMKfA>`_
.. [WiredSummary] `Wired's Overview of the Industry <https://www.wired.com/story/the-era-of-quantum-computing-is-here-outlook-cloudy/>`_
.. [AlgoZoo] `Quantum Algorithm Zoo <https://math.nist.gov/quantum/zoo/>`_
.. [QC10th] `Quantum Computing 10th Edition - Nielson and Chung <http://www-reynal.ensea.fr/docs/iq/QC10th.pdf>`_

Grover Search Algorithm
~~~~~~~~~~~~~~~~~~~~~~~

.. [Grover] `Grover Search Algorithm <https://en.wikipedia.org/wiki/Grover%27s_algorithm>`_
.. [GroverSummary] `Introduction to Implementing Grover's Search Algorithm <http://twistedoakstudios.com/blog/Post2644_grovers-quantum-search-algorithm>`_
.. [GroverVisual] `Visualization of Grover's Search Algorithm <http://davidbkemp.github.io/animated-qubits/grover.html>`_

Quantum Bit Simulation
----------------------

Simulating a quantum bit takes advantage of the probabilistic nature of the measurement result of a quantum bit and records strictly the complex number probability for each of the bits in a coherent state.  Thus, a two qubit system which can be expressed through the following equation:

.. math::
   :label: psi_prob

    \rvert\psi\rangle = x_0 \rvert000\rangle + x_1 \rvert001\rangle + x_2 \rvert010\rangle + x_3 \rvert011\rangle + \
                        x_4 \rvert100\rangle + x_5 \rvert101\rangle + x_6 \rvert110\rangle + x_7 \rvert111\rangle

Each of the :math:`x_n` complex numbers represents the probability of the quantum system, on measurement, resulting in a particular bit pattern.

By collecting :math:`x_n` into a complex number array (called :cpp:member:`Qrack::CoherentUnit::stateVec`), the full quantum representation of the system can be recorded using :math:`2^N` *complex* variables per quantum bit:

.. code-block:: cpp

    std::unique_ptr<Complex16[]> sv(new Complex16[1 << qBitCount]);

The :cpp:func:`Qrack::CoherentUnit::Apply2x2()` method applies a :math:`2\times2` matrix against the complex number, for example from an :cpp:func:`Qrack::CoherentUnit::X()` gate.

.. TODO: Add additional commentary breaking apart how Apply2x2 works, and what it iterates over.


6502 Reference Documents
------------------------

.. [MOS-6502] The 6502 CPU - https://en.wikipedia.org/wiki/MOS_Technology_6502
.. [6502ASM] 6502 Assembly Reference - http://www.6502.org/tutorials/6502opcodes.html
