project(
    'schain',
    ['fortran', 'c'],
    version: '1.0.0'
)


py = import('python').find_installation(
    pure: false
)


numpy_include = run_command(
    py,
    '-c',
    'import numpy; print(numpy.get_include())',
    check: true
).stdout().strip()


f2py_include = run_command(
    py,
    '-c',
    '''
import numpy.f2py
import os
print(
    os.path.join(
        os.path.dirname(numpy.f2py.__file__),
        "src"
    )
)
''',
    check:true
).stdout().strip()



numpy_inc = include_directories(numpy_include)
f2py_inc = include_directories(f2py_include)



#
# Generar wrapper C de f2py
#

wrapper = custom_target(
    'routine_wrapper',

    output: '_routinemodule.c',

    input: 'schainf/routine.pyf',

    command:[
        py,
        '-m',
        'numpy.f2py',
        '@INPUT@',
        '-m',
        '_routine'
    ]
)



#
# f2py runtime
#

fortranobject_c = files(
    join_paths(
        f2py_include,
        'fortranobject.c'
    )
)



#
# Extension module
#

py.extension_module(
    '_routine',

    [
        'schainf/routine.f90',
        wrapper,
        fortranobject_c
    ],

    include_directories:[
        numpy_inc,
        f2py_inc
    ],

    install:true,

    subdir:'schainpy/model/proc',

    dependencies: py.dependency()
)



#
# Python package
#

py.install_sources(
    'src/schainpy/__init__.py',
    subdir:'schainpy'
)


py.install_sources(
    'src/schainpy/model/__init__.py',
    subdir:'schainpy/model'
)


py.install_sources(
[
    'src/schainpy/model/proc/__init__.py',
    'src/schainpy/model/proc/routine.py'
],
subdir:'schainpy/model/proc'
)