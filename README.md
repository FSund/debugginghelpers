# debugginghelpers
Extra Debugging Helpers for QtCreator.
Currently only has helpers for Armadillo (a C++ linear algebra library).

Add to QtCreator by Tools > Options > Debugger > GDB (tab) > Extra Debugging Helpers (near the bottom).

Only tested for QtCreator 3.4.0, but should work for most versions newer than ~2.8 (I think).

Works both with older gdb versions (which are linked to Python 2), and newer (which are linked to Python 3).

The inspiration was this answer on stackoverflow http://stackoverflow.com/a/29984170/1850917
which cites this source: http://plohrmann.blogspot.no/2013/10/writing-debug-visualizers-for-gdb.html
None of those scripts work with Python 3 though, which is why this repo was created.