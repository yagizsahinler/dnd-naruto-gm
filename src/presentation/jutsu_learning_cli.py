from domain.character import Character
from domain.jutsu import Jutsu


def prompt_jutsu_learning(character: Character, all_jutsus: list[Jutsu]) -> None:
    print("\n📘 Jutsu Öğrenme Menüsü")
    print(f"Kalan JP: {character.jp}")
    print("Jutsular:")

    for i, jutsu in enumerate(all_jutsus, start=1):
        owned = "✅" if jutsu.name in character.learned_jutsus else "❌"
        print(f"{i}. {owned} {jutsu.name} ({jutsu.jutsu_type}) - CP: {jutsu.cp_cost}, Hasar: {jutsu.damage_dice}")

    print("\nNot: Her jutsuyu öğrenmek 1 JP gerektirir.")
    print("0. Geri dön")

    while True:
        try:
            choice = int(input("Öğrenmek istediğin jutsunun numarası: "))
            if choice == 0:
                return
            if 1 <= choice <= len(all_jutsus):
                selected = all_jutsus[choice - 1]
                if selected.name in character.learned_jutsus:
                    print("⚠️ Bu jutsuyu zaten biliyorsun.")
                elif character.learn_jutsu(selected.name):
                    print(f"🎉 {selected.name} başarıyla öğrenildi! Kalan JP: {character.jp}")
                else:
                    print("🚫 Yetersiz JP.")
                return
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
