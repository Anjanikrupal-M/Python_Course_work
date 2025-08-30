import os
import json

# Directory to store anime data
anime_dir = "Assignments/anime_data"
os.makedirs(anime_dir, exist_ok=True)

def sanitize_filename(filename):
    """Ensure safe filenames for anime storage."""
    filename = filename.strip().replace(" ", "_")
    if not filename.endswith(".json"):
        filename += ".json"
    return filename

def add_anime():
    """Add a new anime entry."""
    title = input("Enter Anime Title: ").strip()
    filename = sanitize_filename(title)
    filepath = os.path.join(anime_dir, filename)

    if os.path.exists(filepath):
        print("❌ Anime already exists! Try modifying instead.")
        return

    genre = input("Enter Genre: ")
    episodes = input("Enter Number of Episodes: ")
    status = input("Enter Status (Watching / Completed / Plan to Watch / Dropped): ")
    rating = input("Enter Rating (1-10, optional): ") or "N/A"

    anime = {
        "title": title,
        "genre": genre,
        "episodes": episodes,
        "status": status,
        "rating": rating
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(anime, f, indent=4)

    print(f"✅ Anime '{title}' added successfully!")

def list_animes():
    """List all anime shows and return file list."""
    files = os.listdir(anime_dir)
    if not files:
        print("No anime shows found.")
        return []

    print("\n📺 Anime List:")
    for i, file in enumerate(files, start=1):
        with open(os.path.join(anime_dir, file), "r", encoding="utf-8") as f:
            anime = json.load(f)
        # Show only title (no status or rating here)
        print(f"{i}. {anime['title']}")
    return files

def view_anime_details():
    """View full details of a selected anime."""
    files = list_animes()
    if not files:
        return

    choice = input("Enter anime title to view details: ").strip()
    filename = sanitize_filename(choice)
    filepath = os.path.join(anime_dir, filename)

    if not os.path.exists(filepath):
        print("❌ Anime not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        anime = json.load(f)

    print("\n📖 Anime Details:")
    for k, v in anime.items():
        print(f"{k}: {v}")

def modify_anime():
    """Modify existing anime entry."""
    files = list_animes()
    if not files:
        return

    choice = input("Enter anime title to modify: ").strip()
    filename = sanitize_filename(choice)
    filepath = os.path.join(anime_dir, filename)

    if not os.path.exists(filepath):
        print("❌ Anime not found.")
        return

    with open(filepath, "r", encoding="utf-8") as f:
        anime = json.load(f)

    print("\nCurrent Info:")
    for k, v in anime.items():
        print(f"{k}: {v}")

    print("\nEnter new values (leave blank to keep current):")
    anime["genre"] = input(f"Genre ({anime['genre']}): ") or anime["genre"]
    anime["episodes"] = input(f"Episodes ({anime['episodes']}): ") or anime["episodes"]
    anime["status"] = input(f"Status ({anime['status']}): ") or anime["status"]
    anime["rating"] = input(f"Rating ({anime['rating']}): ") or anime["rating"]

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(anime, f, indent=4)

    print(f"✅ Anime '{anime['title']}' updated successfully!")

def anime_summary():
    """Show how many animes are completed, watching, etc."""
    files = os.listdir(anime_dir)
    if not files:
        print("No anime shows found.")
        return

    status_count = {"Watching": 0, "Completed": 0, "Plan to Watch": 0, "Dropped": 0}

    for file in files:
        with open(os.path.join(anime_dir, file), "r", encoding="utf-8") as f:
            anime = json.load(f)
            status = anime.get("status", "Unknown")
            if status in status_count:
                status_count[status] += 1

    print("\n📊 Anime Collection Summary:")
    for status, count in status_count.items():
        print(f"{status}: {count} shows")

def main():
    """Main menu for Anime Management System."""
    while True:
        print("\n🎌 Anime Management System")
        print("1. List Anime Shows")
        print("2. Add New Anime")
        print("3. View Anime Details")
        print("4. Modify Anime")
        print("5. Anime Collection Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_animes()
        elif choice == "2":
            add_anime()
        elif choice == "3":
            view_anime_details()
        elif choice == "4":
            modify_anime()
        elif choice == "5":
            anime_summary()
        elif choice == "6":
            print("👋 Exiting... Goodbye, Otaku!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
