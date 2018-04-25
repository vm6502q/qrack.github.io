import subprocess, os, sys

# -- Doxygen Integration through Breath --------------------------------------

def run_doxygen(repo):
    """Run the doxygen make command in the designated folder"""

    try:
        rc = subprocess.call("git clone https://github.com/vm6502q/{0}.git /tmp/{0}".format(repo), shell=True)
        if rc < 0:
            sys.stderr.write("failed to clone repo {0}: {1}, {2}".format(repo))
            return
    except OSError as e:
        sys.stderr.write("git clone {0} failed: {1}".format(repo, e))
        return
    sys.stderr.write("Doxygen: git clone for {0} succeeded\n".format(repo))


    try:
        retcode = subprocess.call("cd /tmp/{0}; doxygen doxygen.config".format(repo), shell=True)
        if retcode < 0:
            sys.stderr.write("doxygen terminated by signal %s" % (-retcode))
            return
    except OSError as e:
        sys.stderr.write("doxygen run for {0} failed: {1}".format(repo, e))
        return
    sys.stderr.write("Doxygen: doxygen {0} succeeded\n".format(repo))

    try:
        retcode = subprocess.call("mkdir -p _build/html/_static/doxygen; cp -r /tmp/{0}/doc/html/* _build/html/_static/doxygen".format(repo), shell=True)
        if retcode < 0:
            sys.stderr.write("copy terminated by signal %s" % (-retcode))
            return
    except OSError as e:
        sys.stderr.write("doxygen run for {0} failed: {1}".format(repo, e))
        return
    sys.stderr.write("Doxygen: copy for {0} succeeded\n".format(repo))
