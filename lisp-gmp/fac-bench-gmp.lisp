(declaim (optimize (speed 3) (space 0) (safety 0) (compilation-speed 0)))
(require 'sb-gmp)
(sb-gmp:install-gmp-funs)

(defun main ()
  (princ (loop for n from 1 to 3000
               summing (sb-gmp:mpz-fac n))))
