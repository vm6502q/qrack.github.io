:orphan:

.. _installing-opencl-reference:

Installing OpenCL
=================

VMWare
------

#.  Download the `AMD APP SDK <https://developer.amd.com/amd-accelerated-parallel-processing-app-sdk/>`_
#.  Install it.
#.  Add symlinks for ``/opt/AMDAPPSDK-3.0/lib/x86_64/sdk/libOpenCL.so.1`` to ``/usr/lib``
#.  Add symlinks for ``/opt/AMDAPPSDK-3.0/lib/x86_64/sdk/libamdocl64.so`` to ``/usr/lib``
#.  Make sure ``clinfo`` reports back that there is a valid backend to use (anything other than an error should be fine).
#.  Adjust the ``Makefile`` to have the appropriate search paths, if they are not already correct.


