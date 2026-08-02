#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <numpy/arrayobject.h>
#include <math.h>


static PyObject *HS_algorithm(PyObject *self, PyObject *args)
{
    double navg;
    PyObject *data_obj;
    PyArrayObject *data_array;

    if (!PyArg_ParseTuple(args, "Od", &data_obj, &navg))
    {
        return NULL;
    }

    data_array = (PyArrayObject *)PyArray_FROM_OTF(
        data_obj,
        NPY_FLOAT64,
        NPY_ARRAY_IN_ARRAY
    );

    if (data_array == NULL)
    {
        return NULL;
    }

    double *sortdata = (double *)PyArray_DATA(data_array);

    npy_intp lenOfData = PyArray_SIZE(data_array);

    double nums_min = lenOfData * 0.75;

    if (nums_min <= 5)
        nums_min = 5;


    double sump = 0.0;
    double sumq = 0.0;

    npy_intp j = 0;

    int cont = 1;

    double rtest = 0.0;


    while ((cont == 1) && (j < lenOfData))
    {
        sump += sortdata[j];
        sumq += sortdata[j] * sortdata[j];


        if (j > nums_min)
        {
            rtest = (double)j / (j - 1) + 1.0 / navg;


            if ((sumq * j) > (rtest * sump * sump))
            {
                j--;

                sump -= sortdata[j];
                sumq -= sortdata[j] * sortdata[j];

                cont = 0;
            }
        }

        j++;
    }


    double lnoise = sump / (double)j;


    Py_DECREF(data_array);


    /*
       El código original retornaba j:
       return PyFloat_FromDouble(j);

       Si quieres devolver el nivel de ruido:
    */
    return PyFloat_FromDouble(lnoise);
}



static PyMethodDef noiseMethods[] = {

    {
        "HS_algorithm",
        HS_algorithm,
        METH_VARARGS,
        "Applies hildebrand_sekhon algorithm"
    },

    {NULL, NULL, 0, NULL}
};



static struct PyModuleDef noisemodule = {

    PyModuleDef_HEAD_INIT,

    "_HS_algorithm",

    "Applies hildebrand_sekhon algorithm",

    -1,

    noiseMethods
};



PyMODINIT_FUNC PyInit__HS_algorithm(void)
{
    import_array();

    return PyModule_Create(&noisemodule);
}