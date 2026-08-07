module resta_module

use iso_c_binding

contains


subroutine resta(a,b,c) bind(C,name="resta")

real(c_double), value :: a
real(c_double), value :: b
real(c_double) :: c


c = a-b


end subroutine resta


end module resta_module