import os
import pretty_midi
import pandas as pd


POP909_DIR = "POP909/"  
OUTPUT_DIR = "Output/"
PREVIOUS_CHORDS = 4  


def getActiveKey(time, keys):
    active_key = keys[(keys["start"] <= time) & (keys["end"] > time)]
    return active_key["key"].iloc[0] if not active_key.empty else "Unknown"


def parseMidi(midi_path, chord_path, key_path):

    midi = pretty_midi.PrettyMIDI(midi_path)
    chords = pd.read_csv(chord_path, sep="\t", header=None, names=["start", "end", "label"])
    keys = pd.read_csv(key_path, sep="\t", header=None, names=["start", "end", "key"])

    keys_dict = {}
    melody_notes = []
    for instrument in midi.instruments:
        if instrument.name.lower() == "melody":
            melody_notes = instrument.notes

    previous_chords = []
    for _, chord_row in chords.iterrows():
        start, end, chord_label = chord_row["start"], chord_row["end"], chord_row["label"]
        active_key = getActiveKey(start, keys)
        melody_sequence = tuple(note.pitch for note in melody_notes if start <= note.start < end)
        if not melody_sequence:
            continue

        if active_key not in keys_dict:
            keys_dict[active_key] = {}
        if melody_sequence not in keys_dict[active_key]:
            keys_dict[active_key][melody_sequence] = {"chords": {}}

        prev_chords_list = previous_chords[-PREVIOUS_CHORDS:]
        prev_chords_list = ["None"] * (PREVIOUS_CHORDS - len(prev_chords_list)) + prev_chords_list 

        prev_chords_tuple = tuple(prev_chords_list)
        if prev_chords_tuple not in keys_dict[active_key][melody_sequence]["chords"]:
            keys_dict[active_key][melody_sequence]["chords"][prev_chords_tuple] = {}
        if chord_label not in keys_dict[active_key][melody_sequence]["chords"][prev_chords_tuple]:
            keys_dict[active_key][melody_sequence]["chords"][prev_chords_tuple][chord_label] = 0
        keys_dict[active_key][melody_sequence]["chords"][prev_chords_tuple][chord_label] += 1

        previous_chords.append(chord_label)

    return keys_dict


def loadDataset(pop909_dir, output_dir):

    keys_dict = {}
    for folder_name in sorted(os.listdir(pop909_dir)):
        folder_path = os.path.join(pop909_dir, folder_name)
        if not os.path.isdir(folder_path):
            continue

        midi_path = os.path.join(folder_path, f"{folder_name}.mid")
        chord_path = os.path.join(folder_path, "chord_audio.txt")
        key_path = os.path.join(folder_path, "key_audio.txt")
        song_keys_dict = parseMidi(midi_path, chord_path, key_path)

        for active_key, melody_sequences in song_keys_dict.items():
            if active_key not in keys_dict:
                keys_dict[active_key] = {}
            for melody_seq, data in melody_sequences.items():
                if melody_seq not in keys_dict[active_key]:
                    keys_dict[active_key][melody_seq] = {"chords": {}}
                for prev_chords, chords_dict in data["chords"].items():
                    if prev_chords not in keys_dict[active_key][melody_seq]["chords"]:
                        keys_dict[active_key][melody_seq]["chords"][prev_chords] = {}
                    for chord, count in chords_dict.items():
                        keys_dict[active_key][melody_seq]["chords"][prev_chords][chord] = (
                            keys_dict[active_key][melody_seq]["chords"][prev_chords].get(chord, 0) + count
                        )

    saveDictToCSV(keys_dict, os.path.join(output_dir, "keys_dict"))
    return keys_dict


def saveDictToCSV(data_dict, csv_filename):
    csvArray = []
    for active_key, melody_sequences in data_dict.items():
        for melody_seq, data in melody_sequences.items():
            for prev_chords, chords_dict in data["chords"].items():
                for chord, count in chords_dict.items():
                    row = {
                        "active_key": active_key,
                        "melody_sequence": melody_seq,
                        "chord": chord,
                        "chord_count": count,
                    }
                    for i in range(PREVIOUS_CHORDS):
                        row[f"prev_chord_{i+1}"] = prev_chords[i]
                    csvArray.append(row)
    pd.DataFrame(csvArray).to_csv(f"{csv_filename}.csv", index=False)


def main():
    loadDataset(pop909_dir=POP909_DIR, output_dir=OUTPUT_DIR)


if __name__ == "__main__":
    main()