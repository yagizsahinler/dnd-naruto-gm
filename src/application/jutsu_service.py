from domain.character import Character
from domain.jutsu import Jutsu
from core.dice import Dice


class JutsuService:

    @staticmethod
    def parse_dice_expression(expression: str) -> tuple[int, int]:
        """
        "1d8" gibi bir ifadeyi (1, 8) şeklinde çözümler.
        """
        try:
            count, sides = map(int, expression.lower().split("d"))
            return count, sides
        except Exception:
            raise ValueError(f"Geçersiz zar ifadesi: {expression}")

    @staticmethod
    def use_jutsu(character: Character, jutsu: Jutsu) -> dict:
        """
        Jutsu'yu kullan, zar at, hasarı hesapla, CP düş, sonuçları döndür.
        """
        if character.cp < jutsu.cp_cost:
            raise ValueError(f"Yetersiz CP. Gerekli: {jutsu.cp_cost}, mevcut: {character.cp}")

        dice_count, dice_sides = JutsuService.parse_dice_expression(jutsu.damage_dice)

        # Stat modifiyeri belirleme
        if jutsu.jutsu_type == "Taijutsu":
            modifier = character.get_modifier(character.stats["STR"])
        elif jutsu.jutsu_type == "Ninjutsu":
            modifier = character.get_modifier(character.stats["WIS"])
        elif jutsu.jutsu_type == "Genjutsu":
            modifier = character.get_modifier(character.stats["CHA"])
        else:
            modifier = 0

        # Zar atımı
        total_damage = Dice.roll_multiple(dice_count, dice_sides)
        base_roll, is_crit_success, is_crit_fail = Dice.roll(dice_sides, modifier)

        # Kritik başarı/başarısızlık etki
        if is_crit_success:
            total_damage += dice_sides  # bonus zar
            actual_cp_cost = jutsu.cp_cost // 2
        elif is_crit_fail:
            total_damage = 0
            actual_cp_cost = jutsu.cp_cost  # yine de CP gider
        else:
            actual_cp_cost = jutsu.cp_cost

        # CP düşür, kullanım sayısı artır
        character.cp -= actual_cp_cost
        jutsu.use()

        return {
            "damage": total_damage,
            "cp_spent": actual_cp_cost,
            "crit_success": is_crit_success,
            "crit_fail": is_crit_fail,
            "evolved": jutsu.is_evolved(),
            "remaining_cp": character.cp
        }
