#################
Qrack Performance
#################

Abstract
********

The Qrack quantum simulator is an open-source C++ high performance, general
purpose simulation supporting arbitrary numbers of entangled qubits.  While
there are a variety of other quantum simulators such as `Q#`_, `QHipster`_,
and others listed on `Quantiki`_, Qrack represents a unique offering suitable
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
optimizations.  There are some exceptions, such as IBM's _`arXiv:1710.05867`.

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

Results
*******

Summary
=======

Software
========

OpenCL
======

QUnit
=====

Systemic Analysis
*****************

Methodology
***********

Further Work
************

Conclusion
**********

Citations
*********

.. target-notes::

.. _`Q#`: http://TBD.com
.. _`QHipster`: http://TBD.com
.. _`Quantiki`: https://www.quantiki.org/wiki/list-qc-simulators
.. _`arXiv:1710.05867`: Breaking the 49-Qubit Barrier in the Simulation of Quantum Circuits - https://arxiv.org/abs/1710.05867
