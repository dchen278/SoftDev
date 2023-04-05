#lang racket
;Team David and Nakib (DAN) | David Chen, Nakib Abedin
;SoftDev pd08
;K27 -- Basic functions in JavaScript
;2023-04-04w
;Time Spent: 0.5 hr

;Scheme Antecedents for JS work


;factorial:
(define
        fact (lambda(n)
        (if(< n 2) 1
        (* n (fact(- n 1)))
)))

(fact 1) ;"...should be  1"
(fact 2) ;"...should be  2"
(fact 3) ;"...should be  6"
(fact 4) ;"...should be  24"
(fact 5) ;"...should be  120"


;fib:
(define
        fib (lambda(n)
        (if (or (= n 0) (= n 1)) n
        (+ (fib(- n 1)) (fib(- n 2))))
))


(fib 0) ;"...should be  0"
(fib 1) ;"...should be  1"
(fib 2) ;"...should be  1"
(fib 3) ;"...should be  2"
(fib 4) ;"...should be  3"
;=================================================================
 
