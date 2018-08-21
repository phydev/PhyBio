#setup.py file for PhyBiopp:
from setuptools import setup, Extension
#from distutils.core import setup, Extension
#importing numpy
#import numpy
#getting numpy include directory
#numpy_include = numpy.get_include()

setup(name='PhyBiopp',
    version='0.1',
    ext_modules=[Extension('_PhyBiopp', sources=['src/RegularGrid.cc','PhyBiopp.i'],
#    				 include_dirs=['/usr/local/include/','./include'],
 #   				 library_dirs = ['/usr/local/lib/','./lib'],
#    				 libraries = ['m','gsl'],
                    swig_opts=['-c++'],)],
    headers=['src/RegularGrid.hh']
)
