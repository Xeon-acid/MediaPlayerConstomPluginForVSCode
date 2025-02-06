# Media Player Custom Plugin Usage Instructions

This customization was completed with the help of DeepSeek. The author has not systematically learned Python, JavaScript, HTML, or CSS, so any errors in the code are welcome to be corrected by those with the expertise. The file `audio.jpg` is just for example, if there is any infringement, please contact the author to delete it immediately.

## Adjusting Transparency

Add the following line at the end of the file `<VS Code root directory>\resources\app\out\vs\workbench\workbench.desktop.main.css`:

```CSS
.monaco-workbench{opacity: 0.8 !important;}
```

You may see a warning, but it can be ignored. You can adjust the value `0.8` to your preferred opacity, but it is recommended not to go below `0.7`. Setting it to `1` makes it completely opaque, meaning the background will not be visible.

A script file `opacity.py` is provided in the same directory to set the transparency.

Usage:

```python
python .\opacity.py <Number between 0 and 1>
```

For example, running `python .\opacity.py 0.8` will set the transparency to `0.8`.

After making changes, you must restart VS Code for them to take effect.

## Replacing the HTML File

Place the provided `workbench.html` and `Run after Media added.py` files in the directory `<VS Code>\resources\app\out\vs\code\electron-sandbox\workbench`, replacing the original `workbench.html` file.

You can modify the content of the HTML file as needed.

## Refreshing the Media File List

A script file `Run after Media added.py` is provided in the same directory to set up the media file list.

Supported media files include `.mp4`, `.mp3`, `.wav`, and subtitle files `.lrc` and `.wav`.

Create a subdirectory named `media` in the same directory as `workbench.html`, and place your preferred media and subtitle files in it. Note that the prefix of the subtitle file must exactly match the corresponding media file's prefix.

Open a command line in this directory and run the Python script `Run after Media added.py`. The script will read all supported media files in the `media` directory and generate a list. Input the desired order, and the script will automatically reload the media file list into the `.html` file.

If you press Enter without input, the script will load all files in the default order. If you input `0` and press Enter, the script will load an empty list.

After modifying the `.html` file, including after running the Python script, restart VS Code or refresh the page as a local HTML webpage by clicking `Help -> Toggle Developer Tools` in the VS Code top bar.

## Status Bar Function Description

Several options are provided, with the following functions in order: switch to the previous media, pause/play, switch to the next media, toggle mute (with a logarithmic volume slider), toggle single-loop/playlist-loop, and directly select and switch media.

## Other Files

* **audio.jpg:** The background image when playing audio. You can change it, but make sure to update the name in the `.html` file accordingly, or the background image will not load.
* **ChironSungHK-B_0.ttf:** The font used for lyrics when subtitle files are present. You can change it, but ensure the name in the `.html` file is updated as well.

## Video Media Sound Issues

The `ffmpeg.dll` used by VS Code is customized. You can replace it with the corresponding version from Electron.

Steps:

1. In the top bar of VS Code, click `Help -> About` to check the Electron version.
2. Download the corresponding Electron version from [here](https://registry.npmmirror.com/binary.html?path=electron/), extract `ffmpeg.dll`, and replace the file with the same name in the VS Code root directory.
3. Restart the application.

## Notes
1. It is recommended to back up the original workbench.html and other related files to prevent issues that could render VS Code unusable. Otherwise, you may be forced to fix bugs using NotePad or other less convenient text editors.
2. **Do not** update VS Code. Updating the software will reset all directories and files in its root directory. You can either have a secure modification or an updated VS Code—there is no way to have both. Way to disabled auto-update is to press `Ctrl + Shift + P`, and type `Preferences: Open User Settings (JSON)`, and add a new line within the existed brace by:
   ```json
   "update.mode": "none",
   ```
   and press `Ctrl + S` to save your modification. Modfications here will always take effects immediately and permanently, thus restart VS Code is not needed.

## Unresolved Issues

As mentioned earlier, the author is not proficient in the languages used in this code. The following issues remain unresolved:

1. The customization may break some icons in the search functionality, but it does not affect usage.
2. The direct media selection button pops up a secondary menu for selection, and the styling of this menu is not ideal.