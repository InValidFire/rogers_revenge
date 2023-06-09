from game_lib import TextBox, GameObject, LEFT, CENTERED, TOP, RIGHT, Game

import pyxel as px


class HUD(GameObject):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.score_box = TextBox(game, f"Score: {self.game.player.score}", 11)
        self.lives_box = TextBox(game, f"Lives: {self.game.player.lives}", 11)
        self.version_box = TextBox(game, self.game.version, 11)

        self.lives_box.place(LEFT, TOP)
        self.score_box.place(CENTERED, TOP)
        self.version_box.place(RIGHT, TOP)

        self.game.add_obj(self.lives_box, True, True)
        self.game.add_obj(self.score_box, True, True)
        self.game.add_obj(self.version_box, True, True)
        self.tick_task(self.update_lives)
        self.tick_task(self.update_score)
        self.game.add_obj(self, False, True, Game.TICKED)

    def update_score(self):
        if int(self.score_box.text.split()[1]) != self.game.player.score:
            self.score_box.place(CENTERED, TOP)
            self.score_box.text = f"Score: {self.game.player.score}"

    def update_lives(self):
        if int(self.lives_box.text.split()[1]) != self.game.player.lives:
            self.lives_box.place(LEFT, TOP)
            self.lives_box.text = f"Lives: {self.game.player.lives}"

    def game_over(self):
        self.tick_task(self.game_over_screen)

    def game_over_screen(self):
        self.game.debug_objs = []
        self.game.ticked_objs = []
        self.game.drawn_objects = []
        text = f"Game Over\nScore: {self.game.player.score}" \
            "\nPress SPACE (A) to restart"
        game_over_box = TextBox(self.game, text, 11)
        game_over_box.place(CENTERED, CENTERED)
        self.game.add_obj(self, True, True, Game.TICKED)
        self.game.add_obj(self.version_box, True, True, Game.DRAWN)
        self.game.add_obj(game_over_box, True, True, Game.DRAWN)
        if px.btnp(px.KEY_SPACE) or px.btnp(px.GAMEPAD1_BUTTON_A):
            self.untick_task(self.game_over_screen)
            self.game.reset()