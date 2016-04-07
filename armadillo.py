#!/usr/bin/python

import gdb      # gdb.Value()
import dumper   # dumper.Children()

def qdump__arma__Mat(d, value):
    array = value["mem"]
    cols = value["n_cols"]
    rows = value["n_rows"]
    maxDisplayItems = 151
    numDisplayItemsCols = min(maxDisplayItems, cols)
    numDisplayItemsRows = min(maxDisplayItems, rows)
    innerType = d.templateArgument(value.type, 0)
    p = gdb.Value(array.cast(innerType.pointer()))
    d.putItemCount(numDisplayItemsCols)
    d.putNumChild(numDisplayItemsCols)
    if d.isExpanded():
        with dumper.Children(d, 
                numChild = cols, # To get "<incomplete>" at bottom
                maxNumChild = maxDisplayItems,
                childType = "col (%s)" %innerType,
                ):
            for i in range(0, cols):
                if i < numDisplayItemsCols:
                    with dumper.Children(d):
                        if d.isExpanded():
                            with dumper.Children(d,
                                    numChild = rows, # To get "<incomplete>" at bottom
                                    maxNumChild = maxDisplayItems,
                                    childType = innerType,
                                    ):
                                for j in range(0, rows):
                                    if j < numDisplayItemsRows:
                                        d.putSubItem(j, p.dereference())
                                    p += 1
                else:
                    for j in range(0, rows):
                        p += 1
