#!/usr/bin/python

# import gdb      # gdb.Value()
# import dumper   # dumper.Children()
from dumper import * # this makes everything work, usually

def qdump__arma__Col(d, value):
    warn('Hello, World! From arma')
    # array = value["mem_local"]
    array = value["mem"]
    nrows = value["n_rows"].integer() # identical to n_elem for colvec
    ncols = value["n_cols"].integer() #
    n_elem =  value["n_elem"].integer() #
    # ncols = 1
    maxDisplayItems = 300

    innerType = array.type
    innerSize = innerType.size()

    # otherSize = value.type[0]
    # d.putValue('[%s]' %otherSize)

    # p = value['mem_local'].pointer()
    # p = value['mem_local'].address()
    # p = value.address()
    # p = value.pointer()
    # p = value['mem_local']
    # p = value.address()
    # p = array.address()
    # p = array.pointer()
    p = array.address()

    # warn('nrows = %d' %nrows)

    # d.putType('%s[%d]' % (innerType, nrows))
    # d.putEmptyValue()
    d.putValue('[%d] %s ' % (nrows, value["mem"].dereference().type.name))
    # warn('typeobj.name = %s' %typeobj.name)
    # d.putValue('[]')
    # d.putField('keeporder', '1')
    d.putNumChild(4)
    # d.putNumChild(nrows)
    # d.putItemCount(nrows)

    warn('Debug stuff incoming from Arma')
    warn('innerType = %s' % innerType) # "Type(name=$double*$,bsize=64,code=6)
    warn('innerType.__class__ = %s' % innerType.__class__) # "dumper.Type"
    warn('innerSize = %s' % innerSize)
    warn('p = %s' % p)
    warn('p.__class__ = %s' % p.__class__) # "<type 'int'>"
    warn('array.__class__ = %s' %array.__class__) # "dumper.Value"
    warn('array.type.__class__ = %s' %array.type.__class__) # "dumper.Type"
    warn('array.type.size() = %s' %array.type.size()) # 8 -- size in bytes
    warn('nrows = %s' % nrows)

    limit = 10000
    nnrows = min(nrows, limit)

    if d.isExpanded():
        with Children(d):
            warn("%s" %d.Value)
            d.putIntItem("n_rows", nrows)
            d.putIntItem("n_cols", ncols)
            d.putIntItem("n_elem", n_elem)
            # d.putSubItem("n_elem", nrows)

            if False:
                with SubItem(d, "mem"):
                    # if d.isExpanded():
                    # d.putArrayData(base = array.address(), n = n_elem, innerType = innerType)
                    warn('HEEEEEEEi')
                    warn('blablabla %s' %value["mem"]) # Value(name='mem',type=double*,bsize=64,bpos=None,data=,address=0x7fffffffe510)
                    warn('blablabla %s' %value["mem"].dereference()) # Value(name='None',type=double,bsize=None,bpos=None,data=,address=0x7fffffffe520)
                    warn('blablabla %s' %value["mem"].dereference().address()) # 140737488348448
                    
                    base = value["mem"].dereference()
                    typeobj = base.type
                    warn('typeobj = %s' %typeobj)
                    warn('base = %s' %base)
                    d.putArrayData(base.address(), n_elem, typeobj)
                    # d.putItemCount(nrows)
                    # d.putNumChild(nrows)
                    # if d.isExpanded():
                        # with Children(d, nrows, childType = innerType):
                        #     for i in range(0, nnrows):
                        #         item = p + i * innerSize
                        #         d.putSubItem(i, d.createValue(item, innerType))
                        # with Children(
                        #         d,
                        #         numChild = nrows, 
                        #         childType = innerType,
                        #         addrBase = p,
                        #         addrStep = innerSize):
                        #     for i in range(0, nnrows):
                        #         item = p + i * innerSize
                        #         d.putSubItem(i, d.createValue(item, innerType))
            else:
                base = value["mem"].dereference()
                typeobj = base.type
                addrBase = base.address()
                typeName = typeobj.name
                d.putArrayItem('mem', addrBase, n_elem, typeName)

def qdump__arma__Mat(d, value):
    warn('Hello, World! From arma::Mat')
    
    array = value["mem"]
    nrows = value["n_rows"].integer() # identical to n_elem for colvec
    ncols = value["n_cols"].integer() #
    n_elem =  value["n_elem"].integer() #
    
    maxDisplayItems = 300

    innerType = array.type
    innerSize = innerType.size()

    # otherSize = value.type[0]
    # d.putValue('[%s]' %otherSize)

    # p = value['mem_local'].pointer()
    # p = value['mem_local'].address()
    # p = value.address()
    # p = value.pointer()
    # p = value['mem_local']
    # p = value.address()
    # p = array.address()
    # p = array.pointer()
    p = array.address()

    # warn('nrows = %d' %nrows)

    # d.putType('%s[%d]' % (innerType, nrows))
    # d.putEmptyValue()
    # d.putValue('testing')
    # d.putField('keeporder', '1')
    d.putNumChild(4)
    # d.putNumChild(nrows)
    # d.putItemCount(nrows)

    d.putValue('[%d, %d] %s ' % (nrows, ncols, value["mem"].dereference().type.name))

    warn('Debug stuff incoming from Arma')
    warn('innerType = %s' % innerType) # "Type(name=$double*$,bsize=64,code=6)
    warn('innerType.__class__ = %s' % innerType.__class__) # "dumper.Type"
    warn('innerSize = %s' % innerSize)
    warn('p = %s' % p)
    warn('p.__class__ = %s' % p.__class__) # "<type 'int'>"
    warn('array.__class__ = %s' %array.__class__) # "dumper.Value"
    warn('array.type.__class__ = %s' %array.type.__class__) # "dumper.Type"
    warn('array.type.size() = %s' %array.type.size()) # 8 -- size in bytes
    warn('nrows = %s' % nrows)

    limit = 10000
    nnrows = min(nrows, limit)
    nncols = min(ncols, limit)

    if d.isExpanded():
        with Children(d):
            warn("%s" %d.Value)
            d.putIntItem("n_rows", nrows)
            d.putIntItem("n_cols", ncols)
            d.putIntItem("n_elem", n_elem)
            # d.putSubItem("n_elem", nrows)

            with SubItem(d, "mem"):
                d.putNumChild(ncols)
                base = value["mem"].dereference()
                typeobj = base.type
                innerType = typeobj
                innerSize = innerType.size()
                addrBase = base.address()

                warn('typeobj = %s' %typeobj)
                # warn('typeobj.name() = %s' %typeobj.name())
                warn('typeobj.name = %s' %typeobj.name)

                # d.putArrayData(addrBase, nrows, typeobj)

                with Children(d):
                    for i in range(ncols):
                        d.putArrayItem('[%d]' %i, addrBase + innerSize*i*nrows, nrows, typeobj.name)

                # warn('innerSize = %s' %innerSize)
                # warn('nrows = %s' %nrows)
                # for i in range(ncols):
                #     with Children(d):
                #         d.putArrayData(addrBase, nrows, typeobj)
                #         addrBase += innerSize*nrows
                #         warn('addrBase = %s' %addrBase)

def qdump__arma__Cube(d, value):
    warn('Hello, World! From arma::Cube')
    
    array = value["mem"]
    nrows = value["n_rows"].integer()
    ncols = value["n_cols"].integer()
    nslices = value["n_slices"].integer()
    n_elem =  value["n_elem"].integer()
    
    maxDisplayItems = 300

    innerType = array.type
    innerSize = innerType.size()

    d.putValue('[%d, %d, %d] %s ' % (nrows, ncols, nslices, value["mem"].dereference().type.name))
    d.putNumChild(5)

    limit = 10000
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
                        # with SubItem(d, "[slice]")
                        with Children(d):
                            d.putNumChild(ncols)
                            with Children(d):
                                for j in range(ncols):
                                    d.putArrayItem('[%d]' %j, addrBase + (i*ncols*nrows + j*nrows)*innerSize, nrows, typeobj.name)
