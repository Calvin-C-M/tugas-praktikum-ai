Domains
    orang=symbol

Predicates
    lelaki(orang).
    perempuan(orang).
    ayah(orang,orang).
    ibu(orang,orang).

Klausa Khusus
    lelaki(khuz).
    lelaki(shio).
    lelaki(suman).
    lelaki(chico).
    lelaki(jaka).
    lelaki(sudir).
    lelaki(oto).
    lelaki(tio).
    lelaki(bedu).
    lelaki(zaki).
    lelaki(beny).
    lelaki(tono).
    lelaki(dudi).
    lelaki(fandy).
    lelaki(fino).

    perempuan(nani).
    perempuan(erin).
    perempuan(qiqa).
    perempuan(sisi).
    perempuan(ningsih)
    perempuan(eli).
    perempuan(wati).
    perempuan(ina).
    perempuan(santi).
    perempuan(retno).
    perempuan(ita).
    perempuan(vio).

    ayah(suman,khuz).
    ayah(suman,shio).
    ayah(oto,nani).
    ayah(oto,chico).
    ayah(oto,erin).
    ayah(bedu,qiqa).
    ayah(bedu,sudir).
    ayah(beny,sisi).
    ayah(beny,ningsih).
    ayah(beny,tio).
    ayah(tono,eli).
    ayah(tono,bedu).
    ayah(dudi,zaki).
    ayah(dudi,wati).
    ayah(dudi,beny).
    ayah(fandy,ina).
    ayah(fandy,santi).
    ayah(fino,tono).

    ibu(nani,khuz).
    ibu(nani,shio).
    ibu(sisi,nani).
    ibu(sisi,chico).
    ibu(sisi,erin).
    ibu(eli,qiqa).
    ibu(eli,sudir).
    ibu(ina,sisi).
    ibu(ina,ningsih).
    ibu(ina,tio).
    ibu(santi,eli).
    ibu(santi,bedu).
    ibu(retno,zaki).
    ibu(retno,wati).
    ibu(retno,beny).
    ibu(ita,ina).
    ibu(ita,santi).
    ibu(vio,tono).

% Pasangan
    pasangan(suman,nani).
    pasangan(jaka,qiqa).
    pasangan(oto,sisi).
    pasangan(bedu,eli).
    pasangan(beny,ina).
    pasangan(tono,santi).
    pasangan(dudi,retno).
    pasangan(fandy,ita).
    pasangan(fino,vio).

% Klausa Aturan
    orangtua(X,Y):-ayah(X,Y);ibu(X,Y).
    anak(X,Y) :- orangtua(Y,X).
    saudara(X,Y) :- ayah(Z,Y),anak(X,Z).

    paman(X,Y) :- orangtua(Z,Y),saudara(X,Z),lelaki(X).
    tante(X,Y) :- orangtua(Z,Y),saudara(X,Z),perempuan(X).
    sepupu(X,Y) :- paman(Z,Y),anak(A,Z).
    keponakan(X,Y) :- saudara(Z,Y),anak(X,Z).

    kakek(X,Y) :- orangtua(Z,Y),orangtua(X,Z),lelaki(X).
    nenek(X,Y) :- orangtua(Z,Y),orangtua(X,Z),perempuan(X).

    buyut(X,Y) :- kakek(Z,Y),orangtua(A,Z); nenek(Z,Y),orangtua(A,Z).

    cucu(X,Y) :- anak(Z,Y),anak(A,Z).

    cicit(X,Y) :- anak(Z,Y),anak(A,Z),anak(B,Z).

    piut(X,Y) :- anak(Z,Y),anak(A,Z),anak(B,Z),anak(C,Z).

    mertua(X,Y) :- pasangan(Z,Y),orangtua(X,Z).
    menantu(X,Y) :- anak(Z,Y),pasangan(X,Z).
    