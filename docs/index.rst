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
         able to implement a QInterface, or even understand how QInterface
         simulates a qubit.
         
         It's worth noting that it's not necessary for you to write all of this
         text yourself - referencing or directing to valuable external
         literature (but a minimum of published papers) is a very viable way of
         sharing the weight.

Introduction
------------

Qrack is a C++ quantum bit simulator, with the ability to support arbitrary numbers of entangled qubits - up to system limitations.  Suitable for embedding in other projects, the :cpp:class:`Qrack::QInterface` contains a full and performant collection of standard quantum gates, as well as variations suitable for register operations and arbitrary rotations.

As a demonstration of the :cpp:class:`Qrack::QInterface` implementation, a MOS-6502 microprocessor [MOS-6502]_ virtual machine has been modified with a set of new opcodes (:ref:`mos-6502q-opcodes`) supporting quantum operations.  The `vm6502q <https://github.com/vm6502q/vm6502q>`_ virtual machine exposes new integrated quantum opcodes such as Hadamard transforms and an X-indexed LDA, with the X register in superposition, across a page of memory.  An assembly example of a Grover's search with a simple oracle function is demonstrated in the `examples <https://github.com/vm6502q/examples>`_ repository.

Finally, a `6502 toolchain <https://github.com/vm6502q/cc65>`_ - based on `CC65 <http://cc65.github.io/doc/>`_ - has been modified and enhanced to support both the new opcodes - for the assembler - as well as :ref:`c-syntax-enhancements-ref`.  This is performed primarily as sandbox/exploratory work to help clarify what quantum computational software engineering might look like as the hardware reaches commoditization.

.. toctree::
    :maxdepth: 2
    :hidden:

    Introduction <self>
    start
    opencl
    examples
    theory
    implementation

.. toctree::
    :hidden:
    :caption: API
    :maxdepth: 2

    api/qinterface
    api/6502

.. toctree::
    :hidden:
    :caption: Doxygen
    :maxdepth: 2

    QInterface <_static/doxygen/classQrack_1_1QInterface.html#http://>
    QUnit <_static/doxygen/classQrack_1_1QUnit.html#http://>
    QEngineCPU <_static/doxygen/classQrack_1_1QEngineCPU.html#http://>
    QEngineOCL <_static/doxygen/classQrack_1_1QEngineOCL.html#http://>
    Complex16Simd <_static/doxygen/classQrack_1_1Complex16Simd.html#http://>

