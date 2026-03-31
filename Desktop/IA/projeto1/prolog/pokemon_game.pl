:-ensure_loaded("pokemon_list.pl").
:-ensure_loaded("pokemon_info_attacks.pl").
:-ensure_loaded("pokemon_route.pl").

player_starts(0,0).

% predicado auxiliar para ir buscar a informação de um pokemon num indice 

% caso base (indice 0)
get_at_index(0, [H|_], H).

% caso recursivo ( usamos tail e retiramos a head em cada iteracão)
get_at_index(N, [_|T], E) :-
    N > 0,        
    N1 is N - 1,
    get_at_index(N1, T, E).



% posicões adjacentes com verificação outOfBounds
adjacent(X, Y, NX, Y) :- NX is X + 1, NX =< 4. % Right
adjacent(X, Y, NX, Y) :- NX is X - 1, NX >= 0. % Left
adjacent(X, Y, X, NY) :- NY is Y + 1, NY =< 4. % Down
adjacent(X, Y, X, NY) :- NY is Y - 1, NY >= 0. % Up


% ir buscar a informacão de uma posição específica à route
get_cell(X, Y, Matrix, CellData) :-
    get_at_index(Y, Matrix, Row),
    get_at_index(X, Row, CellData).


% vai buscar a informação do pokemon na posição adjacente na route atual
find_adjacent_pokemon(X, Y, [Id, Name, Level, NX, NY, Types]) :-
    adjacent(X, Y, NX, NY),
    route(Matrix),
    get_cell(NX, NY, Matrix, (Id, Level)),
    pokemon(Id, Name, Types).

% TO DO
next_rooms(X,Y,Rooms) :-
    findall(Room, find_adjacent_pokemon(X, Y, Room), Rooms).