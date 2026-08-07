module suma_module

use iso_c_binding

contains


subroutine suma(a,b,c) bind(C,name="suma")

real(c_double), value :: a
real(c_double), value :: b
real(c_double) :: c


c = a+b


end subroutine suma


end module suma_module