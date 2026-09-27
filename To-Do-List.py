tasks = {"Utama": [], "Sedang": [], "Kecil": []}
limits = {"Utama": 1, "Sedang": 3, "Kecil": 5}

while True:
    print("\n To-Do-List 135 Menu")
    for category, task_list in tasks.items():
        print(f"[{category} {len(task_list)}/{limits[category]}]: {', '.join(task_list) or 'Kosong'}")

    category = input("\nMasukkan kategori (Utama/Sedang/Kecil) atau 'keluar': ").upper()
    if category == "KELUAR":
        break

    if category in tasks:
        if len(tasks[category]) >= limits[category]:
            print(f"kategori {category} sudah penuh")
        else:
            tugas = input(f"Masukkan tugas {category}: ")
            tasks[category].append(tugas)
