import os
import json

PHOTO_DIR = "assets/photos"
VIDEO_DIR = "assets/videos"

PHOTO_EXTS = (".jpg", ".jpeg", ".png", ".webp")
VIDEO_EXTS = (".mp4", ".mov", ".webm")

CONFIG_FILE = "config.json"


def scan_folder(folder, extensions):
    items = []

    if not os.path.exists(folder):
        return []

    for file in os.listdir(folder):
        if file.lower().endswith(extensions):
            full_path = os.path.join(folder, file)
            created = os.path.getctime(full_path)
            items.append((created, full_path.replace("\\", "/")))

    # Sort by creation time
    items.sort(key=lambda x: x[0])

    return [path for _, path in items]


def update_config():
    # Load existing config
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
    else:
        # Minimal fallback structure
        config = {
            "property": {},
            "photos": [],
            "videos": [],
            "embeds": []
        }

    # Scan folders
    photos = scan_folder(PHOTO_DIR, PHOTO_EXTS)
    videos = scan_folder(VIDEO_DIR, VIDEO_EXTS)

    # Update only these sections
    config["photos"] = photos
    config["videos"] = videos

    # Write back to config.json
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

    print(f"✅ {len(photos)} photos detected")
    print(f"🎬 {len(videos)} videos detected")
    print("📄 config.json updated successfully")


if __name__ == "__main__":
    update_config()
