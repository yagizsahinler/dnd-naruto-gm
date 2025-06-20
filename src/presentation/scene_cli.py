from infrastructure.scene_repo import SceneRepository


def prompt_scene_view() -> None:
    scenes = SceneRepository.load_scenes()

    if not scenes:
        print("📭 Hiç sahne verisi bulunamadı.")
        return

    print("\n🎭 Ortam İnceleme Menüsü")
    for i, scene in enumerate(scenes, start=1):
        print(f"{i}. {scene['name']}")

    print("0. Geri dön")

    while True:
        try:
            choice = int(input("Görüntülemek istediğin ortamın numarası: "))
            if choice == 0:
                return
            if 1 <= choice <= len(scenes):
                selected = scenes[choice - 1]
                print(f"\n🗺️ {selected['name']}\n{'-' * len(selected['name'])}")
                print(selected["description"])
                return
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
