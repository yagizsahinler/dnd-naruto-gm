from application.mission_service import MissionService
from domain.mission import Mission


def prompt_for_mission(missions: list[Mission]) -> Mission | None:
    available = MissionService.list_available_missions(missions)

    if not available:
        print("✅ Tüm görevler tamamlandı!")
        return None

    print("\n📜 Mevcut Görevler:")
    for i, m in enumerate(available, start=1):
        print(f"{i}. {m}")

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
