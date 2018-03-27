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
