:orphan:

.. Copyright (c) 2018

QInterface
========================

Defined in `qinterface.hpp <https://github.com/vm6502q/qrack/blob/master/include/qinterface.hpp>`_.

This provides a basic interface with a wide-ranging set of functionality 

.. doxygenclass:: Qrack::QInterface
    :project: qrack

Creating a QInterface
-----------------------

There's three primary implementations of a ``QInterface``:

.. doxygenenum:: QInterfaceEngine

These enums can be passed to an allocator to create a ``QInterface`` of that specified implementation type:

.. doxygenfunction:: Qrack::CreateQuantumInterface

Constructors
------------

.. doxygenfunction:: Qrack::QInterface::QInterface(bitLenInt)

.. doxygenfunction:: Qrack::QInterface::QInterface(bitLenInt, bitCapInt)

.. doxygenfunction:: Qrack::QInterface::QInterface(const QInterface&)

Members
-------

.. doxygenvariable:: stateVec

Configuration Methods
---------------------------------

.. doxygenfunction:: Qrack::QInterface::GetQubitCount

.. doxygenfunction:: Qrack::QInterface::GetMaxQPower

State Manipulation Methods
--------------------------

.. doxygenfunction:: Qrack::QInterface::SetPermutation

.. doxygenfunction:: Qrack::QInterface::SetQuantumState

.. doxygenfunction:: Qrack::QInterface::Cohere(QInterfacePtr)
.. doxygenfunction:: Qrack::QInterface::Cohere(std::vector<QInterfacePtr>)

.. doxygenfunction:: Qrack::QInterface::Decohere

.. doxygenfunction:: Qrack::QInterface::Dispose

.. doxygenfunction:: Qrack::QInterface::Prob

.. doxygenfunction:: Qrack::QInterface::ProbAll

.. doxygenfunction:: Qrack::QInterface::ProbArray

.. doxygenfunction:: Qrack::QInterface::Swap(bitLenInt, bitLenInt)

.. doxygenfunction:: Qrack::QInterface::Swap(bitLenInt, bitLenInt, bitLenInt)

.. doxygenfunction:: Qrack::QInterface::Reverse(bitLenInt, bitLenInt)

Quantum Gates
-------------

.. note:: Most gates offer both a single-bit version taking just the index to the qubit, as well as a register-spanning variant for convienence and performance that performs the gate across a sequence of bits.

Single Register Gates
~~~~~~~~~~~~~~~~~~~~~

.. doxygenfunction:: Qrack::QInterface::AND(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CLAND(bitLenInt, bool, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::OR(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CLOR(bitLenInt, bool, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::XOR(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CLXOR(bitLenInt, bool, bitLenInt)

.. doxygenfunction:: Qrack::QInterface::H(bitLenInt)
.. doxygenfunction:: Qrack::QInterface::M(bitLenInt)
.. doxygenfunction:: Qrack::QInterface::X(bitLenInt)

.. doxygenfunction:: Qrack::QInterface::Y(bitLenInt)
.. doxygenfunction:: Qrack::QInterface::Z(bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CY(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CZ(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RT(double, bitLenInt)

.. doxygenfunction:: Qrack::QInterface::RTDyad(int, int, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RX(double, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RXDyad(int, int, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRX(double, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRXDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RY(double, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RYDyad(int, int, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRY(double, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRYDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RZ(double, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RZDyad(int, int, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRZ(double, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRZDyad(int, int, bitLenInt, bitLenInt)

Register-wide Gates
~~~~~~~~~~~~~~~~~~~

.. doxygenfunction:: Qrack::QInterface::AND(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CLAND(bitLenInt, bitCapInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::OR(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CLOR(bitLenInt, bitCapInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::XOR(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CLXOR(bitLenInt, bitCapInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CCNOT(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::AntiCCNOT(bitLenInt, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CNOT(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CNOT(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::AntiCNOT(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::H(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::MReg(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::X(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::Y(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::Z(bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CY(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CZ(bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RT(double, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RTDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RX(double, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RXDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRX(double, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRXDyad(int, int, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RY(double, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RYDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRY(double, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRYDyad(int, int, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RZ(double, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::RZDyad(int, int, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRZ(double, bitLenInt, bitLenInt, bitLenInt)
.. doxygenfunction:: Qrack::QInterface::CRZDyad(int, int, bitLenInt, bitLenInt, bitLenInt)

Algorithmic Implementations
---------------------------

.. doxygenfunction:: Qrack::QInterface::QFT
.. doxygenfunction:: Qrack::QInterface::SuperposeReg8
.. doxygenfunction:: Qrack::QInterface::AdcSuperposeReg8
.. doxygenfunction:: Qrack::QInterface::SbcSuperposeReg8
