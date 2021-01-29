**What are C Extensions?**
- Python talking with the C programming language.
- Creation of wrappers which bind python objects to C Functions.

**What are they for?**
- Because of Python's high level abstractions some things can't be done without a lower level implementation first.
- perhaps you already have a library of C function that you want to turn into a python module to use.

**Python Header**
- Everything in the python header starts with the prefix Py or PY.
- The PyObject type is always used as a pointer and is handles all the data parsing between python and C.
e.g. static PyObject* myFunc(PyObject* self)
   
_python3 setup.py build_

**PyObject**

PyObject is an object structure that you use to define object types for Python. All Python objects share a small number of fields that are defined using the PyObject structure. All other object types are extensions of this type.

PyObject tells the Python interpreter to treat a pointer to an object as an object. For instance, setting the return type of the above function as PyObject defines the common fields that are required by the Python interpreter in order to recognize this as a valid Python type.

