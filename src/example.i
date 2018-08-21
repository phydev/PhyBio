// Linking interface of this particular file
// Need to redo this for any header in src
// And add include it in PhyBiopp.i in root folder
%module example

%{
#include "src/example.hh"
%}

%include src/example.hh
