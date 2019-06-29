# cython wrapper `np.array` <-> `cv::Mat`

Implementation of cython wrapper to allow the convertion between a `numpy.array` and a `cv::Mat` and the other way arround (`cv::Mat` to `numpy.array`).

To build as standalone, run `python setup.py build_ext --inplace`.
To build as rpm package, run python3 setup.py bdist_rpm".

Then try :
```python3
import opencv_mat
from scipy import misc

im_np = misc.imread(filename/image)
im_np2Mat2np = opencv_mat.np2Mat2np(im_np)
```
We get back `im_np2Mat2np` which is the same as `im_np`.

Feel free to integrate the `cdef np2Mat` and `cdef Mat2np` functions to your code!

_Used with Python 3.7 and Opencv 3.4.1_
