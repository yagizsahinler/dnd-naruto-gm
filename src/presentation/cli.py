from application.character_service import CharacterService
from domain.character import Character


def prompt_for_character() -> Character:
    print("🌀 Naruto D&D Karakter Oluşturma Arayüzü")
    name = input("Karakter adı: ").strip()

    print("Mevcut rank'lar: Genin, Chuunin, Jounin, ANBU, Sannin")
    rank = input("Rank: ").strip()

    print("Mevcut klanlar: Uchiha, Hyuga, Haruno, Nara, Aburame, Inuzuka")
    clan = input("Klan: ").strip()

    print("Mevcut elementler: Fire, Water, Wind, Earth, Lightning")
    element = input("Element: ").strip()

    stats = {}
    print("Her stat için 1–20 arasında bir değer giriniz.")
    for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
        while True:
            try:
                val = int(input(f"{stat}: "))
                if 1 <= val <= 20:
                    stats[stat] = val
                    break
                else:
                    print("Hata: Değer 1–20 arasında olmalı.")
            except ValueError:
                print("Hata: Sayısal bir değer giriniz.")

    try:
        character = CharacterService.create_character(
            name=name,
            rank=rank,
            clan=clan,
            element=element,
            stats=stats
        )
        print(f"\n✅ {character.name} başarıyla oluşturuldu!")
        print(f"Seviye: {character.level}, CP: {character.cp}, HP: {character.hp}")
        return character
    except ValueError as e:
        print(f"\n🚫 Hata: {e}")
        return None
