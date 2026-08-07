project(
    'schain',
    ['fortran','c','cython'],
    version:'1.0.0'
)


py = import('python').find_installation(
    pure:false
)


py_dep = py.dependency()

py.extension_module(
    'combine',

    [
        'schainpy/model/proc/combine.pyx',
        'schainf/Ffiles/combine.f90',
        'schainf/Ffiles/suma.f90',
        'schainf/Ffiles/resta.f90'
    ],
    install:true,
    subdir:'schainpy/model/proc',
    dependencies: py_dep

)



#
# Python puro
#

py.install_sources(
    [
    'schainpy/model/proc/__init__.py'
    ],
    subdir:'schainpy/model/proc'
)