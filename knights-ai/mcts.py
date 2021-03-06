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


class UCT(object):
    def __init__(self):
        self.history = []
        self.stats = {}

        self.max_depth = 0
        self.data = {}

        self.calculation_time = float(5)
        self.max_actions = int(1000)
        self.C = float(1.4)

    def to_compact_state(self, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group,
                         roundIndex):
        boardList = []

        for tile in chessTilesSprintTable:
            if tile.check_state(pawnsSprintTable) == 1:
                boardList.append(1)
            elif tile.check_state(pawnsSprintTable) == 2:
                boardList.append(2)
            else:
                boardList.append(0)

        if roundIndex % 2 == 0:
            boardList.append(1)
        else:
            boardList.append(2)

        board_in_compact_state = tuple(boardList)
        return board_in_compact_state

    def check_possible_multiple_jumps_for_black_pawns(self, legal_actions_list, pawnIndex, state, startingIndex,
                                                      previousIndex):
        if pawnIndex < 48:
            if state[pawnIndex + 16] == 0:
                if state[pawnIndex + 8] != 0:
                    legal_actions_list.append((startingIndex, pawnIndex + 16))
                    self.check_possible_multiple_jumps_for_black_pawns(legal_actions_list, pawnIndex + 16, state,
                                                                       startingIndex,
                                                                       pawnIndex)

        if ((pawnIndex + 2) != startingIndex) and ((pawnIndex + 2) != previousIndex):
            if pawnIndex < 62:
                if state[pawnIndex + 2] == 0:
                    if state[pawnIndex + 1] != 0:
                        if ((pawnIndex + 2) % 8) != 1:
                            if ((pawnIndex + 2) % 8) != 0:
                                legal_actions_list.append((startingIndex, pawnIndex + 2))
                                self.check_possible_multiple_jumps_for_black_pawns(legal_actions_list, (pawnIndex + 2),
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
                                self.check_possible_multiple_jumps_for_black_pawns(legal_actions_list, pawnIndex - 2,
                                                                                   state,
                                                                                   startingIndex, pawnIndex)
                else:
                    pass
            else:
                pass
        else:
            pass

    def check_possible_multiple_jumps_for_white_pawns(self, legal_actions_list, pawnIndex, state, startingIndex,
                                                      previousIndex):
        if pawnIndex > 15:
            if state[pawnIndex - 16] == 0:
                if state[pawnIndex - 8] != 0:
                    legal_actions_list.append((startingIndex, pawnIndex - 16))
                    self.check_possible_multiple_jumps_for_white_pawns(legal_actions_list, pawnIndex - 16, state,
                                                                       startingIndex,
                                                                       pawnIndex)

        if ((pawnIndex + 2) != startingIndex) and ((pawnIndex + 2) != previousIndex):
            if pawnIndex < 62:
                if state[pawnIndex + 2] == 0:
                    if state[pawnIndex + 1] != 0:
                        if ((pawnIndex + 2) % 8) != 1:
                            if ((pawnIndex + 2) % 8) != 0:
                                legal_actions_list.append((startingIndex, pawnIndex + 2))
                                self.check_possible_multiple_jumps_for_white_pawns(legal_actions_list, (pawnIndex + 2),
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
                                self.check_possible_multiple_jumps_for_white_pawns(legal_actions_list, pawnIndex - 2,
                                                                                   state,
                                                                                   startingIndex, pawnIndex)
                else:
                    pass
            else:
                pass
        else:
            pass

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

                    self.check_possible_multiple_jumps_for_black_pawns(legal_actions_list, index, state, index, index)
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

                    self.check_possible_multiple_jumps_for_white_pawns(legal_actions_list, index, state, index, index)
        return legal_actions_list

    def next_state(self, history, action):
        state = history[-1]
        if (state[action[0]] == 0) or (state[action[1]] != 0):
            return None
        state_as_list = list(state)
        if state_as_list[64] == 2:
            state_as_list[action[0]] = 0
            state_as_list[action[1]] = 2
            state_as_list[-1] = 1
        elif state_as_list[64] == 1:
            state_as_list[action[0]] = 0
            state_as_list[action[1]] = 1
            state_as_list[-1] = 2
        next_state = tuple(state_as_list)
        return next_state

    def current_player(self, state):
        return state[-1]

    def previous_player(self, state):
        return 3 - state[-1]

    def is_ended(self, state):
        winning_position_for_white = state[:16]
        winning_position_for_black = state[48:64]

        win_for_white = [a for a in winning_position_for_white if a == 1]
        win_for_black = [a for a in winning_position_for_black if a == 2]

        if (len(win_for_white) != 16) and (len(win_for_black) != 16):
            return False
        else:
            return True

    def end_values(self, state):
        winning_position_for_white = state[:16]
        winning_position_for_black = state[48:64]

        win_for_white = [a for a in winning_position_for_white if a == 1]
        win_for_black = [a for a in winning_position_for_black if a == 2]

        if len(win_for_white) == 16:
            return {1: 1, 2: 0}
        elif len(win_for_black) == 16:
            return {1: 0, 2: 1}
        else:
            return None

    def update(self, state):
        self.history.append(state)

    def get_action(self, chessTilesSprintTable: pygame.sprite.Group, pawnsSprintTable: pygame.sprite.Group,
                   roundIndex):
        self.max_depth = 0
        self.data = {'C': self.C, 'max_actions': self.max_actions, 'name': self.name}
        self.stats.clear()
        self.update(self.to_compact_state(chessTilesSprintTable, pawnsSprintTable, roundIndex))

        state = self.history[-1]
        player = self.current_player(state)
        legal = self.legal_actions(state)

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
        new_state = self.next_state(self.history, action)
        self.update(new_state)

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
            try:
                action, state = choice(actions_states)
            except:
                print("\nAn exception occurred\n")
            visited_states.append(state)
            history_copy.append(state)

            if self.is_ended(state):
                break

        end_values = self.end_values(state)
        for state in visited_states:
            try:
                if state not in stats:
                    continue
                S = stats[state]
                S.visits += 1
                S.value += end_values[self.previous_player(state)]
            except:
                print("\nAn exception occurred\n")


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
