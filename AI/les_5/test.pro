domains
drink = coffee ; tea ; juice ; soda ; water.
temperature = hot ; cold.

predicates
nondeterm likes(drink).
nondeterm wants(temperature).
nondeterm suggest(drink).

clauses
likes(coffee).
likes(juice).
likes(soda).
wants(hot).
wants(cold).

suggest(Drink) :- likes(Drink), likes(coffee), wants(hot).
suggest(Drink) :- likes(Drink), likes(juice), wants(cold).
suggest(Drink) :- likes(Drink), wants(cold).
suggest(Drink) :- likes(Drink), likes(soda), wants(cold).
suggest(Drink) :- likes(Drink), wants(hot).

goal
likes(X).