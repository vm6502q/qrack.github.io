#################
Qrack Performance
#################

Abstract
********

The Qrack quantum simulator is an open-source C++ high performance, general
purpose simulation supporting arbitrary numbers of entangled qubits.  While
there are a variety of other quantum simulators such as [QSharp]_, [QHiPSTER]_,
and others listed on [Quantiki]_, Qrack represents a unique offering suitable
for applications across the field.

A selection of performance tests are identified for creating comparisons
between various quantum simulators.  These metrics are implemented and
analyzed for Qrack.  These experimentally derived results compare favorably
against theoretical boundaries, and out-perform naive implementations for many
scenarios.

Introduction
************

There are a growing number of quantum simulators available for research and
industry use.  Many of them perform quite well for smaller number of qubits,
and are suitable for non-rigorous experimental explorations.  Fewer projects
are suitable for the growing mid-tier range of experimentation in the 20-30
qubit range.

Despite the availability of a selection of implementations, very little has
been established when comparing the performance between different simulators.
Broadly, the substantial bottlenecks around memory and IO utilization have
largely preempted analysis into CPU efficiencies and algorithmic
optimizations.  There are some exceptions, such as IBM's `Breaking the
49-Qubit Barrier in the Simulation of Quantum Circuits` [Pednault2017]_ paper.

Qrack provides high performance in the 20-30 qubit range, as well as an
open-source implementation in C++ suitable for utilization in a wide variety
of projects.  As such, it is an ideal test-bed for establishing a set of
benchmarks useful for comparing performance between various quantum
simulators.

Future publications will compare the performance of Qrack against other
publicly available simulators, as rigorous implementations can be implemented.

Reader Guidance
===============

This document is largely targeted towards readers looking for a quantum
simulator that desire to establish the expected bounds for various use-cases
prior to implementation.

Disclaimers
===========

* Your Mileage May Vary - Any performance metrics here are the result of
  experiments executed on local machines; execute the supplied benchmarks on
  the desired target system for accurate performance assessments.

* Benchmarking is Hard - While we've attempted to perform clean and accurate
  results, bugs and mistakes do occur.  If flaws in process are identified,
  please let us know!

Method
******

100 timed trials of each method were run for each qubit count between 3 and 24 qubits. The average and quartile boundary values of each set of 100 were recorded and graphed. Grover's search to invert a black box subroutine, or "oracle," was similarly implemented for trials between 3 and 17 qubits. Grover's algorithm was iterated an optimal number of times, vs. qubit count, to maximize probability on a half cycle of the algorithm's period, being :math:`floor\left[\frac{\pi}{4asin\left(\sqrt{2^N}\right)}\right]` iterations for :math:`N` qubits.

The test machine has an 04WT2G Alienware motherboard with Alienware BIOS A15. Its CPU is an Intel(R) Core(TM) i7-4910MQ. Its GPU is an NVIDIA Corporation GM204M [GeForce GTX 970M]. Its operating system is Ubuntu 16.04.4 LTS. It has 24GB of 1600MHz DDR3 RAM in 8GBx2 and 4GBx2 SODIMM configuration.

Heap profiling was carried out with Valgrind Massif. Heap sampling was limited but ultimately sufficient to show statistical confidence.

Results
*******

We observed extremely close correspondence with theoretical complexity and RAM usage considerations for the behavior of all engine types. QEngineCPU and QEngineOCL require exponential time for a single gate on a coherent unit of N qubits. QUnit types with explicitly separated subsystems as per [Pednault2017]_ show constant time requirements for the same single gate.

.. image:: performance/x_single.png

.. image:: performance/cnot_single.png

QEngineCPU and QEngineOCL can perform many identical gates in parallel across entangled subsystems for about the same cost as a single gate. To test this, we can apply parallel gates at once across the full width of a coherent array of qubits. (CNOT is a two bit gate, so :math:`(N-1)/2` gates are applied to odd numbers of qubits.) Notice in these next graphs how QEngineCPU and QEngineOCL have approximately the same scaling cost as the single gate graphs above, while QUnit types show a linear trend (appearing logarithmic on an exponential axis scale):

.. image:: performance/x_all.png

.. image:: performance/cnot_all.png

Heap sampling showed high confidence adherence to theoretical expecations. Complex numbers are represented as 2 double (64-bit) accuracy floating point types, for real and imaginary components. There is one complex number per permutation in a separable subsystem of qubits. QUnit explicitly separates subsystems, while QEngine maintains complex amplitudes for all :math:`2^N` permutations of :math:`N` qubits. QEngines duplicate their state vectors once for speed and simplicity where it eases implementation.

.. image:: performance/qrack_ram.png

Grover's algorithm is a relatively ideal test case, in that it allows a minimum of abstraction in implementation while representing an ostensibly practical and common task for truly quantum computational hardware. For 1 expected correct function inversion result, there is a well-defined highest likelihood search iteration count on half a period of the algorithm for a given number of oracle input permutations to search. This graphs shows average time against qubit count for an optimal half period search:

.. image:: performance/grovers.png

[Broda2016]_ discusses how Grover's might be adapted in practicality to actually "search an unstructured database," or search an unstructured lookup table, and Qrack is also capable of applying Grover's search to a lookup table with its IndexedLDA, IndexedADC, and IndexedSBC methods. Benchmarks are not given for this arguably more practical application of the algorithm, because few other quantum computer simulator libraries implement it, yet.

A representative sample of Qrack methods were run for 100 trials per qubit as above, for parallel gates up to the full span of the qubits. Multiple bit gates spanned the full length of coherent qubits up to integer division flooring for 2 and 3 qubit gates. Taking an observed threshold of 10 to 15 qubits for API method overhead to become much larger than "noise" levels, we regressed the high qubit end of each graph for an exponential fit for time against qubits. These regression equations are presented in tables of representative samplings of the API. The results follow this equation:

.. math::
   :label: regression_eq

   [Milliseconds] = \exp \left( [Base] \left( [No. of Qubits] + [Intercept] \right) \right)

In addition to the base and intercept, the table also notes the "First Qubit" that passed the noise threshold for the high qubit end of the graph, on the basis of its :math:`R^2` statistic being just greater than or equal to :math:`0.99`. The :math:`R^2` and model p-value are also reported. Assuming a "noise" threshold, note that these equations are expected to be biased in the direction of underestimating the exponential "Base" of the relationship. "Intercept" is then an estimate of how many qubits it would take for the method to 1 millisecond on average.

The quantum Fourier transform ("QFT") is consistently the slowest register-like operation. This offers a reasonable control case, as QFT is one of the only register-like API methods implemented in terms of calls to other fundamental gate methods.

Software
========

These are a representative sample of regression equations for QEngineCPU. Testing was carried out on parallel gates across the full width of a coherent unit of quantum memory, up to integer flooring on 2 and 3 qubit gates.

.. csv-table:: Regressed QEngineCPU Speed Equations
  :header: "Method","First Qubit","Base","Intercept","R^2","p-value"
  :widths: auto
  
  "AND",13,0.672,-14.0,0.992,6.76E-12
  "ASL",14,0.725,-13.8,0.991,1.46E-10
  "CLAND",12,0.681,-11.4,0.993,2.41E-13
  "CLOR",14,0.725,-13.8,0.991,1.46E-10
  "CLXOR",14,0.725,-13.8,0.991,1.46E-10
  "CNOT",12,0.677,-14.5,0.995,4.13E-14
  "CRT",14,0.709,-13.3,0.991,1.70E-10
  "CY",13,0.681,-12.9,0.990,2.75E-11
  "INC",12,0.815,-19.0,0.996,8.70E-15
  "INCC",12,0.627,-14.3,0.992,5.44E-13
  "INCS",12,0.666,-15.1,0.991,1.12E-12
  "INCSC",12,0.629,-14.3,0.992,6.75E-13
  "IndexedADC",12,0.627,-14.0,0.995,8.37E-14
  "IndexedLDA",13,0.632,-14.9,0.992,7.39E-12
  "IndexedSBC",12,0.619,-13.3,0.991,1.07E-12
  "LSL",14,0.774,-14.6,0.990,2.17E-10
  "MReg",12,0.620,-15.2,0.993,4.56E-13
  "OR",13,0.699,-12.4,0.992,9.37E-12
  "PhaseFlip",13,0.646,-15.5,0.993,3.13E-12
  "QFT",11,0.682,-7.98,0.990,2.18E-13
  "ROL",15,0.856,-15.7,0.993,6.02E-10
  "RT",10,0.683,-9.65,0.994,1.17E-15
  "Swap",13,0.728,-14.9,0.992,7.78E-12
  "X",16,0.933,-16.2,0.991,1.88E-08
  "XOR",13,0.697,-13.5,0.992,7.01E-12  
  "Y",12,0.678,-10.9,0.992,6.35E-13
  
  

OpenCL
======

These are a representative sample of regression equations for QEngineOCL. Testing was carried out on parallel gates across the full width of a coherent unit of quantum memory, up to integer flooring on 2 and 3 qubit gates.

.. csv-table:: Regressed QEngineOCL Speed Equations
  :header: "Method","First Qubit","Base","Intercept","R^2","p-value"
  :widths: auto

  "AND",14,0.655,-13.7,0.990,2.42E-10
  "ASL",13,0.595,-13.1,0.992,8.57E-12
  "CLAND",11,0.662,-11.2,0.991,1.14E-13
  "CLOR",12,0.624,-13.4,0.993,3.60E-13
  "CLXOR",10,0.617,-13.9,0.990,2.05E-14
  "CNOT",14,0.639,-13.8,0.994,2.80E-11
  "CRT",11,0.678,-13.4,0.994,1.25E-14
  "CY",11,0.678,-13.4,0.994,1.26E-14
  "INC",14,0.642,-15.5,0.993,4.65E-11
  "INCC",13,0.598,-14.0,0.991,1.71E-11
  "INCS",14,0.642,-15.5,0.992,1.17E-10
  "INCSC",15,0.645,-14.2,0.997,3.76E-11
  "IndexedADC",14,0.592,-13.7,0.990,2.88E-10
  "IndexedLDA",15,0.624,-14.2,0.994,3.49E-10
  "IndexedSBC",14,0.614,-13.5,0.990,2.15E-10
  "LSL",13,0.606,-13.9,0.991,1.42E-11
  "MReg",12,0.603,-14.8,0.997,2.07E-15
  "OR",13,0.669,-12.4,0.991,1.78E-11
  "PhaseFlip",13,0.645,-15.6,0.990,1.96E-11
  "QFT",10,0.704,-9.18,0.991,7.80E-15
  "ROL",14,0.641,-15.5,0.992,7.35E-11
  "RT",11,0.685,-11.5,0.995,3.71E-15
  "Swap",14,0.643,-15.5,0.993,6.23E-11
  "X",14,0.642,-15.6,0.992,7.46E-11
  "XOR",14,0.650,-12.7,0.991,1.70E-10
  "Y",10,0.680,-11.7,0.994,8.93E-16

Discussion
**********

Up to a consistent deviation at low qubit counts, speed and RAM usage is well predicted by theoretical complexity considerations of the gates, up to a factor of 2 on heap usage for duplication of the state vector.

We might speculate that, at high qubit counts, the calculations operate almost entirely on heap, while system call and cache hit efficiency consistently alter the trend up until around roughly 12 qubits, on the test machine, causing the apparent inflection points observed in the graphs given above. For "software" simulation, this would be roughly consistent with the advertised 8MB cache of the i7-4910MQ. If the reduction in the slope of the trend to this point is primarily due to cache hit, about 8 fully entangled qubits would be ideal for an 8MB cache.

Further Work
************

We suggest that a good next primary target for optimizing Qrack is to allow cluster distribution of all the various engine types. Also, CPU "software" implementation parallelism relies on certain potentially expensive standard library functionality, like lambda expressions, and might still be micro-optimized. The API offers many optimized bitwise parallel operations over contiguous bit strings, but similar methods for discontiguous bit sets should be feasible with bit masks, if there is a reasonable demand for them. Further, there is still opportunity for better constant bitwise parallelism cost coverage and better explicit qubit subsystem separation in QUnit.

We will also develop and maintain systematic comparisons to published benchmarks of quantum computer simulation standard libraries, as they arise.

Conclusion
**********

Per [Pednault2017]_, explicitly separated subsystems of qubits in QUnit have a significant RAM and speed edge in many cases over the "Schrödinger algorithm" of QEngineCPU and QEngineOCL. One of Qrack's greatest new optimizations to either general algorithm is constant complexity or "free" scaling of bitwise parallelism in entangled subsystems, compared to linear complexity scaling without this optimization. Qrack gives at least reasonably efficient performance on a single node up to approximately 30 qubits, in the limit of maximal entanglement.

Citations
*********

.. target-notes::

.. [Broda2016] `Broda, Bogusław. "Quantum search of a real unstructured database." The European Physical Journal Plus 131.2 (2016): 38. <https://arxiv.org/abs/1502.04943>`_
.. [Pednault2017] `Pednault, Edwin, et al. "Breaking the 49-qubit barrier in the simulation of quantum circuits." arXiv preprint arXiv:1710.05867 (2017). <https://arxiv.org/abs/1710.05867>`_
.. [QSharp] `Q# <https://www.microsoft.com/en-us/quantum/development-kit>`_
.. [QHiPSTER] `QHipster <https://github.com/intel/Intel-QS>`_
.. [Quantiki] `Quantiki: List of QC simulators <https://www.quantiki.org/wiki/list-qc-simulators>`_
