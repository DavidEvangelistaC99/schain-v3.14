numpy_include = run_command(
    py,
    '-c',
    'import numpy; print(numpy.get_include())',
    check : true
).stdout().strip()

numpy_f2py_include = run_command(
    py,
    '-c',
    'import numpy.f2py, os; print(os.path.join(os.path.dirname(numpy.f2py.__file__), "src"))',
    check : true
).stdout().strip()

numpy_dep = declare_dependency(
    include_directories : [
        include_directories(numpy_include),
        include_directories(numpy_f2py_include)
    ]
)


fdir = join_paths(
    meson.project_source_root(),
    'schainf',
    'Ffiles'
)

mkfact_sources = files(
    join_paths(fdir,'mkfact.f'),
    join_paths(fdir,'lmdif1.f'),
    join_paths(fdir,'r1mach.f'),
    join_paths(fdir,'bfield2.f')
)

mkfact_sources += get_path_generated

f2py_sources = files(
    join_paths(
        numpy_f2py_include,
        'fortranobject.c'
    )
)

mkfact_wrapper = custom_target(
    'mkfact_wrapper',
    input : [
        join_paths(fdir, 'mkfact_short_2020_2.pyf'),
        join_paths(fdir, 'mkfact.f'),
        join_paths(fdir, 'lmdif1.f'),
        join_paths(fdir, 'r1mach.f'),
        join_paths(fdir, 'bfield2.f'),
    ],
    output : [
        'mkfact_short_2020_2module.c',
        'mkfact_short_2020_2-f2pywrappers.f',
    ],
    command : [
        py,
        '-m',
        'numpy.f2py',
        '-m',
        'mkfact_short_2020_2',
        '--build-dir',
        meson.current_build_dir(),
        '@INPUT@',
    ],
)

py.extension_module(
    'mkfact_short_2020_2',
    [
        mkfact_wrapper,
        mkfact_sources,
        files(
            join_paths(
                numpy_f2py_include,
                'fortranobject.c'
            )
        )
    ],
    dependencies : numpy_dep,
    install : true,
    subdir : 'schainpy/model/proc'
)


py.install_sources(
    [
        '__init__.py',
        'jroproc_init.py',
    ],
    subdir : 'schainpy/model/proc'
)