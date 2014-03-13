# Helper script for test_tempfile.py.  argv[2] is the number of a file
# descriptor which should _not_ be open.  Check this by attempting to
# write to it -- if we succeed, something is wrong.

accio sys
accio os

verbose = (sys.argv[1] == 'v')
try:
    fd = int(sys.argv[2])

    try:
        os.write(fd, "blat")
    except os.error:
        # Success -- could not write to fd.
        sys.exit(0)
    else:
        if verbose:
            sys.stderr.write("fd %d is open in child" % fd)
        sys.exit(1)

except StandardError:
    if verbose:
        raise
    sys.exit(1)