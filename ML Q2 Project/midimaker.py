#Code referencing pretty_midi documentation - https://craffel.github.io/pretty-midi/

import pretty_midi

# melody_notes = [61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 66, 66, 65, 66, 65, 65, 66, 65, 61, 63, 63, 65, 66, 66, 65, 66, 65, 63, 61, 66, 66, 68, 70, 68, 68, 70, 68, 65, 66, 61, 63, 66, 70, 68, 66, 68, 70, 68, 66, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 70, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 66, 66, 65, 66, 65, 65, 66, 65, 61, 63, 63, 65, 66, 66, 65, 66, 65, 63, 61, 66, 66, 68, 70, 68, 68, 70, 68, 65, 66, 61, 63, 66, 70, 68, 66, 68, 70, 68, 66, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 70, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 70, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66]
# chords = ['B:maj', 'B:maj', 'F#:maj', 'B:maj', 'Eb:min', 'Ab:min', 'Ab:min', 'C#:maj', 'F#:maj', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'F#:maj', 'Eb:min', 'F#:maj', 'F#:maj', 'F#:maj', 'F#:maj', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'F#:maj', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'F#:maj', 'Eb:min', 'F#:maj', 'F#:maj', 'F#:maj', 'F#:maj', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'F#:maj', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'F#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj', 'Eb:min', 'C#:maj', 'F#:maj', 'C#:maj', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'Eb:min', 'C#:maj']

melody_notes = [61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 66, 66, 65, 66, 65, 65, 66, 65, 61, 63, 63, 65, 66, 66, 65, 66, 65, 63, 61, 66, 66, 68, 70, 68, 68, 70, 68, 65, 66, 61, 63, 66, 70, 68, 66, 68, 70, 68, 66, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 70, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 66, 66, 65, 66, 65, 65, 66, 65, 61, 63, 63, 65, 66, 66, 65, 66, 65, 63, 61, 66, 66, 68, 70, 68, 68, 70, 68, 65, 66, 61, 63, 66, 70, 68, 66, 68, 70, 68, 66, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 70, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 70, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66, 61, 63, 66, 68, 70, 66, 63, 68, 68, 65, 61, 66, 61, 63, 66, 68, 70, 66, 63, 68, 61, 68, 66]
chords = ['Eb:maj(9)', 'Ab:maj', 'F:min/6', 'F:min7/5', 'C#:maj', 'F#:maj(9)', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Eb:min7/2', 'Ab:min7', 'F#:maj6(9)', 'F#:maj6(9)', 'E:maj(2)/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'C#:7', 'F#:maj(9)', 'C#:maj', 'F#:maj(9)', 'Eb:min7/2', 'Ab:7', 'C#:maj', 'Eb:min(9)/5', 'Eb:min7/2', 'F#:maj(9)', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'C#:maj', 'Ab:maj/3', 'Bb:min7', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'C#:maj', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Ab:min(9)', 'Eb:min7/2', 'Eb:min(9)/5', 'F#:maj6(9)', 'Ab:maj', 'C#:maj', 'Bb:min7', 'Eb:min7/2', 'F#:maj(9)', 'Ab:sus4', 'Eb:min7/2', 'Ab:min7', 'F#:maj6(9)', 'F#:maj/5', 'Eb:min(9)/5', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'Bb:min7', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'Eb:min(9)/5', 'Ab:min', 'C#:7', 'C#:maj', 'F#:maj(9)', 'F#:maj(9)', 'Ab:7', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Ab:min(9)', 'Eb:min7/2', 'Bb:min7', 'Eb:min7/2', 'F#:maj(9)', 'B:maj', 'F#:maj/5', 'B:maj', 'Eb:min7/2', 'F#:maj(9)', 'C#:maj', 'F#:maj7/3', 'F#:maj(9)', 'Ab:7', 'C#:maj', 'Ab:min', 'F#:maj6(9)', 'F#:maj(9)', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'C#:maj', 'Ab:maj/3', 'Bb:min7', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'C#:maj', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Ab:min(9)', 'Eb:min7/2', 'Eb:min(9)/5', 'F#:maj6(9)', 'Ab:maj', 'C#:maj', 'Bb:min7', 'Eb:min7/2', 'F#:maj(9)', 'Ab:sus4', 'Eb:min7/2', 'Ab:min7', 'F#:maj6(9)', 'F#:maj/5', 'Eb:min(9)/5', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'Bb:min7', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'Eb:min(9)/5', 'Ab:min', 'C#:7', 'C#:maj', 'F#:maj(9)', 'F#:maj(9)', 'Ab:7', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Ab:min(9)', 'Eb:min7/2', 'Bb:min7', 'Eb:min7/2', 'F#:maj(9)', 'Ab:maj', 'F#:maj/5', 'B:maj', 'Eb:min7/2', 'Ab:min7', 'F#:maj6(9)', 'Ab:min7', 'E:maj7(2)/2', 'E:maj7(2)/2', 'Bb:min7', 'Eb:min7/2', 'F#:min7(13)', 'Eb:min7/2', 'Eb:min7/2', 'B:maj', 'F#:maj/5', 'Ab:min7', 'F#:maj6(9)', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'Bb:min7', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Eb:min7/2', 'Ab:min7', 'F#:maj6(9)', 'E:maj7(2)/2', 'Ab:maj', 'C#:maj', 'Bb:min7', 'Eb:min7/2', 'F#:maj(9)', 'B:maj', 'F#:maj/5', 'Ab:min7', 'Eb:min7/2', 'Ab:min7', 'C#:7', 'F#:maj(9)', 'Ab:maj', 'C#:maj', 'F#:maj(9)', 'Ab:maj', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Ab:min(9)', 'Ab:min', 'C#:maj', 'C#:maj', 'F#:maj(9)', 'F#:maj(9)', 'Ab:maj', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'Eb:min7/2', 'F#:maj6(9)', 'Ab:min(9)', 'Eb:min7/2', 'Bb:min7']

bpm = 100
quarter_note_duration = 60.0 / bpm

midi = pretty_midi.PrettyMIDI()

melody_instrument = pretty_midi.Instrument(program=24) 

chord_instrument = pretty_midi.Instrument(program=0) 

lowest_melody_note = min(melody_notes)
chord_octave = (lowest_melody_note // 12) - 1 

for i, pitch in enumerate(melody_notes):
    start_time = i * quarter_note_duration / 2  
    end_time = start_time + (quarter_note_duration / 2)
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=end_time)
    melody_instrument.notes.append(note)

num_chords = len(chords)
for i in range(0, len(melody_notes), 4):
    chord_index = i // 4
    if chord_index < num_chords: 
        chord_name = chords[chord_index]
        start_time = i * quarter_note_duration / 2
        end_time = start_time + quarter_note_duration * 2 

        root_note = pretty_midi.note_name_to_number(chord_name.split(':')[0] + "3")  # Default to octave 3
        chord_type = chord_name.split(':')[1]

        chord_intervals = {"maj": [0, 4, 7], "min": [0, 3, 7]}
        intervals = chord_intervals.get(chord_type, [0, 4, 7])

        for interval in intervals:
            note = pretty_midi.Note(velocity=90, pitch=root_note + interval, start=start_time, end=end_time)
            chord_instrument.notes.append(note)

midi.instruments.append(melody_instrument)
midi.instruments.append(chord_instrument)

midi.write("generated_song_2.mid")
