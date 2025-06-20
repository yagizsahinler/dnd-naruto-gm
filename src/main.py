from presentation.cli import prompt_for_character
from presentation.mission_cli import prompt_for_mission
from presentation.jutsu_learning_cli import prompt_jutsu_learning
from presentation.scene_cli import prompt_scene_view
from infrastructure.file_repo import CharacterFileRepository
from infrastructure.scene_repo import SceneRepository
from application.jutsu_service import JutsuService
from application.mission_service import MissionService


def select_jutsu(jutsu_list):
    print("\n🧬 Mevcut Jutsular:")
    for i, jutsu in enumerate(jutsu_list, start=1):
        print(f"{i}. {jutsu}")
    while True:
        try:
            choice = int(input("\nKullanmak istediğin jutsu numarası (0 = çıkış): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(jutsu_list):
                return jutsu_list[choice - 1]
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Lütfen bir sayı girin.")


def rest_menu(character):
    print("\n🛌 Dinlenme Seçenekleri:")
    print("1. Kısa Dinlenme (1d6 + WIS mod CP)")
    print("2. Uzun Dinlenme (CP tamamen yenilenir)")
    print("0. Geri dön")

    choice = input("Seçimin: ").strip()

    if choice == "1":
        recovered = character.short_rest()
        print(f"🌿 Kısa dinlenme → +{recovered} CP (Toplam CP: {character.cp})")
    elif choice == "2":
        character.long_rest()
        print(f"🌀 Uzun dinlenme → CP tamamen doldu ({character.cp})")
    elif choice == "0":
        return
    else:
        print("❌ Geçersiz seçim.")


if __name__ == "__main__":
    # Karakteri yükle veya oluştur
    character = CharacterFileRepository.load_character()
    if not character:
        character = None
        while character is None:
            character = prompt_for_character()
        CharacterFileRepository.save_character(character)

    # Jutsu ve görevleri yükle
    all_jutsus = CharacterFileRepository.load_jutsus()
    mission_list = CharacterFileRepository.load_missions()

    while True:
        print(f"\n👤 {character.name} | Seviye: {character.level} | CP: {character.cp} | EXP: {character.exp} | JP: {character.jp}")
        print("\n🔹 Ne yapmak istiyorsun?")
        print("1. Jutsu Kullan")
        print("2. Görev Tamamla")
        print("3. Dinlen")
        print("4. Jutsu Öğren")
        print("5. Ortamı İncele")
        print("0. Çıkış")

        choice = input("Seçimin: ").strip()

        if choice == "1":
            available = [j for j in all_jutsus if j.name in character.learned_jutsus]
            if not available:
                print("📭 Henüz jutsu öğrenmedin.")
            else:
                jutsu = select_jutsu(available)
                if jutsu:
                    try:
                        result = JutsuService.use_jutsu(character, jutsu)
                        print(f"\n⚔️ {jutsu.name} kullanıldı!")
                        print(f"Hasar: {result['damage']}")
                        print(f"CP Harcandı: {result['cp_spent']} | Kalan CP: {result['remaining_cp']}")
                        if result["crit_success"]:
                            print("🔥 Kritik başarı!")
                        elif result["crit_fail"]:
                            print("💥 Kritik başarısızlık!")
                        if result["evolved"]:
                            print("⚡ Jutsu evrimleşti!")
                    except ValueError as e:
                        print(f"🚫 Hata: {e}")

        elif choice == "2":
            mission = prompt_for_mission(mission_list)
            if mission:
                result = MissionService.complete_mission(character, mission)
                print(result)

        elif choice == "3":
            rest_menu(character)

        elif choice == "4":
            prompt_jutsu_learning(character, all_jutsus)

        elif choice == "5":
            prompt_scene_view()

        elif choice == "0":
            print("👋 Çıkış yapılıyor. Karakter kaydediliyor...")
            CharacterFileRepository.save_character(character)
            break

        else:
            print("❌ Geçersiz seçim. Lütfen tekrar dene.")
