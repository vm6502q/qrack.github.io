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
.. [QC10th] `Quantum Computing 10th Edition - Nielson and Chuang <http://www-reynal.ensea.fr/docs/iq/QC10th.pdf>`_
.. [QAVLA] `Quantum Algorithms via Linear Algebra: A Primer - Lipton and Regan <http://mmrc.amss.cas.cn/tlb/201702/W020170224608149911380.pdf>`_

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

The :cpp:func:`Qrack::CoherentUnit::Apply2x2()` method applies a :math:`2\times2` matrix against the state vector, for example from an :cpp:func:`Qrack::CoherentUnit::X()` gate. If we apply a gate only to the second bit, then the :math:`2\times2` matrix operation is acted in parallel pairings of all states where all bits are the same except for the second bit. Pairs of states where all bits are the same, except the second bit pairs values of `0` and `1`, can be independently acted on by the :math:`2\times2` matrix in parallel. For example, for two bits, acting on the right-hand bit, the pairings would be :math:`\rvert00\rangle` with :math:`\rvert01\rangle`, and :math:`\rvert10\rangle` with :math:`\rvert11\rangle`. Uninvolved bits are held the same and iterated over, while the bit acted upon is drawn into pairs `0` and `1`. This gives a set of sub-state vectors with only two components, which can be multiplied by the :math:`2\times2` matrix.

Extending to register-like operations, say we want to apply a bitwise ``NOT`` or ``X`` operation on the right-hand register of 8 bits. We simply apply the ``NOT`` operation simultaneously on all of the right-hand bits in all entangled input states.

Say we have a `Qrack::CoherentUnit` called `qReg` with the following initial state:

.. math:: \rvert\psi_0\rangle = \frac{1}{\sqrt{2}} \rvert(01010101)\ (11111110)\rangle - \frac{1}{\sqrt{2}} \rvert(10101010)\ (00000000)\rangle

We act the ``X`` operation on the right-hand 8 bits:

.. code-block:: cpp

    qReg->X(8, 8);

This is like acting a ``NOT`` operation on the right-hand 8 bits in every superposed state, in parallel, becoming this state:

.. math:: \hat{X} \rvert\psi_0\rangle = \rvert\psi_1\rangle = \frac{1}{\sqrt{2}} \rvert(01010101)\ (00000001)\rangle - \frac{1}{\sqrt{2}} \rvert(10101010)\ (11111111)\rangle

This is again an "embarrassingly parallel" operation. Some bits are completely uninvolved and these bits are passed unchanged in each state from input to output. Bits acted on by the register operation have a one-to-one mapping between input and states. This can all be handled through transformation via bit masks on the input state permutation index. Register-like methods generally all use bitmasks to separate involved bits from uninvolved bits, transform the involved bits like above, and use the bit transformation to map state vector coefficients to new positions in the vector, in a unitary manner. (Note that the operation amounts to swapping coefficients in correspondence with the bitmask transforms, not directly acting bitwise operations on the raw representation of the state itself. The state is represented as a set of double precision complex coeffecients, not bits.)


6502 Reference Documents
------------------------

.. [MOS-6502] The 6502 CPU - https://en.wikipedia.org/wiki/MOS_Technology_6502
.. [6502ASM] 6502 Assembly Reference - http://www.6502.org/tutorials/6502opcodes.html
