import time
import pygame


class Stat(object):
    __slots__ = ('value', 'visits')

    def __init__(self, value=0.0, visits=0):
        self.value = value
        self.visits = visits

    def __repr__(self):
        return u"Stat(value={}, visits={})".format(self.value, self.visits)


# TODO
class UCT(object):
    def __init__(self):
        # self.board = board
        self.history = []
        self.stats = {}

        self.max_depth = 0
        self.data = {}

        self.calculation_time = float(5)
        self.max_actions = int(1000)
        self.C = float(1.4)

    # TODO: przekazemy tutaj te sprite'y (nie wiem jak to sie nazywa) tutaj i zamieniamy je na tablice 1-wymiarowa
    # TODO: (2, 2, ..., 0, 0, ..., 1, 1)
    def to_compact_state(self, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group,
                         roundIndex):

        boardList = []

        # filling list which will be later transformated to tuple
        for tile in chessTilesSprintTable:
            if tile.checkState(pawnsSprintTable) == 1:
                boardList.append(1)
            elif tile.checkState(pawnsSprintTable) == 2:
                boardList.append(2)
            else:
                boardList.append(0)

        # appending sitting
        if roundIndex % 2 == 0:
            boardList.append(1)
        else:
            boardList.append(2)

        # transformating list to tuple
        board_in_compact_state = tuple(boardList)

        print(board_in_compact_state)

        return board_in_compact_state

        # return state
        # przykladowa zwrocona wartosc
        # return (2, 2, 2, 2, 2, 2, 2, 2,  # 0 - 7
        #         2, 2, 2, 2, 2, 2, 2, 2,  # 8 - 15
        #         0, 0, 0, 0, 0, 0, 0, 0,  # 16 - 23
        #         0, 0, 0, 0, 0, 0, 0, 0,  # 24 - 31
        #         0, 0, 0, 0, 0, 0, 0, 0,  # 32 - 39
        #         0, 0, 0, 0, 0, 0, 0, 0,  # 40 - 47
        #         1, 1, 1, 1, 1, 1, 1, 1,  # 48 - 55
        #         1, 1, 1, 1, 1, 1, 1, 1,  # 56 - 63
        #         1)  # to bedzie oznaczac gracza ktorego jest ruch w tym stanie (1, 2)
        # pass

    def check_possible_double_jumps(self, legal_actions_list, pawnIndex, state, startingIndex):
        # if state[pawnIndex + 16] != None:
        if pawnIndex < 48:
            if ( state[pawnIndex + 16] == 0):
                if (state[pawnIndex + 8] != 0):
                    legal_actions_list.append((startingIndex, pawnIndex + 16))
                    self.check_possible_double_jumps(legal_actions_list, pawnIndex + 16, state, startingIndex)


        if (pawnIndex + 2) != startingIndex:
            if pawnIndex < 63:
                if (state[pawnIndex + 2] == 0):
                    if (state[pawnIndex + 1] != 0):
                        if (((pawnIndex + 2) % 8) != 1):
                            if (((pawnIndex + 2) % 8) != 0):
                                legal_actions_list.append((startingIndex, pawnIndex + 2))
                                self.check_possible_double_jumps(legal_actions_list, (pawnIndex + 2), state, startingIndex)
                else:
                    pass
            else:
                pass
        elif (pawnIndex - 2) != startingIndex:
            if pawnIndex > 1:
                if (state[pawnIndex - 2] == 0):
                    if (state[pawnIndex - 1] != 0):
                        if (((pawnIndex - 2) % 8) != 7):
                            if (((pawnIndex - 2) % 8) != 6):
                                legal_actions_list.append((startingIndex, pawnIndex - 2))
                                self.check_possible_double_jumps(legal_actions_list, pawnIndex - 2, state,startingIndex)
                else:
                    pass
            else:
                pass
        else:
            pass

    # TODO: funkcja ktora zwraca legalne ruchy z danego stanu
    def legal_actions(self, state):

        legal_actions_list = []

        if state[64] == 2:
            for index, pawn in enumerate(state[:64]):
                if pawn == 2:
                    if (state[index + 1] == 0) and ((index + 1) % 8 != 0):
                        legal_actions_list.append((index, index + 1))
                        # print(index, index + 1)
                    if (state[index - 1] == 0) and ((index % 8) != 0):
                        legal_actions_list.append((index, index - 1))
                        # print(index, index - 1)
                    if index < 48:
                        if state[index + 8] == 0:
                            legal_actions_list.append((index, index + 8))
                            # print('ruch do przodu',index, index + 8)

                    self.check_possible_double_jumps(legal_actions_list, index, state, index)

                    # #calculating the number of max number of jumps
                    # max_number_of_jumps_down = int(((56 + (index % 8)) - index) / 16)
                    #
                    # #max_number_of_jumps_down +1 because it not includes last value
                    # for jumpIndex in range(max_number_of_jumps_down + 1):
                    #     print("jumpIndex",jumpIndex)
                    #     if jumpIndex == 0:
                    #         if state[index]
                    #     elif state[index + (8 * jumpIndex)] == 0 and :
                    #         pass

                    # print(index, max_number_of_jumps_down)
                    print(legal_actions_list)
        else:
            for pawn in state[48:64]:
                print('White', pawn)
                pass

        # return actions
        # przykladowa zwrocona wartosc przy inpucie (state) wygladajacym jak w powyzszej funkcji
        # return [(48, 40), (49, 41), (50, 42), (51, 43), (52, 44), (53, 45), (54, 46), (55, 47)]
        # pass

    # TODO: funkcja ktora zwraca z danego stanu oraz ruchu, stan nastepujacy po tym ruchu
    def next_state(self, history, action):
        # state = history[-1]
        # przykladowa zwrocona wartosc przy inpucie (state, action = (48, 40)) wygladajacym jak w powyzszej funkcji
        return (2, 2, 2, 2, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 2, 2,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                1, 0, 0, 0, 0, 0, 0, 0,  # 40 - 47
                0, 1, 1, 1, 1, 1, 1, 1,  # 48 - 55
                1, 1, 1, 1, 1, 1, 1, 1,  # 56 - 63
                2)  # to bedzie oznaczac gracza ktorego jest ruch w tym stanie (1, 2)
        pass

    # TODO: napisac logike ktora zwroci nam zawodnika ktorego jest ruch w danej pozycji
    def current_player(self, state):
        # return 1 lub 2
        return 2
        pass

    # TODO: napisac logike ktora zwroci nam zawodnika ktorego jest ruch w danej pozycji
    def previous_player(self, state):
        # return 1 lub 2
        return 1
        pass

    def update(self, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group,
               roundIndex):
        self.history.append(self.to_compact_state(chessTilesSprintTable, pawnsSprintTable, roundIndex))

    # TODO
    def get_action(self):
        self.max_depth = 0
        self.data = {'C': self.C, 'max_actions': self.max_actions, 'name': self.name}
        self.stats.clear()

        state = self.history[-1]
        player = self.current_player(state)
        legal = self.legal_actions(state)

        # TODO: trzeba przekminic, jak inaczej zwracac te obiekty jsonowe:
        # TODO: czy tablice z ruchami, czy koncowy stan
        # if not legal:
        #     return {
        #         'type': 'action',
        #         'message': None,
        #         'extras': self.data.copy()}
        # if len(legal) == 1:
        #     return {
        #         'type': 'action',
        #         'message': self.board.to_json_action(legal[0]),
        #         'extras': self.data.copy(),
        #     }

        games = 0
        begin = time.time()
        while time.time() - begin < self.calculation_time:
            self.run_simulation()
            games += 1

        self.data.update(games=games, max_depth=self.max_depth, time=str(time.time() - begin))
        print(self.data['games'], self.data['time'])
        print("Maximum depth searched:", self.max_depth)

        # TODO: trzeba przekminic, jak inaczej zwracac te obiekty jsonowe:
        # TODO: czy tablice z ruchami, czy koncowy stan
        # return {
        #     'type': 'action',
        #     'message': self.board.to_json_action(self.data['actions'][0]['action']),
        #     'extras': self.data.copy(),
        # }

        pass

    # TODO
    def run_simulation(self):
        c, stats = self.C, self.stats

        visited_states = []
        history_copy = self.history[:]
        state = history_copy[-1]

        expand = True
        for t in range(1, self.max_actions + 1):
            legal = self.legal_actions(state)  # TODO: patrz rozkmine przy funkcji
            actions_states = [(a, self.next_state(history_copy, a)) for a in legal]

        pass


# TODO
class UCTWins(UCT):
    name = "jrb.mcts.uct"
    action_template = "{action}: {percent:.2f}% ({wins} / {plays})"

    # def __init__(self, board):
    #     super(UCTWins, self).__init__(board)

    def __init__(self):
        super(UCTWins, self).__init__()

    # TODO
    def calculate_action_values(self, history, player, legal):
        pass
