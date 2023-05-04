# Random Song Plugin for Ultimaker Cura

**Disclaimer:**
I'm new to programming, but I did manage to make it work for me while keeping an eye on security. Feel free to modify it to your preferences and make it better...

## Summary

This plugin for Ultimaker Cura selects a random song from a folder and plays it when printing finishes. This is a useful add-on for customizing the end of your print and adding a fun touch.

## Installation

1. Download the plugin zip file from this [GitHub repository](https://github.com/rodrigomauricio/cura_random_song_plugin).
2. Unzip the .py file to the scripts at `C:\Program Files\Ultimaker Cura {Cura version}\share\cura\plugins\PostProcessingPlugin\scripts`.
3. Open Cura and activate the plugin in the "Extensions" menu.

## Usage

1. Create a folder called "UltimakerGcodesongs" in your OneDrive's document folder (`C:\Users\[USER]\OneDrive\Documentos`).
2. Add `.gsong` files to this folder. These files should contain M300 or G4 commands that play the desired song. See the "Song file format" section for more information about the song file format.
3. Open Cura and load a model.
4. Click "Prepare" to generate the G-code.
5. If the plugin is enabled, an M300 command that plays a random song will be automatically added to the end of the G-code.

## Song file format

`.gsong` files should contain M300 (plays a note) or G4 (waits) commands that play the desired song,those are the only commands the plugin can read, other commands are ignored for security reasons. 
Each command should be on a separate line. 

- `P` = Duration in ms
- `S` = Frequency in Hz (A4=440hz)

For example:

M300 P149 S1760
G4 P149
M300 P165 S92
G4 P165
M300 P324 S0
G4 P324
M300 P319 S1568
G4 P319
M300 P149 S1480
G4 P149
M300 P128 S73
G4 P128
M300 P191 S82
G4 P191
M300 P170 S92
G4 P170
M300 P340 S1319
G4 P340
M300 P298 S1480


### How to get M300 Code from a midi file:

1. Load your midi file to: [https://alexyu132.github.io/midi-m300/](https://alexyu132.github.io/midi-m300/)
2. Select the instrument you prefer (3D printers reproduce 1 sound at a time).
3. Click "Generate".
4. Copy the notes you want to play.
5. Paste it on a new notepad file and save it as `Name.gsong` in the folder you created before. 

If you want to try the G-code you can copy it to your SD and change its format to `.gcode`, or use the gsong player I added to this repository.

