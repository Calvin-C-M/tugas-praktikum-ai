Klauses
    member(X,[X|_]).
    member(X,[_|T]) :- member(X,T).

    append(T,T,X) :- member(X,T),!.
    append(T,[X|T],X).

    length([], 0).
    length([H|T], Len) :- length(T, LenTemp). Len is LenTemp+1.