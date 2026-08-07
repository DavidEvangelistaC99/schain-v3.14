module combine_module

use iso_c_binding
use suma_module
use resta_module

contains


subroutine combine(a,b,result) bind(C,name="combine")

real(c_double), value :: a
real(c_double), value :: b
real(c_double) :: result

real(c_double) :: suma_result
real(c_double) :: resta_result


call suma(a,b,suma_result)

call resta(a,b,resta_result)


result = suma_result * resta_result


end subroutine combine


end module combine_module