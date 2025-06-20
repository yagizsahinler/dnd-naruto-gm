import random
from typing import Tuple


class Dice:
    @staticmethod
    def roll(sides: int = 20, modifier: int = 0) -> Tuple[int, bool, bool]:
        """
        Zar atar ve sonucu döner.
        :param sides: Zarın yüz sayısı (varsayılan 20)
        :param modifier: Stat modifiyeri (örneğin INT mod)
        :return: (toplam değer, kritik başarı mı, kritik başarısızlık mı)
        """
        base_roll = random.randint(1, sides)
        total = base_roll + modifier
        is_critical_success = base_roll == sides
        is_critical_failure = base_roll == 1
        return total, is_critical_success, is_critical_failure

    @staticmethod
    def roll_multiple(dice_count: int, sides: int) -> int:
        """
        Belirli sayıda zar atar ve toplamını döner.
        Örn: 2d6 için: roll_multiple(2, 6)
        """
        return sum(random.randint(1, sides) for _ in range(dice_count))
