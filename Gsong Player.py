import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy.io import wavfile
import os

DEFAULT_GSONG_FOLDER = os.path.expanduser(r"~\OneDrive\Documentos\UltimakerGcodesongs")
TEMP_WAV_FOLDER = os.path.join(os.environ['TEMP'], "gcodesongs")

def load_file():
    initial_dir = DEFAULT_GSONG_FOLDER if os.path.exists(DEFAULT_GSONG_FOLDER) else os.path.expanduser("~")
    filename = filedialog.askopenfilename(initialdir=initial_dir, title="Select file",
                                          filetypes=(("gsong files", "*.gsong"), ("all files", "*.*")))
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

def convert_to_wav():
    filename = file_entry.get()
    if not filename.endswith(".gsong"):
        error_label.config(text="Invalid file type")
        return

    with open(filename) as f:
        lines = f.readlines()

    notes = []
    for line in lines:
        if line.startswith("M300"):
            parts = line.split()
            duration = int(parts[1][1:])
            frequency = int(parts[2][1:])
            note = np.sin(2*np.pi*np.arange(44100*duration/2000)*frequency/44100)
            notes.append(note)
        elif line.startswith("G4"):
            parts = line.split()
            duration = int(parts[1][1:])
            note = np.zeros(int(44100*duration/2000))
            notes.append(note)

    wav_data = np.concatenate(notes)
    wav_data *= 32767 / np.max(np.abs(wav_data))  # escalar los datos de audio
    wav_data = wav_data.astype(np.int16)  # convertir a entero de 16 bits

    os.makedirs(TEMP_WAV_FOLDER, exist_ok=True)
    temp_wav_file = os.path.join(TEMP_WAV_FOLDER, "temp.wav")
    wavfile.write(temp_wav_file, 44100, wav_data)
    temp_wav_file = os.path.join(TEMP_WAV_FOLDER, "temp.wav")
    if os.path.exists(temp_wav_file):
        os.system(f"start {temp_wav_file}")


def cleanup():
    temp_wav_file = os.path.join(TEMP_WAV_FOLDER, "temp.wav")
    if os.path.exists(temp_wav_file):
        os.remove(temp_wav_file)
    window.destroy()

window = tk.Tk()
window.title("Gsong Converter")

file_label = tk.Label(window, text="File:")
file_label.grid(row=0, column=0)

file_entry = tk.Entry(window, width=50)
file_entry.grid(row=0, column=1)

file_button = tk.Button(window, text="Load file", command=load_file)
file_button.grid(row=0, column=2)

convert_button = tk.Button(window, text="Play", command=convert_to_wav)
convert_button.grid(row=1, column=1)

error_label = tk.Label(window, text="")
error_label.grid(row=2, column=1)

window.protocol("WM_DELETE_WINDOW", cleanup)
window.mainloop()
