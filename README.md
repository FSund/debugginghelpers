! Warning: There seems to be a bug when viewing large Armadillo objects/matrices (larger than `maxDisplayItems`). A hack to fix this is to increase `maxDisplayItems` to something larger than `n_cols` and `n_rows`. I hope to write a proper fix for this soon.

# debugginghelpers
Extra Debugging Helpers for QtCreator.  
Currently only has helpers for Armadillo (a C++ linear algebra library).

Only tested with QtCreator 3.4.0, but should work for most versions newer than ~2.8 (I think).  
Works both with older gdb versions (which are linked to Python 2), and newer (which are linked to Python 3).

The inspiration was [this](http://stackoverflow.com/a/29984170/1850917) answer on stackoverflow which cites [this](http://plohrmann.blogspot.no/2013/10/writing-debug-visualizers-for-gdb.html) blog post.  
None of those scripts work with Python 3 though, which is why this repo was created.

# Installation
Add to QtCreator by Tools > Options > Debugger > GDB (tab) > Extra Debugging Helpers (near the bottom).
