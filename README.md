# PhyBio++

Biological applications of phase-field modeling with steroids! Pythonic wrapper and C++ core code for performance!

## Instructions

In order to use this library in python you need to either add the directory of _PhyBiopp.so and PhyBiopp.py to the path variable:

    import sys
    import os
    fn = os.path.join("/Users/yourusername/path/to/files")
    sys.path.append(fn)
    import PhyBiopp as pb

Or move the _PhyBiopp.so and PhyBiopp.py files to where you will be running python and just do:

    import PhyBiopp as pb


To compile the library you just need to run

    python setup.py build_ext --inplace

the option --inplace will create it here, however you can put it anywhere as long as you specify the path as above
