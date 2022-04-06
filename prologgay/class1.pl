female(sita).
female(gita).
female(nethra).
female(yukta).

male(yogesh).
male(murgesh).
male(george).
male(rome).
parent(sita,murgesh).
parent(george,murgesh).
parent(george,gita).
parent(murgesh,yukta).

parent(murgesh,nethra).
parent(nethra,yogesh).
parent(murgesh,rome).
parent(rome,yogesh).

mother(X,Y):- parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).
sister(X,Y):-parent(Z,X),parent(Z,Y),female(X),X\==Y.
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.
grandparent(X,Y):-parent(X,Z),parent(Z,Y).
grandmother(X,Z):-mother(X,Y),parent(Y,Z).
grandfather(X,Z):-father(X,Y),parent(Y,Z).
wife(X,Y):-parent(X,Z),parent(Y,Z),female(X),male(Y).
uncle(X,Z):-brother(X,Y),parent(Y,Z).
