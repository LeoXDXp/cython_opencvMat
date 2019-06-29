from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy
import sys
import os
import glob

lib_folder = os.path.join(sys.prefix, 'lib64')

# Find opencv libraries in lib_folder
cvlibs = list()
for file in glob.glob(os.path.join(lib_folder, 'libopencv_*')):
    cvlibs.append(file.split('.')[0])
cvlibs = list(set(cvlibs))
cvlibs = ['-L{}'.format(lib_folder)] + \
         ['opencv_{}'.format(lib.split(os.path.sep)[-1].split('libopencv_')[-1]) for lib in cvlibs]

sourcefiles=['opencv_mat/opencv_mat.pyx']
extensions = [ Extension("opencv_mat", sourcefiles, include_dirs=[numpy.get_include(), os.path.join(sys.prefix, 'include', 'opencv2'), ],
                        library_dirs=[lib_folder],
                        libraries=cvlibs,
                        language="c++")
]
setup(
    name="opencv_mat",
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(extensions, annotate=True),
    packages=["opencv_mat"],
    include_package_data=True,
    package_data={'': ['*.pyx', '*.pxd', '*.h', '*.c']}
)
