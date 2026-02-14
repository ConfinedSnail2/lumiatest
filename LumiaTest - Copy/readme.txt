🛠 STEP-BY-STEP USAGE
STEP 1 — Duplicate The Folder
For a new property: Copy the entire project folder

Rename it (example: 1234-ocean-view)


STEP 2 — Add Photos
Place all property images inside:   assets/photos/
Supported formats:
.jpg
.jpeg
.png
.webp

Do not put images anywhere else.


STEP 3 — Add Videos (Optional)
Place videos inside:  assets/videos/
Supported formats:
.mp4
.mov
.webm


STEP 4 — Edit Property Info
Open: config.json

Edit the property section: UPDATE address, city, price, description fields.
{
  "property": {
    "address": "1234 Ocean View Drive",
    "city": "Malibu, CA",
    "price": "$4,995,000",
    "description": "Luxury oceanfront estate with panoramic views."
  }
}


STEP 5 — (Optional) Add Interactive Embeds
Inside config.json, edit:

"embeds": [
  {
    "title": "Matterport Tour",
    "url": "https://my.matterport.com/show/?m=YOUR_MODEL_ID"
  }

  {
  "title": "EXAMPLE EDITION HERE",
  "url": " WOULD PLACE THE URL OF THE TARGET EMBED HERE"
  }
]


Possible Additions in Embeds section are add:
Matterport tours
YouTube embeds
Vimeo embeds
    or
iframe-compatible link


STEP 6 — Auto-Fill Photos & Videos
Instead of manually listing photo/video paths in config.json, run:

python generate.py

This will:
Scan assets/photos
Scan assets/videos
Automatically update the photos and videos sections in config.json

YOU DO NOT need to manually upadate photos and videos section in the json.config