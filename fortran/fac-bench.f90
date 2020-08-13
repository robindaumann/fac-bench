program facbench
  use fmzm
  implicit none

  integer :: i
  type(im) :: res
  character(10000) :: out

  res = 0
  do i = 1, 3000
     res = res + fac(i)
  end do

  call im_form('i10000', res, out)
  print '(a)', trim(adjustl(out))

contains

  type(im) function fac(n)
    integer, intent(in) :: n
    integer :: i

    fac = 1
    do i = 1, n
       fac = fac * i
    end do
  end function fac

end program facbench
