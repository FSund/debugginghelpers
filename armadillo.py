#!/usr/bin/python

import gdb      # gdb.Value()
import dumper   # dumper.Children()
from dumper import * # this makes everything work, usually

def qdump__arma__Col(d, value):
    array = value["mem"]
    size = value["n_elem"]
    maxDisplayItems = 300
    innerType = d.templateArgument(value.type, 0)
    p = gdb.Value(array.cast(innerType.pointer()))
    d.putValue('[%d] @0x%x' % (size, p.dereference().address))
    d.putAddress(value.address)
    d.putNumChild(2)
    with dumper.Children(d):
        d.putSubItem("n_elem", size)
        with dumper.SubItem(d, "mem_local"):
            d.putItemCount(size)
            d.putNumChild(size)
            d.putType("[%d %s]" %(size, innerType))
            if d.isExpanded():
                numDisplayItems = min(maxDisplayItems, size)
                with dumper.Children(d, 
                        numChild = size,
                        maxNumChild = numDisplayItems,
                        childType = innerType,
                        addrBase = p,
                        addrStep = p.dereference().__sizeof__):
                    for j in range(0, int(numDisplayItems)):
                        d.putSubItem(j, p.dereference())
                        p += 1

def qdump__arma__Mat(d, value):
    # mat(n_rows, n_cols)

    array = value["mem"]
    cols = value["n_cols"]
    rows = value["n_rows"]

    maxDisplayItems = 300
    innerType = d.templateArgument(value.type, 0)
    p = gdb.Value(array.cast(innerType.pointer()))

    d.putValue('Mat [%dx%d] @0x%x' % (rows, cols, p.dereference().address))
    d.putAddress(value.address)
    d.putNumChild(3)
    with dumper.Children(d):
        d.putSubItem("n_cols", cols)
        d.putSubItem("n_rows", rows)
        with dumper.SubItem(d, "mem_local"):
    # cols -------------------------------------------------------------------------------------- #
            d.putItemCount(cols)
            d.putNumChild(cols)
            if d.isExpanded():
                numDisplayItems = min(maxDisplayItems, cols)
                with dumper.Children(d, 
                        numChild = cols,
                        maxNumChild = numDisplayItems,
                        childType = "<column>",
                        addrBase = p,
                        addrStep = p.dereference().__sizeof__):
                    for j in range(0, int(cols)):
                        with dumper.Children(d):
    # rows -------------------------------------------------------------------------------------- #
                            # d.putItemCount(rows)
                            # d.putNumChild(rows)
                            if d.isExpanded():
                                numDisplayItems = min(maxDisplayItems, rows)
                                with dumper.Children(d, 
                                        numChild = rows,
                                        maxNumChild = numDisplayItems,
                                        childType = innerType,
                                        addrBase = p,
                                        addrStep = p.dereference().__sizeof__):
                                    for k in range(0, int(rows)):
                                        if j < maxDisplayItems and k < maxDisplayItems:
                                            d.putSubItem(k, p.dereference())
                                        p += 1

def qdump__arma__Cube(d, value):
    # cube(n_rows, n_cols, n_slices)

    array = value["mem"]
    cols = value["n_cols"]
    rows = value["n_rows"]
    slices = value["n_slices"]

    maxDisplayItems = 300
    innerType = d.templateArgument(value.type, 0)
    p = gdb.Value(array.cast(innerType.pointer()))

    d.putValue('Cube [%dx%dx%d] @0x%x' % (rows, cols, slices, p.dereference().address))
    d.putAddress(value.address)
    d.putNumChild(4)
    with dumper.Children(d):
        d.putSubItem("n_slices", slices)
        d.putSubItem("n_cols", cols)
        d.putSubItem("n_rows", rows)
        with dumper.SubItem(d, "mem_local"):
            # d.putType("[%dx%d %s]" %(rows, cols, innerType))

    # slices ------------------------------------------------------------------------------------ #
            d.putItemCount(slices)
            d.putNumChild(slices)
            if d.isExpanded():
                numDisplayItems = min(maxDisplayItems, slices)
                with dumper.Children(d, 
                        numChild = slices,
                        maxNumChild = numDisplayItems,
                        childType = "<slice>",
                        addrBase = p,
                        addrStep = p.dereference().__sizeof__):
                    for i in range(0, int(slices)):
                        with dumper.Children(d):
    # cols -------------------------------------------------------------------------------------- #
                            # d.putItemCount(cols)
                            # d.putNumChild(cols)
                            if d.isExpanded():
                                numDisplayItems = min(maxDisplayItems, cols)
                                with dumper.Children(d, 
                                        numChild = cols,
                                        maxNumChild = numDisplayItems,
                                        childType = "<column>",
                                        addrBase = p,
                                        addrStep = p.dereference().__sizeof__):
                                    for j in range(0, int(cols)):
                                        with dumper.Children(d):
    # rows -------------------------------------------------------------------------------------- #
                                            # d.putItemCount(rows)
                                            # d.putNumChild(rows)
                                            if d.isExpanded():
                                                numDisplayItems = min(maxDisplayItems, rows)
                                                with dumper.Children(d, 
                                                        numChild = rows,
                                                        maxNumChild = numDisplayItems,
                                                        childType = innerType,
                                                        addrBase = p,
                                                        addrStep = p.dereference().__sizeof__):
                                                    for k in range(0, int(rows)):
                                                        if i < maxDisplayItems and j < maxDisplayItems and k < maxDisplayItems:
                                                            d.putSubItem(k, p.dereference())
                                                        p += 1
