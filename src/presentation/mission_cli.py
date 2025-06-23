from application.mission_service import MissionService
from domain.mission import Mission
from infrastructure.character_repo import CharacterRepository
from infrastructure.mission_repo import MissionRepository
from ai.generate_scene import generate_scene_prompt, run_ollama_mistral


def prompt_for_mission(missions: list[Mission]) -> Mission | None:
    available = MissionService.list_available_missions(missions)

    if not available:
        print("✅ Tüm görevler tamamlandı!")
        return None

    print("\n📜 Mevcut Görevler:")
    for i, m in enumerate(available, start=1):
        print(f"{i}. {m.title} ({m.location})")

    while True:
        try:
            choice = int(input("\nTamamlamak istediğin görevin numarası (0 = çıkış): "))
            if choice == 0:
                return None
            if 1 <= choice <= len(available):
                return available[choice - 1]
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Lütfen sayı giriniz.")


def run_mission_flow(character_path: str, missions_path: str) -> None:
    missions = MissionRepository.load_missions(missions_path)
    selected = prompt_for_mission(missions)
    if selected is None:
        return

    # Karakteri yükle
    character = CharacterRepository.load_character(character_path)

    # Sahne üret
    location = selected.location
    summary = selected.description
    context = getattr(selected, "previous_context", "The mission is about to begin.")

    prompt = generate_scene_prompt(character, location, summary, context)
    scene_text = run_ollama_mistral(prompt)

    # Sonuçları göster
    print("\n🎬 AI-Generated Scene\n" + "-" * 30)
    print(scene_text)

    print(f"\n🎮 Görev başlatıldı: {selected.title}")


# Test amaçlı çalıştırma
if __name__ == "__main__":
    character_path = "data/character.json"
    missions_path = "data/missions.json"
    run_mission_flow(character_path, missions_path)
