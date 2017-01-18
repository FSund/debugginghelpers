#!/usr/bin/python

from dumper import * # this makes everything work, usually

def qdump__arma__Col(d, value):
    nrows = value["n_rows"].integer() # identical to n_elem for colvec
    ncols = value["n_cols"].integer() #
    n_elem =  value["n_elem"].integer() #

    d.putValue('[%d] %s ' % (nrows, value["mem"].dereference().type.name))
    d.putNumChild(4)

    limit = 10000 # not really used at the moment
    nnrows = min(nrows, limit)

    if d.isExpanded():
        with Children(d):
            warn("%s" %d.Value)
            d.putIntItem("n_rows", nrows)
            d.putIntItem("n_cols", ncols)
            d.putIntItem("n_elem", n_elem)

            base = value["mem"].dereference()
            typeobj = base.type
            addrBase = base.address()
            typeName = typeobj.name
            d.putArrayItem('mem', addrBase, n_elem, typeName)

def qdump__arma__Mat(d, value):
    array = value["mem"]
    nrows = value["n_rows"].integer() # identical to n_elem for colvec
    ncols = value["n_cols"].integer() #
    n_elem =  value["n_elem"].integer() #

    d.putNumChild(4)
    d.putValue('[%d, %d] %s ' % (nrows, ncols, value["mem"].dereference().type.name))

    limit = 10000 # not used at the moment
    nnrows = min(nrows, limit)
    nncols = min(ncols, limit)

    if d.isExpanded():
        with Children(d):
            warn("%s" %d.Value)
            d.putIntItem("n_rows", nrows)
            d.putIntItem("n_cols", ncols)
            d.putIntItem("n_elem", n_elem)
            with SubItem(d, "mem"):
                d.putNumChild(ncols)
                base = value["mem"].dereference()
                typeobj = base.type
                innerType = typeobj
                innerSize = innerType.size()
                addrBase = base.address()
                with Children(d):
                    for i in range(ncols):
                        d.putArrayItem('[%d]' %i, addrBase + innerSize*i*nrows, nrows, typeobj.name)

def qdump__arma__Cube(d, value):
    array = value["mem"]
    nrows = value["n_rows"].integer()
    ncols = value["n_cols"].integer()
    nslices = value["n_slices"].integer()
    n_elem =  value["n_elem"].integer()

    d.putValue('[%d, %d, %d] %s ' % (nrows, ncols, nslices, value["mem"].dereference().type.name))
    d.putNumChild(5)

    limit = 10000 # not used at the moment
    nnrows = min(nrows, limit)
    nncols = min(ncols, limit)

    if d.isExpanded():
        with Children(d):
            d.putIntItem("n_rows", nrows)
            d.putIntItem("n_cols", ncols)
            d.putIntItem("n_slices", nslices)
            d.putIntItem("n_elem", n_elem)
            with SubItem(d, "mem"):
                d.putNumChild(nslices)
                base = value["mem"].dereference()
                typeobj = base.type
                innerType = typeobj
                innerSize = innerType.size()
                addrBase = base.address()
                with Children(d):
                    for i in range(nslices):
                        with Children(d):
                            d.putNumChild(ncols)
                            with Children(d):
                                for j in range(ncols):
                                    d.putArrayItem('[%d]' %j, addrBase + (i*ncols*nrows + j*nrows)*innerSize, nrows, typeobj.name)
