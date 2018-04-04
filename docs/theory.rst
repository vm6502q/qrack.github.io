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

Simulating a quantum bit takes advantage of the probabilistic nature of the measurement result of a quantum bit and records strictly the complex number amplitude for each of the possible qubit outcomes in a coherent state.  Thus, a two qubit system which can be expressed through the following equation:

.. math::
   :label: 3qb_amp

    \lvert\psi\rangle = x_0 \lvert 000\rangle + x_1 \lvert 001\rangle + x_2 \lvert 010\rangle + x_3 \lvert 011\rangle + \
                        x_4 \lvert 100\rangle + x_5 \lvert 101\rangle + x_6 \lvert 110\rangle + x_7 \lvert 111\rangle

Each of the :math:`x_n` complex numbers represents the amplitudes of the quantum system, on measurement, resulting in a particular bit pattern.  While a real quantum mechanical system would produce probabilistic measurements based on these amplitudes, a simulation like this is deterministic.

.. note:: **Probability vs Amplitude**

	It's a common misrepresentation to consider the :math:`x_n` `eigenstate <http://farside.ph.utexas.edu/teaching/qmech/Quantum/node40.html>`_ as a *probability* rather than an *amplitude*.  The root of this misrepresentation lies in the measurement operation, which collapses the amplitude in a non-unitary fashion, resulting in a probabilistic result.  But the :math:`x_n` eigenstates are not probabilistic values - rather, they are the amplitude times a complex `phase factor <https://en.wikipedia.org/wiki/Phase_factor>`_.  In this document, we will refer to the eigenstates as amplitudes, and values obtained post-measurement as probabilistic.

By collecting :math:`x_n` into a complex number array (called :cpp:member:`Qrack::CoherentUnit::stateVec`), the full quantum representation of the system can be recorded using :math:`2^N` *complex* variables per quantum bit:

.. code-block:: cpp

    std::unique_ptr<Complex16[]> sv(new Complex16[1 << qBitCount]);

Given a standard :math:`X` gate matrix,

.. math::
    :label: x_gate

    \begin{bmatrix}
      0 & 1 \\
      1 & 0
    \end{bmatrix}

a question arises: how can this :math:`2\times2` matrix be applied against the :math:`1xN` matrix for N arbitrary entangled qubits, where the matrix is the :math:`x_n` amplitudes from :eq:`3qb_amp`?

.. math::

    \begin{bmatrix}
      0 & 1 \\
      1 & 0
    \end{bmatrix} ???
    \begin{bmatrix}
      x_{000} \\
      x_{001} \\
      x_{010} \\
      x_{011} \\
      x_{100} \\
      x_{101} \\
      x_{110} \\
      x_{111}
    \end{bmatrix}

The solution here is to apply a `Kronecker product <https://en.wikipedia.org/wiki/Kronecker_product>`_ to the gate matrix.  This expands the matrix out to the appropriate number of dimensions - in this case we would need to perform two Kronecker products for each of the two bits whose values are irrelevant to the result:

.. math::
    :label: x_3bit

    (X \otimes I \otimes I) \times M

.. math::
    :label: x_3bit_2

    (\begin{bmatrix}
      0 & 1 \\\
      1 & 0
    \end{bmatrix}
    \otimes
    \begin{bmatrix}
      1 & 0 \\\
      0 & 1
    \end{bmatrix}
    \otimes
    \begin{bmatrix}
      1 & 0 \\\
      0 & 1
    \end{bmatrix}) \times
    \begin{bmatrix}
      x_{000} \\
      x_{001} \\
      x_{010} \\
      x_{011} \\
      x_{100} \\
      x_{101} \\
      x_{110} \\
      x_{111}
    \end{bmatrix}

.. math::
    :label: x_3bit_3

    \begin{bmatrix}
      0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
      1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
      0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
      0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
      0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
      0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
      0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
      0 & 0 & 0 & 0 & 0 & 0 & 1 & 0
    \end{bmatrix}
    \times
    \begin{bmatrix}
      x_{000} \\
      x_{001} \\
      x_{010} \\
      x_{011} \\
      x_{100} \\
      x_{101} \\
      x_{110} \\
      x_{111}
    \end{bmatrix}

.. math::
  :label: x_3bit_final

    (X \otimes I \otimes I) \times 
    \begin{bmatrix}
      x_{000} \\
      x_{001} \\
      x_{010} \\
      x_{011} \\
      x_{100} \\
      x_{101} \\
      x_{110} \\
      x_{111}
    \end{bmatrix}
    = 
    \begin{bmatrix}
      x_{001} \\
      x_{000} \\
      x_{011} \\
      x_{010} \\
      x_{101} \\
      x_{100} \\
      x_{111} \\
      x_{110}
    \end{bmatrix}

The equation :eq:`x_3bit` inverts the amplitudes of the first bit out of three, but leave the second and third bits alone.  Using the identity matrix :math:`I` preserves the amplitudes of the :math:`x_{0nn}` and :math:`x_{1nn}` positions.  The expanded matrix in :eq:`x_3bit_3` now has the proper dimensionality to be multiplied directly against the amplitude matrix.

.. note:: It's important to remember here that, unlike a classical :math:`NOT` which directly inverts a bit, the :math:`X` gate swaps the *amplitudes* for the states where the qubit is 1 with the amplitudes where the qubit is 0.  So while :math:`x_{000}` and :math:`x_{100}` have particular complex number values, the position in the matrix :math:`M[0]` will always correspond to the amplitude :math:`x_0` in :eq:`3qb_amp`.  If the value of :math:`M[0]` is :math:`x_{100}`, then the amplitude of the system, on measurement, resulting in :math:`\rvert000\rangle` is equal to the amplitude that the system, prior to the :math:`X` gate, would have resulted in :math:`\rvert100\rangle`.  See `Quantum Logic Gates <https://en.wikipedia.org/wiki/Quantum_logic_gate#Circuit_composition_and_entangled_states>`_ for more information.

Implementing this simplistically would, as illustrated above in :eq:`x_3bit_3`, require matrices sized at :math:`2^{2x}`, where :math:`x` is the number of qubits the gate operates on.  This rapidly grows prohibitive in memory usage, and is the primary limitation for simulating quantum systems using classical components.  Happily, these types of matrix operations lend themselves particularly well to both memory optimization as well as parallelization of computational cost.

There are two immediate optimizations that can be performed.  The first is an optimization on the matrix size: by performing the math with only a :math:`2\times2` matrix, the amount of memory allocated is substantially reduced. The :cpp:func:`Qrack::CoherentUnit::Apply2x2()` method utilizes this optimization.

In shorthand for clarity, an optimized :math:`X` gate is calculated using the following linear algebra:

.. math::
  :label: x_3bit_opt

  \begin{bmatrix}
    {
       \begin{bmatrix}
          0 & 1 \\
          1 & 0
       \end{bmatrix}
       \times
        \begin{bmatrix}
            x_{000} \\
            x_{001}
        \end{bmatrix}
    }\\
    {
       \begin{bmatrix}
          0 & 1 \\
          1 & 0
       \end{bmatrix}
       \times
        \begin{bmatrix}
            x_{010} \\
            x_{011}
        \end{bmatrix}
    }\\
    {
       \begin{bmatrix}
          0 & 1 \\
          1 & 0
       \end{bmatrix}
       \times
        \begin{bmatrix}
            x_{100} \\
            x_{101}
        \end{bmatrix}
    }\\
    {
       \begin{bmatrix}
          0 & 1 \\
          1 & 0
       \end{bmatrix}
       \times
        \begin{bmatrix}
            x_{110} \\
            x_{111}
        \end{bmatrix}
    }
  \end{bmatrix}
  =
  \begin{bmatrix}
      {
        \begin{bmatrix}
          x_{001} \\
          x_{000}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
          x_{011} \\
          x_{010}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
          x_{101} \\
          x_{100}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
          x_{111} \\
          x_{110}
        \end{bmatrix}
      }
  \end{bmatrix}

And, fully decomposing :eq:`x_3bit_opt`:

.. math::
    \begin{bmatrix}
      {
        \begin{bmatrix}
            0 & 1
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{000} \\
            x_{001}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
            1 & 0
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{000} \\
            x_{001}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
            0 & 1
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{010} \\
            x_{011}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
            1 & 0
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{010} \\
            x_{011}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
            0 & 1
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{100} \\
            x_{101}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
            1 & 0
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{100} \\
            x_{101}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
            0 & 1
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{110} \\
            x_{111}
        \end{bmatrix}
      } \\
      {
        \begin{bmatrix}
            1 & 0
        \end{bmatrix}
        \times
        \begin{bmatrix}
            x_{110} \\
            x_{111}
        \end{bmatrix}
      }
    \end{bmatrix}
    =
    \begin{bmatrix}
      x_{001} \\
      x_{000} \\
      x_{011} \\
      x_{010} \\
      x_{101} \\
      x_{100} \\
      x_{111} \\
      x_{110}
    \end{bmatrix}

It's worth pointing out that the operation detailed in :eq:`x_3bit_opt` is heavily parallelize-able, yielding substantial benefits when working with gates spanning more than just one register (e.g. :math:`CNOT` and :math:`CCNOT` gates).  In C++, this would be implemented like so:

.. code-block:: cpp

    // Create a three qubit register.
    Qrack::CoherentUnit qReg(3);

    // X-gate the bit at index 0
    qReg->X(0);

The second optimization is one of combining sequential gates into a single matrix, allowing for a reduction in both matrix size and computational cost.  See IBM's `article <https://www.ibm.com/blogs/research/2017/10/quantum-computing-barrier/>`_ and related `publication <https://arxiv.org/abs/1710.05867>`_ for details on how to optimize these operations in more detail.  The :cpp:class:`Qrack::CoherentUnit` register-wide operations (e.g. :cpp:func:`Qrack::CoherentUnit::X`) leverage these types of optimizations, with parallelization provided through threading and OpenCL, as supported.

LDA,X Unitary Matrix
~~~~~~~~~~~~~~~~~~~~

.. math::

	\begin{bmatrix}
		1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
		0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 
	\end{bmatrix}

6502 Reference Documents
------------------------

.. [MOS-6502] The 6502 CPU - https://en.wikipedia.org/wiki/MOS_Technology_6502
.. [6502ASM] 6502 Assembly Reference - http://www.6502.org/tutorials/6502opcodes.html

For details on the added opcodes supported by vm6502q, see :ref:`mos-6502q-opcodes`.
