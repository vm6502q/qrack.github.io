:orphan:

.. Copyright (c) 2018

Qrack::CoherentUnit
===================

Defined in `qregister.hpp <https://github.com/vm6502q/qrack/blob/master/qregister.hpp>`_.

.. doxygenclass:: Qrack::CoherentUnit
    :project: qrack

Creating a CoherentUnit
-----------------------

There's two primary implementations of a ``CoherentUnit``:

.. doxygenenum:: CoherentUnitEngine

These enums can be passed to an allocator to create a ``CoherentUnit`` of that specified implementation type:

.. doxygenfunction:: CreateCoherentUnit

Constructors
------------

.. doxygenfunction:: CoherentUnit(bitLenInt)

.. doxygenfunction:: CoherentUnit(bitLenInt, bitCapInt)

.. doxygenfunction:: CoherentUnit(const CoherentUnit&)

Members
-------

.. doxygenvariable:: stateVec

Configuration Methods
---------------------------------

.. doxygenfunction:: SetRandomSeed

.. doxygenfunction:: GetQubitCount

.. doxygenfunction:: GetMaxQPower

State Manipulation Methods
--------------------------

.. doxygenfunction:: CloneRawState

.. doxygenfunction:: SetPermutation

.. doxygenfunction:: SetQuantumState

.. doxygenfunction:: Cohere

.. doxygenfunction:: Decohere

.. doxygenfunction:: Dispose

.. doxygenfunction:: Prob

.. doxygenfunction:: ProbAll

.. doxygenfunction:: ProbArray

Quantum Gates
-------------

.. note:: Most gates offer both a single-bit version taking just the index to the qubit, as well as a register-spanning variant for convienence and performance that performs the gate across a sequence of bits.

Single Register Gates
~~~~~~~~~~~~~~~~~~~~~

.. doxygenfunction:: AND(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CLAND(bitLenInt, bool, bitLenInt)
.. doxygenfunction:: OR(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CLOR(bitLenInt, bool, bitLenInt)
.. doxygenfunction:: XOR(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CLXOR(bitLenInt, bool, bitLenInt)

.. doxygenfunction:: H(bitLenInt)
.. doxygenfunction:: M(bitLenInt)
.. doxygenfunction:: X(bitLenInt)

.. doxygenfunction:: Y(bitLenInt)
.. doxygenfunction:: Z(bitLenInt)
.. doxygenfunction:: CY(bitLenInt, bitLenInt)
.. doxygenfunction:: CZ(bitLenInt, bitLenInt)
.. doxygenfunction:: RT(double, bitLenInt)

.. doxygenfunction:: RTDyad(int, int, bitLenInt)
.. doxygenfunction:: RX(double, bitLenInt)
.. doxygenfunction:: RXDyad(int, int, bitLenInt)
.. doxygenfunction:: CRX(double, bitLenInt, bitLenInt)
.. doxygenfunction:: CRXDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: RY(double, bitLenInt)
.. doxygenfunction:: RYDyad(int, int, bitLenInt)
.. doxygenfunction:: CRY(double, bitLenInt, bitLenInt)
.. doxygenfunction:: CRYDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: RZ(double, bitLenInt)
.. doxygenfunction:: RZDyad(int, int, bitLenInt)
.. doxygenfunction:: CRZ(double, bitLenInt, bitLenInt)
.. doxygenfunction:: CRZDyad(int, int, bitLenInt, bitLenInt)

Register-wide Gates
~~~~~~~~~~~~~~~~~~~

.. doxygenfunction:: AND(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CLAND(bitLenInt, bitCapInt, bitLenInt, bitLenInt)
.. doxygenfunction:: OR(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CLOR(bitLenInt, bitCapInt, bitLenInt, bitLenInt)
.. doxygenfunction:: XOR(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CLXOR(bitLenInt, bitCapInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CCNOT
.. doxygenfunction:: AntiCCNOT
.. doxygenfunction:: CNOT(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CNOT(bitLenInt, bitLenInt)
.. doxygenfunction:: AntiCNOT
.. doxygenfunction:: H(bitLenInt, bitLenInt)
.. doxygenfunction:: M(bitLenInt, bitLenInt)
.. doxygenfunction:: X(bitLenInt, bitLenInt)
.. doxygenfunction:: Y(bitLenInt, bitLenInt)
.. doxygenfunction:: Z(bitLenInt, bitLenInt)
.. doxygenfunction:: CY(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CZ(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: RT(double, bitLenInt, bitLenInt)
.. doxygenfunction:: RTDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: RX(double, bitLenInt, bitLenInt)
.. doxygenfunction:: RXDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: CRX(double, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CRXDyad(int, int, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: RY(double, bitLenInt, bitLenInt)
.. doxygenfunction:: RYDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: CRY(double, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CRYDyad(int, int, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: RZ(double, bitLenInt, bitLenInt)
.. doxygenfunction:: RZDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: CRZ(double, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: CRZDyad(int, int, bitLenInt, bitLenInt, bitLenInt)

Internal Utility Methods
------------------------

.. doxygenfunction:: Apply2x2

