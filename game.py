#!/usr/bin/env python3

import logging
import itertools

class DumbStickPlayer(object):
    _name = "DUMBPlayer"

    def turn(self, sticks):
        return 1

    def __repr__(self):
        return self._name

class EvenDumberStickPlayer(DumbStickPlayer):
    _name = "EvenDumberPlayer"

    def turn(self, sticks):
        return 3

class HumanStickPlayer(DumbStickPlayer):
    _name = "Human"
    
    def __init__(self, keys='qwe'):
        self.keys = keys

    def turn(self, sticks):
        return 1

class StickGame(object):

    def __init__(self, playerA, playerB):
        self.players = itertools.cycle([playerA, playerB])
        playerA._name+=" playerA"
        playerB._name+=" playerB"

    def run(self):
        self.sticks = 11
        while self.sticks > 1:
            self.turn(next(self.players))
        else:
            logging.info("Player %r LOSE", next(self.players)._name)
            logging.info("Player %r WON", next(self.players)._name)

    def turn(self, player):
        logger = logging.getLogger('turn %r'%player)
        try:
            player_takes = player.turn(self.sticks)
            if not isinstance(player_takes, int):
                raise ValueError("returned non integer value: %r !"%(player_takes))
            if player_takes > 3:
                raise ValueError("taking more than 3 sticks: %r !"%(player_takes))
            if player_takes > self.sticks-1:
                raise ValueError("taking more than available sticks: taking %r, left %r!"%(player_takes, self.sticks))
            if player_takes < 1:
                    raise ValueError("taking less than 1 stick, that's forbidden. Taking %r."%(player_takes, self.sticks))
            self.sticks -= player_takes
            logger.info("Took %d sticks, left %d", player_takes, self.sticks)
        except Exception as e:
            logger.exception("Player messed up!")
            raise e

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    sg = StickGame(DumbStickPlayer(), DumbStickPlayer())
    sg.run()

    sg = StickGame(DumbStickPlayer(), EvenDumberStickPlayer())
    sg.run()
