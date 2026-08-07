cdef extern:

    void combine(
        double a,
        double b,
        double *result
    )


def combine_operation(double a,double b):

    cdef double result

    combine(a,b,&result)

    return result