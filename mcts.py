import time
import pygame
from math import log, sqrt
from random import choice


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

    def check_possible_double_jumps_for_black_pawns(self, legal_actions_list, pawnIndex, state, startingIndex, previousIndex):
        if pawnIndex < 48:
            if state[pawnIndex + 16] == 0:
                if state[pawnIndex + 8] != 0:
                    legal_actions_list.append((startingIndex, pawnIndex + 16))
                    self.check_possible_double_jumps_for_black_pawns(legal_actions_list, pawnIndex + 16, state, startingIndex,
                                                     pawnIndex)

        if ((pawnIndex + 2) != startingIndex) and ((pawnIndex + 2) != previousIndex):
            if pawnIndex < 62:
                if state[pawnIndex + 2] == 0:
                    if state[pawnIndex + 1] != 0:
                        if ((pawnIndex + 2) % 8) != 1:
                            if ((pawnIndex + 2) % 8) != 0:
                                legal_actions_list.append((startingIndex, pawnIndex + 2))
                                self.check_possible_double_jumps_for_black_pawns(legal_actions_list, (pawnIndex + 2), state,
                                                                 startingIndex, pawnIndex)
                else:
                    pass
            else:
                pass
        if ((pawnIndex - 2) != startingIndex) and ((pawnIndex - 2) != previousIndex):
            if pawnIndex > 1:
                if state[pawnIndex - 2] == 0:
                    if state[pawnIndex - 1] != 0:
                        if ((pawnIndex - 2) % 8) != 7:
                            if ((pawnIndex - 2) % 8) != 6:
                                legal_actions_list.append((startingIndex, pawnIndex - 2))
                                self.check_possible_double_jumps_for_black_pawns(legal_actions_list, pawnIndex - 2, state,
                                                                 startingIndex, pawnIndex)
                else:
                    pass
            else:
                pass
        else:
            pass

    def check_possible_double_jumps_for_white_pawns(self, legal_actions_list, pawnIndex, state, startingIndex,
                                                    previousIndex):
        if pawnIndex > 15:
            if state[pawnIndex - 16] == 0:
                if state[pawnIndex - 8] != 0:
                    legal_actions_list.append((startingIndex, pawnIndex - 16))
                    self.check_possible_double_jumps_for_white_pawns(legal_actions_list, pawnIndex - 16, state,
                                                                     startingIndex,
                                                                     pawnIndex)

        if ((pawnIndex + 2) != startingIndex) and ((pawnIndex + 2) != previousIndex):
            if pawnIndex < 62:
                if state[pawnIndex + 2] == 0:
                    if state[pawnIndex + 1] != 0:
                        if ((pawnIndex + 2) % 8) != 1:
                            if ((pawnIndex + 2) % 8) != 0:
                                legal_actions_list.append((startingIndex, pawnIndex + 2))
                                self.check_possible_double_jumps_for_white_pawns(legal_actions_list, (pawnIndex + 2),
                                                                                 state,
                                                                                 startingIndex, pawnIndex)
                else:
                    pass
            else:
                pass
        if ((pawnIndex - 2) != startingIndex) and ((pawnIndex - 2) != previousIndex):
            if pawnIndex > 1:
                if state[pawnIndex - 2] == 0:
                    if state[pawnIndex - 1] != 0:
                        if ((pawnIndex - 2) % 8) != 7:
                            if ((pawnIndex - 2) % 8) != 6:
                                legal_actions_list.append((startingIndex, pawnIndex - 2))
                                self.check_possible_double_jumps_for_white_pawns(legal_actions_list, pawnIndex - 2,
                                                                                 state,
                                                                                 startingIndex, pawnIndex)
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
                    if index != 63:
                        if (state[index + 1] == 0) and ((index + 1) % 8 != 0):
                            legal_actions_list.append((index, index + 1))
                    if index != 0:
                        if (state[index - 1] == 0) and ((index % 8) != 0):
                            legal_actions_list.append((index, index - 1))
                    if index < 56:
                        if state[index + 8] == 0:
                            legal_actions_list.append((index, index + 8))

                    self.check_possible_double_jumps_for_black_pawns(legal_actions_list, index, state, index, index)

                    print(legal_actions_list)
        else:
            for index, pawn in enumerate(state[:64]):
                if pawn == 1:
                    if index != 63:
                        if (state[index + 1] == 0) and ((index + 1) % 8 != 0):
                            legal_actions_list.append((index, index + 1))
                    if index != 0:
                        if (state[index - 1] == 0) and ((index % 8) != 0):
                            legal_actions_list.append((index, index - 1))
                    if index > 7:
                        if state[index - 8] == 0:
                            legal_actions_list.append((index, index - 8))

                    self.check_possible_double_jumps_for_white_pawns(legal_actions_list, index, state, index, index)

                    print(legal_actions_list)

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

    # TODO: napisac logike ktora zwroci nam zawodnika ktorego byl ruch w poprzedniej pozycji
    def previous_player(self, state):
        # return 1 lub 2
        return 1
        pass

    # TODO: funkcja ktora zwraca nam info, czy gra zostala juz zakonczona (nie wazne ktory gracz wygral)
    def is_ended(self, state):
        # return True lub False
        pass

    # TODO: funkcja ktora zwraca nam info ktory konkretnie gracz wygral
    def end_values(self, state):
        # return {1: 1, 2: 0} lub return {1: 0, 2: 1}
        pass

    # TODO: update w sumie bedzie musial zostac wykonany po tym jak my zrobimy ruch (czyli przed get_action), oraz
    # TODO: po tym jak komputer zrobi ruch (czyli po get_action). Przerobic tak, zeby update juz przyjmowal
    # TODO: compact_state, bo musi tez byc wywolany po zrobieniu ruchu przez komputer (dodac update po wybraniu ruchu,
    # TODO: w funkcji run_simulation)
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

        # TODO: przekminic czy zostawic te logike
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

        self.data['actions'] = self.calculate_action_values(self.history, player, legal)
        action = self.data['actions'][0]['action']
        for m in self.data['actions']:
            print(self.action_template.format(**m))

        return action

    def run_simulation(self):
        c, stats = self.C, self.stats

        visited_states = []
        history_copy = self.history[:]
        state = history_copy[-1]

        expand = True
        for t in range(1, self.max_actions + 1):
            legal = self.legal_actions(state)
            actions_states = [(a, self.next_state(history_copy, a)) for a in legal]

            if expand and not all(S in stats for a, S in actions_states):
                stats.update((S, Stat()) for a, S in actions_states if S not in stats)
                expand = False
                if t > self.max_depth:
                    self.max_depth = t

            if expand:
                actions_states = [(a, S, stats[S]) for a, S in actions_states]
                log_total = log(sum(e.visits for a, S, e in actions_states) or 1)
                values_actions = [
                    (a, S, (e.value / (e.visits or 1)) + c * sqrt(log_total / (e.visits or 1)))
                    for a, S, e in actions_states
                ]
                max_value = max(v for _, _, v in values_actions)
                actions_states = [(a, S) for a, S, v in values_actions if v == max_value]

            action, state = choice(actions_states)
            visited_states.append(state)
            history_copy.append(state)

            if self.is_ended(state):
                break

        end_values = self.end_values(state)
        for state in visited_states:
            if state not in stats:
                continue
            S = stats[state]
            S.visits += 1
            S.value += end_values[self.previous_player(state)]


class UCTWins(UCT):
    name = "jrb.mcts.uct"
    action_template = "{action}: {percent:.2f}% ({wins} / {plays})"

    def __init__(self):
        super(UCTWins, self).__init__()

    def calculate_action_values(self, history, player, legal):
        actions_states = ((a, self.next_state(history, a)) for a in legal)
        return sorted(
            ({'action': a,
              'percent': 100 * self.stats[S].value / (self.stats[S].visits or 1),
              'wins': self.stats[S].value,
              'plays': self.stats[S].visits}
             for a, S in actions_states),
            key=lambda x: (x['percent'], x['plays']),
            reverse=True
        )
