# debuggingHelpers
Extra Debugging Helpers for QtCreator.
Currently only has helpers for [Armadillo](http://arma.sourceforge.net/) (a C++ linear algebra library).

Latest version has been tested with QtCreator 4.2.0 and 4.4.0, but should work for most versions newer than ~2.8 (I think).
Works both with older gdb versions (which are linked to Python 2), and newer (which are linked to Python 3).

The inspiration was [this](http://stackoverflow.com/a/29984170/1850917) answer on stackoverflow which cites [this](http://plohrmann.blogspot.no/2013/10/writing-debug-visualizers-for-gdb.html) blog post.

# Installation
**QtCreator 4.2.0**: Tools > Options > Debugger > GDB (tab) > Extra Debugging Helpers (near the bottom).  
**QtCreator 4.4.0**: Tools > Options > Debugger > Locals & Expressions (tab) > Extra Debugging Helpers (in the middle).
