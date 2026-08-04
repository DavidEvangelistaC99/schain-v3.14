project(
    'schain',
    ['c', 'fortran'],
    version : '3.14.0',
    meson_version : '>=1.6',
)

# Resolve incompatibilites in Fortran version files
add_project_arguments(
    '-fallow-argument-mismatch',
    language : 'fortran'
)

py = import('python').find_installation(pure: false)

# Steps for Fortran module installation

bfmodel_path = join_paths(
    meson.project_source_root(),
    'schainf',
    'Ffiles',
    'bfmodel'
)

config = configuration_data()

config.set(
    'BFMODEL_PATH',
    bfmodel_path
)

get_path_generated = configure_file(
    input : 'schainf/Ffiles/get_path.f90.in',
    output : 'get_path.f90',
    configuration : config
)

subdir('schainpy')