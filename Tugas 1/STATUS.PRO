Klausa
    saudara(tuti).
    saudara(chein).
    saudara(iza).
    saudara(retno).
    saudara(siska).

    umur(tuti,40).
    umur(chein,60).
    umur(iza,25).
    umur(retno,15).
    umur(siska,20).

    kakak(X,Y) :- 
        umur(X,Z),
        umur(Y,A),
        Z>A,
        write(X),write(' adalah kakak '),write(Y).

    adik(X,Y) :- 
        umur(X,Z),
        umur(Y,A),
        Z<A,
        write(X),write(' adalah adik '),write(Y).