#!/usr/bin/python

import gdb      # gdb.Value()
import dumper   # dumper.Children()

def qdump__arma__Mat(d, value):
    array = value["mem"]
    cols = value["n_cols"]
    rows = value["n_rows"]
    maxDisplayItems = 50
    innerType = d.templateArgument(value.type, 0)
    p = gdb.Value(array.cast(innerType.pointer()))
    d.putItemCount(cols)
    d.putNumChild(cols)
    if d.isExpanded():
        numDisplayItems = min(maxDisplayItems, cols)
        with dumper.Children(d, numChild=cols,
               maxNumChild=numDisplayItems,
               # childType=innerType,
               childType="<column>",
               addrBase=p,
               addrStep=p.dereference().__sizeof__):
            for i in range(0, int(numDisplayItems)):
                with dumper.Children(d):
                    d.putItemCount(rows)
                    d.putNumChild(rows)
                    if d.isExpanded():
                        numDisplayItems = min(maxDisplayItems, rows)
                        with dumper.Children(d, numChild=rows,
                               maxNumChild=numDisplayItems,
                               childType=innerType,
                               addrBase=p,
                               addrStep=p.dereference().__sizeof__):
                            for j in range(0, int(numDisplayItems)):
                                d.putSubItem(j, p.dereference())
                                p += 1