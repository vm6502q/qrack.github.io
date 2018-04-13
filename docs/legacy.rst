Old Text
========

Primarily, this documentation teaches enough practical quantum computation and emulation theory that one can understand the implementation of all methods in Qrack. This introduction contains an overview of the general methods whereby Qrack implements its gate and register functionality.

Quantum Bit Permutation Basis Overview
--------------------------------------

Like classical bits, a set of qubits has a maximal representation as the permutation of bits. (An 8 bit byte has 256 permutations, commonly numbered 0 to 255, as does an 8 bit qubyte.) Additionally, the state of a qubyte is fully specified in terms of probability and phase of each permutation of qubits. This is the ":math:`\rvert0\rangle/\rvert1\rangle`" or "permutation basis." There are other fully descriptive bases, such as the ":math:`\rvert+\rangle/\rvert-\rangle`" permutation basis, which is characteristic of Hadamard gates. The notation ":math:`\rvertx\rangle`" represents a "ket" of the "x" state in the quantum "bra-ket" notation of Dirac. It is a quantum state vector as described by Schrödinger's equation. When we say :math:`\rvert01\rangle`, we mean the qubit equivalent of the classical binary bit permutation "01."

The state of a two bit permutation can be described as follows: where one in the set of variables ":math:`x_0, x_1, x_2,` and :math:`x_3`" is equal to 1 and the rest are equal to zero, the state of the bit permutation can always be described by:

.. math:: \rvert\psi\rangle = x_0 \rvert00\rangle + x_1 \rvert01\rangle + x_2 \rvert10\rangle + x_3 \rvert11\rangle
   :label: legacy_psi_prob

One of the leading variables is always 1 and the rest are always 0. That is, the state of the classical bit combination is always exactly one of :math:`\rvert00\rangle, \rvert01\rangle, \rvert10\rangle,` or :math:`\rvert11\rangle,` and is not probabilistic in it's value.

However, quantum bit's can be represented probabilistically, in which the sum of probabilities of states should be 100% or 1. For example, this suggests splitting :math:`x_0` and :math:`x_1` into :math:`1/2` and :math:`1/2` to represent a potential :math:`\rvert\psi\rangle`, but Schrödinger's equation actually requires us to split into :math:`1/\sqrt{2}` and :math:`1/\sqrt{2}` to get 100% probability, like so,

.. math:: \rvert\psi\rangle = \frac{1}{\sqrt{2}} \rvert00\rangle + \frac{1}{\sqrt{2}} \rvert10\rangle,

where the leading coefficients are ultimately squared - more accurately: multiplied by their complex conjugate. This is a valid description of a 2 qubit permutation.

Complex Number States
---------------------

The equation :eq:`legacy_psi_prob` given above encompasses all possible states of a 2 qubit combination, when :math:`x_n` are constrained so that the total probability of all states adds up to one. However, the domain of the :math:`x_n` variables must also be the complex numbers. This is also a valid state, for example:

.. math:: \rvert\psi\rangle = \frac{1+i}{2 \sqrt{2}} \rvert00\rangle + \frac{1-i}{2 \sqrt{2}} \rvert10\rangle

where "i" is defined as the :math:`\sqrt(-1)`. This imparts "phase" to each permutation state vector component like :math:`\rvert00\rangle` or :math:`\rvert10\rangle` - which are "eigenstates". Phase and probability of permutation state fully (but not uniquely) specify the state of a coherent set of qubits.

:cpp:class:`Qrack::CoherentUnit` Qubit Simulation
-------------------------------------------------

For N bits, there are :math:`2^N` permutation basis "eigenstates" that with probability normalization and phase fully describe every possible quantum state of the N qubits. A :cpp:class:`Qrack::CoherentUnit` tracks the :math:`2^N` dimensional state vector of eigenstate components, each permutation carrying probability and phase. It optimizes certain register-like methods by operating in parallel over the "entanglements" of these permutation basis states. For example, the state

.. math:: \rvert\psi\rangle = \frac{1}{\sqrt{2}} \rvert00\rangle + \frac{1}{\sqrt{2}} \rvert11\rangle

has a probability of both bits being 1 or else both bits being 0, but it has no independent probability for the bits being different, when measured. If this state is acted on by an ``X`` or ``NOT`` gate on the left qubit we need only act on the states entangled into the original state.

For example, when acted on by an ``X`` gate on the left bit:

.. math:: \rvert\psi_0\rangle = \frac{1}{\sqrt{2}} \rvert00\rangle + \frac{1}{\sqrt{2}} \rvert11\rangle \Rightarrow \frac{1}{\sqrt{2}} \rvert10\rangle + \frac{1}{\sqrt{2}} \rvert01\rangle

In the permutation basis, "entanglement" is as simple as the ability to restrain bit combinations in specifying an arbitrary :math:`\rvert\psi\rangle` state.

.. TODO: This section is a bit ambiguous.  What is meant by paired?  How is
         this actually implemented mathematically and programmatically?

In Qrack, simple gates are represented by small complex number matrices, generally with :math:`2\times2` components, that act on pairings of state vector components with the target qubit being 0 or 1 and all other qubits being held fixed in a loop iteration. For example, in an 8 qubit system, acting on a single bit gate on the leftmost qubit, these two states become paired:

.. math::
    &\rvert00101111\rangle \Rightarrow \\
    &\rvert10101111\rangle

Similarly, these states also become paired:

.. math::
    &\rvert00101100\rangle \Rightarrow \\
    &\rvert10101100\rangle

And so on for all states in which the seven uninvolved bits are kept the same, but 0 and 1 states are paired for the bit acted on by the gate.

This covers the entire permutation basis, a full description of all possible quantum states of the :cpp:class:`Qrack::CoherentUnit`, with pairs of two state vector components acted on by a :math:`2\times2` matrix. For example, for the ``Z`` gate, acting it on a single bit is equivalent to multiplying a single bit state vector by this matrix:

Basic Gate Operations
---------------------
.. math::
   :label: legacy_zgate

   \begin{pmatrix}
   1 & 0\\
   0 & 1\\
   \end{pmatrix}

Equation :eq:`legacy_zgate` is a standard ``Z`` gate matrix.

The single qubit state vector has two components:

.. math::
   :label: legacy_bitvec

   \begin{pmatrix}
   x_0\\
   x_1\\
   \end{pmatrix}

Equation :eq:`legacy_bitvec` represents the permutations of a single qubit.

These ":math:`x_0`" and ":math:`x_1`" are the same coefficients as from :eq:`legacy_psi_prob`.

The action of a gate is a matrix multiplication:

.. math::
   :label: legacy_zgatemult

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

    :math:`\rvert00100011\rangle` is paired with :math:`\rvert10100011\rangle`,

and

    :math:`\rvert00101011\rangle` is paired with :math:`\rvert10101011\rangle`,

and

    :math:`\rvert01101011\rangle` is paired with :math:`\rvert11101011\rangle`,

and we can carry out the gate in terms of only :math:`2\times2` complex number matrix multiplications, which is a massive optimization and "embarrassingly parallel."

.. TODO: For comments like these, include links to OpenCL documentation or to
         an additional section later in the document that details
         optimizations.

(Further, Qrack already employs POSIX thread type parallelism, SIMD parallelism for complex number operations, and kernel-type GPU parallelism.)

For register-like operations, we can optimize beyond this level for single bit gates. If a virtual quantum chip has multiple registers that can be entangled, by requirements of the minimum full physical description of a quantum mechanical state, the registers must usually be all contained in a single :cpp:class:`Qrack::CoherentUnit`. So, for 2 8-bit registers, we might have one 16-bit :cpp:class:`Qrack::CoherentUnit`.

.. TODO: Clarify: 'sieve out'.

For a bitwise ``NOT`` or ``X`` operation on one register, we can take an initial entangled state and sieve out initial register states to be mapped to final register states. For example, say we start with an entangled state:

.. math:: \rvert\psi\rangle = \frac{1}{\sqrt{2}} \rvert(01010101)\ (11111110)\rangle - \frac{1}{\sqrt{2}} \rvert(10101010)\ (00000000)\rangle

.. TODO: Clarify: normalization

The registers are "entangled" so that only two possible states can result from measurement; if we measure any single bit - except the right-most, in this example - we collapse into one of these two states, adjusting the normalization so that only one state remains in the full description of the quantum state.

In general, measuring a single bit might only partially collapse the entanglement, as more than one state could potentially be consistent with the same qubit measurement outcome as 0 or 1. This is the case for the right-most bit; measuring it from this example initial state will always yield "0" and tell us nothing else about the overall permutation state, leaving the state uncollapsed. Measuring any bit except the right-most will collapse the entire set of bits into a single permutation.)

Say we want to apply a bitwise ``NOT`` or ``X`` operation on the right-hand register of 8 bits. We simply apply the ``NOT`` operation simultaneously on all of the right-hand bits in all entangled input states:

.. math:: \rvert\psi_0\rangle = \frac{1}{\sqrt{2}} \rvert(01010101)\ (11111110)\rangle - \frac{1}{\sqrt{2}} \rvert(10101010)\ (00000000)\rangle

.. TODO: Replace the line of text below with the actual line of code that'd be used.

(acted on by a bitwise NOT or X on the right-hand 8 bit register becomes)

.. math:: \rvert\psi_1\rangle = \frac{1}{\sqrt{2}} \rvert(01010101)\ (00000001)\rangle - \frac{1}{\sqrt{2}} \rvert(10101010)\ (11111111)\rangle

:cpp:class:`Qrack::CoherentUnit` Gate Implementations
-----------------------------------------------------

This is again "embarrassingly parallel." Some bits are completely uninvolved and these bits are passed unchanged in each state from input to output. Bits acted on by the register operation have a one-to-one mapping between input and states. This can all be handled via transformation via bit masks on the input state permutation index.

.. TODO: I think you're saying here that the various x_i change but not the nature of the overall equation.  While true, this doesn't lead naturally to how the implementation actually handles those various x_i values.

And, in fact, bits are not rearranged in the state vector at all; it is the ":math:`x_n`" complex number coefficients which are rearranged according to this bitmask transformation and mapping of the input state to the output state. (The coefficient ":math:`x_i`" of state :math:`\rvert(01010101)\ (11111110)\rangle` is switched for the coefficient ":math:`x_j`" of state :math:`\rvert(01010101)\ (00000001)\rangle`, and only the coefficients are rearranged, with a mapping that's determined via bitmask transformations.) This is almost the entire principle behind the algorithms for optimized register-like methods in Qrack. Also, as a point of algorithmic optimization, if N bits are known to have a fixed value like 0, we can often also completely skip permutations where their value would be 1, dividing the number of permutation states we need to iterate over in total by a factor of :math:`2^N`. This optimization is again handled in terms of bitmasks and bitshifts. See also the register-wise :cpp:func:`Qrack::CoherentUnit::X()` gate implementation for inline documentation on this general algorithm.

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
