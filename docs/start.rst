Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

Qrack compiles with a C++11 compiler, such as g++ or clang++, with any required compilation flags to enable the C++11 standard.

You also need CMake to build. `CMake installation instructions can be found here. <https://cmake.org/install/>`_

Optional GPU support is provided by OpenCL development libraries. See :ref:`installing-opencl-reference` for further instructions.

Checking Out
~~~~~~~~~~~~

Check out each of the major repositories into a project branch:

.. code-block:: bash

          / $ mkdir qc
          / $ cd qc
        qc/ $ git clone https://github.com/vm6502q/qrack.git
        qc/ $ git clone https://github.com/vm6502q/vm6502q.git
        qc/ $ git clone https://github.com/vm6502q/examples.git
            # Note: the cc65 repository changes live in the 6502q branch
        qc/ $ git clone https://github.com/vm6502q/cc65.git -b 6502q

            # Add a necessary symlink connecting the vm6502q project with qrack
        qc/ $ cd vm6502q && ln -s ../qrack

            # vm6502q expects the qrack buildfiles to exist in qrack/build
        qc/ $ mkdir qrack/build
        qc/ $ cd qrack/build && cmake ..
            # OR if no OpenCL support is enabled
        qc/ $ cd qrack/build && cmake -DUSE_OPENCL=OFF ..

Compiling
~~~~~~~~~

.. note::

    The ``qrack`` project supports two primary implementations: OpenCL-optimized and software-only.  See :doc:`opencl` for details on installing OpenCL on some platforms, or your appropriate OS documentation.

    If you do not have OpenCL or do not wish to use it, supply the ``USE_OPENCL=OFF`` environment to ``cmake`` when building qrack the first time, and ``ENABLE_OPENCL=0`` to ``make`` when building ``vm6502q``.

Compile in the ``vm6502q`` project.  This will build both the ``vm6502q`` emulator as well as the linked ``qrack`` project:

.. code-block:: bash

   vm6502q/ $ make
            # OR if no OpenCL is available
   vm6502q/ $ ENABLE_OPENCL=0 make

.. note::

    Qrack compiles with either double or single accuracy complex numbers. Doubles are used by default. Single float accuracy uses almost exactly half as much RAM, allowing one additional qubit. Single accuracy may also be faster or the only compatible option for certain OpenCL devices, such as accelerators. Double vectorization uses AVX, while single vectorization uses SSE 1.0.

To enable float accuracy as opposed to double, run CMake with the appropriate flag:

.. code-block:: bash

    qc/ $ cd qrack/build && cmake -DENABLE_COMPLEX8=ON ..

Testing
~~~~~~~

The qrack project has an extensive set of unittests for the various :cpp:class:`Qrack::QInterface` gates and simulator methods.  This can be executed through running the test suite in the ``qrack`` project:

.. code-block:: bash

     qrack/build/ $ make test

This may take a few minutes to complete, depending on the strength of the system executing the tests.

.. note::

    The unittests, by default, run against all supported engines.  If only a specific engine type is desired, the ``--disable-opencl`` or ``--disable-software`` command line parameters may be supplied to the ``unittest`` binary.


Embedding Qrack
~~~~~~~~~~~~~~~

The ``qrack`` project produces a ``libqrack.a`` archive, suitable for being linked into a larger binary.  See the :cpp:class:`Qrack::QInterface` documentation for API references, as well as the examples present in `the unit tests <https://github.com/vm6502q/qrack/blob/master/tests.cpp>`_.

Performance
~~~~~~~~~~~

See the extensive :doc:`performance analysis and graphs <performance>` section.

Contributing
~~~~~~~~~~~~

Pull requests and issues are happily welcome!

Please make sure ``make format`` (depends on `clang-format-5 <https://clang.llvm.org/docs/ClangFormat.html>`_) has been executed against any PRs before being published.

Community
~~~~~~~~~

Qrack and VM6502Q have a development community on the `Advanced Computing Topics <https://discord.gg/yDZBuhu>`_ discord server on channel #qrack.  Come join us!

