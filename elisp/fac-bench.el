#!/bin/sh
":"; exec emacs -Q --script "$0" -- "$@" # -*- mode: emacs-lisp; lexical-binding: t -*-

(require 'cl-lib)

(defun fac (n)
  (cl-loop with res = 1
           for i from 1 to n
           do (setq res (* res i))
           finally (return res)))

(princ (cl-loop for i from 1 to 3000 summing (fac i)))

(kill-emacs 0)
