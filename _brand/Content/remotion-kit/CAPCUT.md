# How to edit the v4 reel in CapCut

This folder is the $200,000 automation reel **v4** taken apart into layers. Use **CapCut on your computer**. The phone app can't import the caption file. Menu names below match recent CapCut desktop versions and may differ slightly in yours.

## What's in the folder

| File | What it is |
|---|---|
| `footage.mp4` | Your talking footage with the zooms. In the split-screen parts it's already positioned in the bottom half, with black on top for the graphics to cover. Its sound is your raw voice, for lining things up. |
| `graphics.mov` | **All the graphics on one transparent layer**: glass background, screenshots, step cards, the $200,000 card, 3D icons and logos. It runs the full length of the reel. |
| `graphics_on_magenta.mp4` | The same graphics on solid magenta. Only use this if `graphics.mov` shows a black background in CapCut (see step 4). |
| `voice.wav`, `music.wav`, `sfx.wav` | The sound, in three parts that add up to the finished mix |
| `captions.srt` | All 70 captions with timings |
| `timings.txt` | When each part happens, and where captions sit |

## 1. Get the folder ready

In Google Drive, right-click the folder and choose **Available offline**. `graphics.mov` is a large file, and CapCut stalls if it's still downloading.

## 2. Start the project

Open CapCut, click **Create project**, then **Import** and select every file in the folder.

## 3. Footage and sound

1. Drag `footage.mp4` onto the main track at 0:00. The canvas switches to 9:16.
2. Mute its sound with the speaker icon at the left of the main track.
3. Drag `voice.wav`, `music.wav` and `sfx.wav` onto three separate audio tracks, each starting at 0:00.

## 4. Graphics

1. Drag `graphics.mov` onto a track **above** the footage, starting at 0:00. It's exactly the same length.
2. Play it. You should see your footage wherever there are no graphics.
3. **If you see black instead of your footage**, CapCut hasn't read the transparency:
   - Delete `graphics.mov` and put `graphics_on_magenta.mp4` in its place, at 0:00.
   - Select it, open **Video → Remove BG → Chroma key**, use the colour picker to click the magenta, and raise **Intensity** until the magenta is gone and your footage shows.
   - You may see a faint pink edge around the logo tiles' shadows. Lowering **Shadow** in the chroma key settings helps.

## 5. Captions

1. Go to **Text → Local captions → Import** and pick `captions.srt`.
2. Style one caption: white, black **Stroke** about 6–8, bold. Use TikTok Sans if CapCut lists it, otherwise the default bold. Then use the apply-to-all option.
3. **Position:** most captions sit just below your chin, about three-quarters of the way down. During the split-screen parts (times in `timings.txt`), they sit higher, just above the line where the graphics meet your footage, so they don't cover your face. To do that, select the captions in those windows and drag them up.

GoHighLevel and Claude have no caption on purpose, because their logos pop up instead.

## 6. Export

**Export** → 1080p, 30 fps, MP4 (H.264), bit rate Higher. Save it to `Exports/` as `2026-11-04_200k-automation_v5.mp4`. Never overwrite an older version.
