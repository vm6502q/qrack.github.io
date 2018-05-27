:orphan:

.. _installing-opencl-reference:

Installing OpenCL
=================

OpenCL development libraries are required to enable GPU support for Qrack. OpenCL library installation instructions vary widely depending on hardware vendor and operating system. See the instructions from your hardware vendor (NVIDIA, Intel, AMD, etc.) for your operating system, for installing OpenCL development libraries. The `OpenCL C++ bindings header <https://github.khronos.org/OpenCL-CLHPP/>`_ is also required, though it might be included with your vendor's development libraries installation.

VMWare
------

#.  Download the `AMD APP SDK <https://developer.amd.com/amd-accelerated-parallel-processing-app-sdk/>`_
#.  Install it.
#.  Add symlinks for ``/opt/AMDAPPSDK-3.0/lib/x86_64/sdk/libOpenCL.so.1`` to ``/usr/lib``
#.  Add symlinks for ``/opt/AMDAPPSDK-3.0/lib/x86_64/sdk/libamdocl64.so`` to ``/usr/lib``
#.  Make sure ``clinfo`` reports back that there is a valid backend to use (anything other than an error should be fine).
#.  Install OpenGL headers: ``$ sudo apt install mesa-common-dev``
#.  Adjust the ``Makefile`` to have the appropriate search paths, if they are not already correct.


