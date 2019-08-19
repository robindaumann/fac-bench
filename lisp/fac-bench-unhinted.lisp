(declaim (optimize (speed 3) (space 0) (safety 0) (compilation-speed 0)))

(defun fac (n)
  (loop with res = 1
        for i from 1 to n
        do (setq res (* res i))
        finally (return res)))

(defun fac-bench (n)
  (loop for i from 1 to n
        summing (fac i)))

(defun main ()
  (princ (fac-bench 3000)))
