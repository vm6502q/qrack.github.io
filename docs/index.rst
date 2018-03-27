.. vm6502q documentation master file, created by
   sphinx-quickstart on Wed Mar 21 20:32:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

VM6502Q and Qrack
=================

Build Status
------------

 * Qrack: |qrack_build_status|
 * VM6502Q: |vm6502q_build_status|
 * CC65: |cc65_build_status|
 * Examples: |examples_build_status|

.. |cc65_build_status| image:: https://api.travis-ci.org/vm6502q/cc65.svg?branch=6502q
    :target: https://travis-ci.org/vm6502q/cc65/builds

.. |qrack_build_status| image:: https://api.travis-ci.org/vm6502q/qrack.svg?branch=master
    :target: https://travis-ci.org/vm6502q/qrack/builds

.. |vm6502q_build_status| image:: https://api.travis-ci.org/vm6502q/vm6502q.svg?branch=master
    :target: https://travis-ci.org/vm6502q/vm6502q/builds

.. |examples_build_status| image:: https://api.travis-ci.org/vm6502q/examples.svg?branch=master
    :target: https://travis-ci.org/vm6502q/examples/builds

.. TODO: General commentary:
         
         Broadly speaking, there's a lot of information here.  It needs to be
         pulled out into three sections:
             1. Quantum Computation Basics
                ... containing all of the gate operation and most of the math,
                    as well as references to external literature
                theory bits.
             2. Simulating a Quantum Bit
                ... containing a dissection of how a quantum bit is simulated
                    in classical hardware, including code snippets, examples,
                    and references to external literature.
             3. Qrack Implementation Details
                ... containing the details on how a CoherentBit is implemented,
                    including optimizations, parallalization tradeoffs, and
                    mathematical accuracy issues.
         
         The first section has the most material present, but the second and
         third sections are very sparse.  I would not, after reading this, be
         able to implement a CoherentUnit, or even understand how CoherentUnit
         simulates a qubit.
         
         It's worth noting that it's not necessary for you to write all of this
         text yourself - referencing or directing to valuable external
         literature (but a minimum of published papers) is a very viable way of
         sharing the weight.

VM6502Q and Qrack
=================

Introduction
------------


Qrack is a C++ quantum bit simulator, with the ability to support arbitrary numbers of entangled qubits - up to system limitations.  Suitable for embedding in other projects, the :cpp:class:`Qrack::CoherentUnit` contains a full and performant collection of standard quantum gates, as well as variations suitable for register operations and arbitrary rotations.

As a demonstration of the :cpp:class:`Qrack::CoherentUnit` implementation, a MOS-6502 microprocessor [MOS-6502]_ virtual machine has been modified with a set of new opcodes supporting quantum operations.  The `vm6502q <https://github.com/vm6502q/vm6502q>`_ virtual machine exposes new integrated quantum opcodes such as a Grover Search [Grover]_ across a page of memory.  These programs are demonstrated in the `examples <https://github.com/vm6502q/examples>`_ repository.

Finally, a `6502 toolchain <https://github.com/vm6502q/cc65>`_, based on the CC65 toolchain [CC65]_, has been modified and enhanced to support both the new opcodes - for the assembler - as well as `C Syntax Enhancements`_.  This is performed primarily as sandbox/exploratory work to help clarify what quantum computational software engineering might look like as the hardware reaches commoditization.

Getting Started
---------------

Checking Out
~~~~~~~~~~~~

Check out each of the major repositories into a project branch:

.. code-block:: bash

          / $ mkdir qc
          / $ cd qc
        qc/ $ for i in 'https://github.com/vm6502q/qrack.git'      \
                       'https://github.com/vm6502q/vm6502q.git'    \
                       'https://github.com/vm6502q/examples.git'   \
                       'https://github.com/vm6502q/cc65.git'; do
                git clone $i
              done

            # Add a necessary symlink connecting the vm6502q project with qrack
        qc/ $ cd vm6502q && ln -s ../qrack

Compiling
~~~~~~~~~

.. note::

    The ``qrack`` project supports two primary implementations: OpenCL-optimized and software-only.  See :doc:`opencl` for details on installing OpenCL on some platforms, or your appropriate OS documentation.

    If you do not have OpenCL or do not wish to use it, supply the ``ENABLE_OPENCL=0`` environment to ``make`` when building the project.

Compile in the ``vm6502q`` project.  This will build both the ``vm6502q`` emulator as well as the linked ``qrack`` project:

.. code-block:: bash

   vm6502q/ $ make
            # OR if no OpenCL is available
   vm6502q/ $ ENABLE_OPENCL=0 make

Testing
~~~~~~~

The qrack project has an extensive set of unittests for the various :cpp:class:`Qrack::CoherentUnit` gates and simulator methods.  This can be executed through running the test suite in the ``qrack`` project:

.. code-block:: bash

     qrack/ $ make test
            # OR if no OpenCL is available
     qrack/ $ ENABLE_OPENCL=0 make test

This may take a few minutes to complete, depending on the strength of the system executing the tests.

.. note::

    The unittests, by default, run against all supported engines.  If only a specific engine type is desired, the ``--disable-opencl`` or ``--disable-software`` command line parameters may be supplied to the ``unittest`` binary.

Embedding Qrack
~~~~~~~~~~~~~~~

The ``qrack`` project produces a ``libqrack.a`` archive, suitable for being linked into a larger binary.  See the :cpp:class:`Qrack::CoherentUnit` documentation for API references, as well as the examples present in `the unit tests <https://github.com/vm6502q/qrack/blob/master/tests.cpp>`_.

Performance
~~~~~~~~~~~

TBD.

Contributing
~~~~~~~~~~~~

Pull requests and issues are happily welcome!

Please make sure ``make format`` (depends on `clang-format-5 <https://clang.llvm.org/docs/ClangFormat.html>`_) has been executed against any PRs before being published.

Community
~~~~~~~~~

Qrack and VM6502Q have a development community on the `Advanced Computing Topics <https://discord.gg/yDZBuhu>`_ discord server on channel #qrack.  Come join us!

Theory
======

Foundational Material
---------------------

Quantum Bit Simulation
----------------------

Implementation
==============

:cpp:class:`Qrack::CoherentUnit`
--------------------------------

VM6502Q Opcodes
---------------

CC65
----

C Syntax Enhancements
~~~~~~~~~~~~~~~~~~~~~


Old Text
========

Primarily, this documentation teaches enough practical quantum computation and emulation theory that one can understand the implementation of all methods in Qrack. This introduction contains an overview of the general methods whereby Qrack implements its gate and register functionality.

Quantum Bit Permutation Basis Overview
--------------------------------------

Like classical bits, a set of qubits has a maximal representation as the permutation of bits. (An 8 bit byte has 256 permutations, commonly numbered 0 to 255, as does an 8 bit qubyte.) Additionally, the state of a qubyte is fully specified in terms of probability and phase of each permutation of qubits. This is the ":math:`|0\rangle/|1\rangle`" or "permutation basis." There are other fully descriptive bases, such as the ":math:`|+\rangle/|-\rangle`" permutation basis, which is characteristic of Hadamard gates. The notation ":math:`|x\rangle`" represents a "ket" of the "x" state in the quantum "bra-ket" notation of Dirac. It is a quantum state vector as described by Schrödinger's equation. When we say :math:`|01\rangle`, we mean the qubit equivalent of the classical binary bit permutation "01."

The state of a two bit permutation can be described as follows: where one in the set of variables ":math:`x_0, x_1, x_2,` and :math:`x_3`" is equal to 1 and the rest are equal to zero, the state of the bit permutation can always be described by:

.. math:: |\psi\rangle = x_0 |00\rangle + x_1 |01\rangle + x_2 |10\rangle + x_3 |11\rangle
   :label: psi_prob

.. Syntax Highlight fixing comment: `|

One of the leading variables is always 1 and the rest are always 0. That is, the state of the classical bit combination is always exactly one of :math:`|00\rangle, |01\rangle, |10\rangle,` or :math:`|11\rangle,` and is not probabilistic in it's value.

However, quantum bit's can be represented probabilistically, in which the sum of probabilities of states should be 100% or 1. For example, this suggests splitting x_0 and x_1 into 1/2 and 1/2 to represent a potential :math:`|\psi\rangle`, but Schrödinger's equation actually requires us to split into :math:`1/\sqrt{2}` and :math:`1/\sqrt{2}` to get 100% probability, like so,

.. math:: |\psi\rangle = \frac{1}{\sqrt{2}} |00\rangle + \frac{1}{\sqrt{2}} |10\rangle,

.. Syntax Highlight fixing comment: `|

where the leading coefficients are ultimately squared - more accurately: multiplied by their complex conjugate. This is a valid description of a 2 qubit permutation.

Complex Number States
---------------------

The equation :eq:`psi_prob` given above encompasses all possible states of a 2 qubit combination, when :math:`x_n` are constrained so that the total probability of all states adds up to one. However, the domain of the :math:`x_n` variables must also be the complex numbers. This is also a valid state, for example:

.. math:: |\psi\rangle = \frac{1+i}{2 \sqrt{2}} |00\rangle + \frac{1-i}{2 \sqrt{2}} |10\rangle

.. Syntax Highlight fixing comment: `|

where "i" is defined as the :math:`\sqrt(-1)`. This imparts "phase" to each permutation state vector component like :math:`|00\rangle` or :math:`|10\rangle` - which are "eigenstates". Phase and probability of permutation state fully (but not uniquely) specify the state of a coherent set of qubits.

:cpp:class:`Qrack::CoherentUnit` Qubit Simulation
-------------------------------------------------

For N bits, there are :math:`2^N` permutation basis "eigenstates" that with probability normalization and phase fully describe every possible quantum state of the N qubits. A :cpp:class:`Qrack::CoherentUnit` tracks the :math:`2^N` dimensional state vector of eigenstate components, each permutation carrying probability and phase. It optimizes certain register-like methods by operating in parallel over the "entanglements" of these permutation basis states. For example, the state

.. math:: |\psi\rangle = \frac{1}{\sqrt{2}} |00\rangle + \frac{1}{\sqrt{2}} |11\rangle

.. Syntax Highlight fixing comment: `|

has a probability of both bits being 1 or else both bits being 0, but it has no independent probability for the bits being different, when measured. If this state is acted on by an ``X`` or ``NOT`` gate on the left qubit we need only act on the states entangled into the original state.

For example, when acted on by an ``X`` gate on the left bit:

.. math:: |\psi_0\rangle = \frac{1}{\sqrt{2}} |00\rangle + \frac{1}{\sqrt{2}} |11\rangle \Rightarrow \frac{1}{\sqrt{2}} |10\rangle + \frac{1}{\sqrt{2}} |01\rangle

.. Syntax Highlight fixing comment: `|

In the permutation basis, "entanglement" is as simple as the ability to restrain bit combinations in specifying an arbitrary :math:`|\psi\rangle` state.

.. TODO: This section is a bit ambiguous.  What is meant by paired?  How is
         this actually implemented mathematically and programmatically?

In Qrack, simple gates are represented by small complex number matrices, generally with :math:`2\times2` components, that act on pairings of state vector components with the target qubit being 0 or 1 and all other qubits being held fixed in a loop iteration. For example, in an 8 qubit system, acting on a single bit gate on the leftmost qubit, these two states become paired:

.. math::
    &|00101111\rangle \Rightarrow \\
    &|10101111\rangle

Similarly, these states also become paired:

.. math::
    &|00101100\rangle \Rightarrow \\
    &|10101100\rangle

And so on for all states in which the seven uninvolved bits are kept the same, but 0 and 1 states are paired for the bit acted on by the gate.

This covers the entire permutation basis, a full description of all possible quantum states of the :cpp:class:`Qrack::CoherentUnit`, with pairs of two state vector components acted on by a :math:`2\times2` matrix. For example, for the ``Z`` gate, acting it on a single bit is equivalent to multiplying a single bit state vector by this matrix:

Basic Gate Operations
---------------------
.. math::
   :label: zgate

   \begin{pmatrix}
   1 & 0\\
   0 & 1\\
   \end{pmatrix}

Equation :eq:`zgate` is a standard ``Z`` gate matrix.

The single qubit state vector has two components:

.. math::
   :label: bitvec

   \begin{pmatrix}
   x_0\\
   x_1\\
   \end{pmatrix}

Equation :eq:`bitvec` represents the permutations of a single qubit.

These ":math:`x_0`" and ":math:`x_1`" are the same coefficients as from :eq:`psi_prob`.

The action of a gate is a matrix multiplication:

.. math::
   :label: zgatemult

   \begin{pmatrix}
   1 & 0\\
   0 & 1\\
   \end{pmatrix}
   \begin{pmatrix}
   x_0\\
   x_1\\
   \end{pmatrix}
   =
   \begin{pmatrix}
   x_0\\
   -x_1\\
   \end{pmatrix}.

.. TODO: This concept of 'pairing' needs expansion, so that
         optimizations/processes as described below.  That would hopefully make
         this example a little clearer.

For 2 qubits, we can form 4x4 matrices to act on 4 permutation eigenstates. For 3 qubits, we can form 8x8 matrices to act on 8 permutation eigenstates, and so on. However, for gates acting on single bits in states with large numbers of qubits, it is actually not necessary to carry out any matrix multiplication larger than a :math:`2\times2` matrix acting on a sub-state vector of 2 components. We pair all permutation state vector components where all qubits are the same same, except for the one bit being acted on, for which we pair 0 and 1. For example, acting on the leftmost qubit,

    :math:`|00100011\rangle` is paired with :math:`|10100011\rangle`,

and

    :math:`|00101011\rangle` is paired with :math:`|10101011\rangle`,

and

    :math:`|01101011\rangle` is paired with :math:`|11101011\rangle`,

and we can carry out the gate in terms of only :math:`2\times2` complex number matrix multiplications, which is a massive optimization and "embarrassingly parallel."

.. TODO: For comments like these, include links to OpenCL documentation or to
         an additional section later in the document that details
         optimizations.

(Further, Qrack already employs POSIX thread type parallelism, SIMD parallelism for complex number operations, and kernel-type GPU parallelism.)

For register-like operations, we can optimize beyond this level for single bit gates. If a virtual quantum chip has multiple registers that can be entangled, by requirements of the minimum full physical description of a quantum mechanical state, the registers must usually be all contained in a single :cpp:class:`Qrack::CoherentUnit`. So, for 2 8-bit registers, we might have one 16-bit :cpp:class:`Qrack::CoherentUnit`.

.. TODO: Clarify: 'sieve out'.

For a bitwise ``NOT`` or ``X`` operation on one register, we can take an initial entangled state and sieve out initial register states to be mapped to final register states. For example, say we start with an entangled state:

.. math:: |\psi\rangle = \frac{1}{\sqrt{2}} |(01010101)\ (11111110)\rangle - \frac{1}{\sqrt{2}} |(10101010)\ (00000000)\rangle

.. Syntax Highlight fixing comment: `|

.. TODO: Clarify: normalization

The registers are "entangled" so that only two possible states can result from measurement; if we measure any single bit - except the right-most, in this example - we collapse into one of these two states, adjusting the normalization so that only one state remains in the full description of the quantum state.

In general, measuring a single bit might only partially collapse the entanglement, as more than one state could potentially be consistent with the same qubit measurement outcome as 0 or 1. This is the case for the right-most bit; measuring it from this example initial state will always yield "0" and tell us nothing else about the overall permutation state, leaving the state uncollapsed. Measuring any bit except the right-most will collapse the entire set of bits into a single permutation.)

Say we want to apply a bitwise ``NOT`` or ``X`` operation on the right-hand register of 8 bits. We simply apply the ``NOT`` operation simultaneously on all of the right-hand bits in all entangled input states:

.. math:: |\psi_0\rangle = \frac{1}{\sqrt{2}} |(01010101)\ (11111110)\rangle - \frac{1}{\sqrt{2}} |(10101010)\ (00000000)\rangle

.. TODO: Replace the line of text below with the actual line of code that'd be used.

(acted on by a bitwise NOT or X on the right-hand 8 bit register becomes)

.. math:: |\psi_1\rangle = \frac{1}{\sqrt{2}} |(01010101)\ (00000001)\rangle - \frac{1}{\sqrt{2}} |(10101010)\ (11111111)\rangle

.. Syntax Highlight fixing comment: `|

:cpp:class:`Qrack::CoherentUnit` Gate Implementations
-----------------------------------------------------

This is again "embarrassingly parallel." Some bits are completely uninvolved and these bits are passed unchanged in each state from input to output. Bits acted on by the register operation have a one-to-one mapping between input and states. This can all be handled via transformation via bit masks on the input state permutation index.

.. TODO: I think you're saying here that the various x_i change but not the nature of the overall equation.  While true, this doesn't lead naturally to how the implementation actually handles those various x_i values.

And, in fact, bits are not rearranged in the state vector at all; it is the ":math:`x_n`" complex number coefficients which are rearranged according to this bitmask transformation and mapping of the input state to the output state. (The coefficient ":math:`x_i`" of state :math:`|(01010101)\ (11111110)\rangle` is switched for the coefficient ":math:`x_j`" of state :math:`|(01010101)\ (00000001)\rangle`, and only the coefficients are rearranged, with a mapping that's determined via bitmask transformations.) This is almost the entire principle behind the algorithms for optimized register-like methods in Qrack. Also, as a point of algorithmic optimization, if N bits are known to have a fixed value like 0, we can often also completely skip permutations where their value would be 1, dividing the number of permutation states we need to iterate over in total by a factor of :math:`2^N`. This optimization is again handled in terms of bitmasks and bitshifts. See also the register-wise :cpp:func:`Qrack::CoherentUnit::X()` gate implementation for inline documentation on this general algorithm.

Quantum gates are represented by "unitary" matrices. Unitary matrices preserve the norm (length) of state vectors. Quantum physically observable quantities are associated with "Hermitian" unitary matrices, which are equal to their own conjugate transpose. Not all gates are Hermitian or associated with quantum observables, like general rotation operators. (Three dimensions of spin can be physically measured; the act of rotating spin along these axes is not associated with independent measurable quantities.)

.. TODO: This is a sentence that should be better at the top, perhaps?

The Qrack project is targeted to efficient and practical classical emulation of ideal, noiseless systems of qubits, and so does not concern itself with hardware noise, error correction, or restraining emulation to gates which have already been realized in physical hardware. If a hypothetical gate is at least unitary, and if it is logically expedient for quantum emulation, the design intent of Qrack permits it as a method in the API.

.. TODO: It's important to specify why these pseudo-quantum operations are
         present, and whether or not they taint all of the related
         implementation work (moving it out of the 'feasible' space) or if
         they're provided for diagnostic or debugging capabilities only.

Additionally, as Qrack targets classical emulation of quantum hardware, certain convenience methods can be employed in classical emulation which are not physically or practically attainable in quantum hardware, such as the "cloning" of arbitrary pure quantum states and the direct nondestructive measurement of probability and phase. Members of this limited set of convenience methods are marked "PSEUDO-QUANTUM" in the API reference and need not be employed at all.

API Documentation
===========================

The API documentation is contained in :doc:`api/coherent_unit`.

Citations and Footnotes
=======================

.. [MOS-6502] https://en.wikipedia.org/wiki/MOS_Technology_6502
.. [Grover] https://en.wikipedia.org/wiki/Grover%27s_algorithm
.. [CC65] http://cc65.github.io/doc/

