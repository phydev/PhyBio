// Linking interface of this particular file
// Need to redo this for any header in src
// And add include it in PhyBiopp.i in root folder
%module PhyBio

%{
#include "src/PhyBio.hh"
%}

%include src/PhyBio.hh
