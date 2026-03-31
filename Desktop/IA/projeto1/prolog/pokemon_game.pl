:-ensure_loaded("pokemon_list.pl").
:-ensure_loaded("pokemon_info_attacks.pl").
:-ensure_loaded("pokemon_route.pl").

player_starts(0,0).
% Caso Base: Se o índice for 0, o elemento é a Cabeça (H).
obter_at_index(0, [H|_], H).

% Caso Recursivo: Se o índice for N (MAIOR que 0), continua a procurar.
obter_at_index(N, [_|T], E) :-
    N > 0,              % Aqui garantimos que se N for 0, esta regra nem tenta correr
    N1 is N - 1,
    obter_at_index(N1, T, E).
% TO DO
next_rooms(X,Y,Rooms) :-
    route(M).