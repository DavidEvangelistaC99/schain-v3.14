# Copyright (c) 2012-2020 Jicamarca Radio Observatory
# All rights reserved.
#
# Distributed under the terms of the BSD 3-clause license.
"""schainpy is an open source library to read, write and process radar data

Signal Chain is a radar data processing library wich includes modules to read,
and write different files formats, besides modules to process and visualize the
data.
"""

import os
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from schainpy import __version__

DOCLINES = __doc__.split("\n")

class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # Prevent numpy from thinking it is still in its setup process:
        __builtins__.__NUMPY_SETUP__ = False
        import numpy
        self.include_dirs.append(numpy.get_include())

setup(
    name = "schainpy",
    version = __version__,
    description = DOCLINES[0],
    long_description = "\n".join(DOCLINES[2:]),
    url = "https://github.com/JRO-Peru/schainpy",
    author = "Jicamarca Radio Observatory",
    author_email = "jro-developers@jro.igp.gob.pe",
    license="BSD-3-Clause",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
    ],
    packages = {
        'schainpy',
        'schainpy.model',
        'schainpy.model.data',
        'schainpy.model.graphics',
        'schainpy.model.io',
        'schainpy.model.proc',
        'schainpy.model.utils',
        'schainpy.utils',
        'schainpy.gui',
        'schainpy.cli',
        },
    package_data = {'': ['schain.conf.template'],
                    'schainpy.files': ['*.oga']
                    },
    include_package_data = False,
    scripts = ['schainpy/gui/schainGUI'],
    entry_points = {
        'console_scripts': [
            'schain = schainpy.cli.cli:main',
            ],
        },
    cmdclass = {'build_ext': build_ext},
    ext_modules=[
        Extension("schainpy.model.data._noise", ["schainc/_noise.c"]),
        Extension("schainpy.model.data._HS_algorithm", ["schainc/_HS_algorithm.c"]),
        ],
    setup_requires = ["numpy"],
    install_requires = [
        "scipy",
        "h5py",
        "matplotlib",
        "pyzmq",
        "fuzzywuzzy",
        "click",
        ],
)

from numpy.distutils.core import Extension, setup

setup(name='schainpy',
    ext_modules = [
        Extension("schainpy.model.proc.mkfact_short_2020_2",
            sources=[
                "schainf/mkfact/mkfact_short_2020_2.pyf",
                "schainf/mkfact/lmdif1.f",
                "schainf/mkfact/mkfact.f",
                "schainf/mkfact/r1mach.f",
                "schainf/mkfact/bfield2.f"])
                ]
                )

'''
setup(name='schainpy',
    ext_modules = [
        Extension("schainpy.model.proc.mkfact_short_2020_2",
            sources=[
                "schainf/mkfact/mkfact_short_2020_2.pyf",
                "schainf/mkfact/lmdif1.f",
                "schainf/mkfact/mkfact.f",
                "schainf/mkfact/r1mach.f",
                "schainf/mkfact/bfield2.f"]),
        Extension("schainpy.model.proc.full_profile_profile",
            sources=[
                "schainf/full_profile/full_profile_profile.pyf",
                "schainf/full_profile/full_profile_profile.f",
                "schainf/full_profile/fitacf.f",
                "schainf/full_profile/r1mach.f",
                "schainf/full_profile/lmdif1.f",
                "schainf/full_profile/lagp.f",
                "schainf/full_profile/reader.c",
                "schainf/full_profile/cbesi.f",
                "schainf/full_profile/i1mach.f",
                "schainf/full_profile/zeta.f",
                "schainf/full_profile/qc25f.f",
                "schainf/full_profile/qwgtf.f",
                "schainf/full_profile/qcheb.f",
                "schainf/full_profile/sgtsl.f",
                "schainf/full_profile/qk15w.f",
                "schainf/full_profile/complex.c",
                "schainf/full_profile/cbinu.f",
                "schainf/full_profile/cseri.f",
                "schainf/full_profile/cwrsk.f",
                "schainf/full_profile/crati.f",
                "schainf/full_profile/casyi.f",
                "schainf/full_profile/cbuni.f",
                "schainf/full_profile/cuni2.f",
                "schainf/full_profile/gamln.f",
                "schainf/full_profile/cuchk.f",
                "schainf/full_profile/cbknu.f",
                "schainf/full_profile/cshch.f",
                "schainf/full_profile/ckscl.f",
                "schainf/full_profile/cuoik.f",
                "schainf/full_profile/cunik.f",
                "schainf/full_profile/cuni1.f",
                "schainf/full_profile/cairy.f",
                "schainf/full_profile/cmlri.f",
                "schainf/full_profile/cunhj.f",
                "schainf/full_profile/cacai.f",
                "schainf/full_profile/csisl.f",
                "schainf/full_profile/caxpy.f",
                "schainf/full_profile/cs1s2.f",
                "schainf/full_profile/scabs1.f",
                "schainf/full_profile/cdotu.f",
                "schainf/full_profile/rs.f",
                "schainf/full_profile/sppfa.f",
                "schainf/full_profile/sdot.f",
                "schainf/full_profile/tred2.f",
                "schainf/full_profile/tql2.f",
                "schainf/full_profile/sppdi.f",
                "schainf/full_profile/saxpy.f",
                "schainf/full_profile/sscal.f",
                "schainf/full_profile/pythag.f",
                "schainf/full_profile/tql1.f",
                "schainf/full_profile/tred1.f"]),
        Extension("schainpy.model.proc.fitacf_acf2",
            sources = [
                "schainf/acf2/fitacf_acf2.pyf",
                "schainf/acf2/full_profile_profile.f",
                "schainf/acf2/fitacf.f",
                "schainf/acf2/r1mach.f",
                "schainf/acf2/lmdif1.f",
                "schainf/acf2/lagp.f",
                "schainf/acf2/reader.c",
                "schainf/acf2/cbesi.f",
                "schainf/acf2/i1mach.f",
                "schainf/acf2/zeta.f",
                "schainf/acf2/qc25f.f",
                "schainf/acf2/qwgtf.f",
                "schainf/acf2/qcheb.f",
                "schainf/acf2/sgtsl.f",
                "schainf/acf2/qk15w.f",
                "schainf/acf2/complex.c",
                "schainf/acf2/cbinu.f",
                "schainf/acf2/cseri.f",
                "schainf/acf2/cwrsk.f",
                "schainf/acf2/crati.f",
                "schainf/acf2/casyi.f",
                "schainf/acf2/cbuni.f",
                "schainf/acf2/cuni2.f",
                "schainf/acf2/gamln.f",
                "schainf/acf2/cuchk.f",
                "schainf/acf2/cbknu.f",
                "schainf/acf2/cshch.f",
                "schainf/acf2/ckscl.f",
                "schainf/acf2/cuoik.f",
                "schainf/acf2/cunik.f",
                "schainf/acf2/cuni1.f",
                "schainf/acf2/cairy.f",
                "schainf/acf2/cmlri.f",
                "schainf/acf2/cunhj.f",
                "schainf/acf2/cacai.f",
                "schainf/acf2/csisl.f",
                "schainf/acf2/caxpy.f",
                "schainf/acf2/cs1s2.f",
                "schainf/acf2/scabs1.f",
                "schainf/acf2/cdotu.f",
                "schainf/acf2/rs.f",
                "schainf/acf2/sppfa.f",
                "schainf/acf2/sdot.f",
                "schainf/acf2/tred2.f",
                "schainf/acf2/tql2.f",
                "schainf/acf2/sppdi.f",
                "schainf/acf2/saxpy.f",
                "schainf/acf2/sscal.f",
                "schainf/acf2/pythag.f",
                "schainf/acf2/tql1.f",
                "schainf/acf2/tred1.f"])
                ]
                )
'''
