from app.players.player import Player


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        first_part = f"{self.nickname} is playing a song on"
        second_part = f" the {self._musical_instrument}"
        print(first_part + second_part)