from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
ext_modules = [
    Extension("filehunt",  ["filehunt.py"],),
    Extension("msmsg",  ["msmsg.py"]),
    Extension("pst",  ["pst.py"]),
    Extension("main",  ["main.py"]),

#   ... all your modules that need be compiled ...
]
for item in ext_modules:
    item.cython_c_in_temp = True 

ext_modules = cythonize(ext_modules,   compiler_directives={'language_level': 3},)
setup(
    name = 'Panhunt',
    build_dir="build",
    compiler_directives={'language_level': 3},
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    language_level = "3",
)