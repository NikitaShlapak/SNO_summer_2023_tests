      program primes
      integer, parameter :: n = 100
      integer, dimension(n) :: b
      integer :: k, i
      integer :: a[allocatable](:)
      

      call filter_primes(n, b, k)
      allocate(a(k), stat=ierr)
      do i = 1, k
      a(i) = b(i)
      end do
      print*, a
      deallocate(a)
      read *
      end program primes
      
      subroutine filter_primes(n, b, k)
      integer, dimension(n) :: b, a
      integer :: i, j, k
      do i = 1,n
      a(i) = 0
      end do
      k = 0
      do i = 2,(n + 1)
         if (a(i)==0) then
            k = k + 1
            b(k) = i
            if (i*i < (n+1)) then
               do j = i*i,n+1,i
                  a(j) = 1
               end do
            end if
         end if
      end do
      end subroutine filter_primes
