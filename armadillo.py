#!/usr/bin/python

import gdb      # gdb.Value()
import dumper   # dumper.Children()
from dumper import * # this makes everything work, usually

def qdump__arma__Col(d, value):
    array = value["mem"]
    size = value["n_elem"]
    maxDisplayItems = 50
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
    array = value["mem"]
    cols = value["n_cols"]
    rows = value["n_rows"]
    maxDisplayItems = 151
    numDisplayItemsCols = min(maxDisplayItems, cols)
    numDisplayItemsRows = min(maxDisplayItems, rows)
    innerType = d.templateArgument(value.type, 0)
    p = gdb.Value(array.cast(innerType.pointer()))
    d.putValue('[%dx%d] @0x%x' % (rows, cols, p.dereference().address))
    d.putAddress(value.address)
    d.putNumChild(3)
    with dumper.Children(d):
        d.putSubItem("n_cols", cols)
        d.putSubItem("n_rows", rows)
        with dumper.SubItem(d, "mem_local"):
            d.putItemCount(numDisplayItemsCols)
            d.putNumChild(numDisplayItemsCols)
            d.putType("[%dx%d %s]" %(rows, cols, innerType))
            if d.isExpanded():
                with dumper.Children(d, 
                        numChild=cols, # To get "<incomplete>" at bottom
                        maxNumChild=maxDisplayItems,
                        childType="[%d %s]" %(cols, innerType),
                        ):
                    for i in range(0, cols):
                        if i < numDisplayItemsCols:
                            with dumper.Children(d):
                                if d.isExpanded():
                                    with dumper.Children(d,
                                            numChild=rows, # To get "<incomplete>" at bottom
                                            maxNumChild=maxDisplayItems,
                                            childType=innerType,
                                            ):
                                        for j in range(0, rows):
                                            if j < numDisplayItemsRows:
                                                d.putSubItem(j, p.dereference())
                                            p += 1
                        else:
                            for j in range(0, rows):
                                p += 1
