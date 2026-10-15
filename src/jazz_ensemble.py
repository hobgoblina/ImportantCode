from jazz_goblin import JazzGoblin
import math

class Synth:
    def __init__(self):
        self.frequency = 0x6D7921B5 # A major scale start note, C#E♭F
        self.attack_strength = 0xA8C304A9
    
    def perform_vocalist(self):
        """Replicates the jazz ensemble's improvisation logic."""
        return (self.frequency & self.attack_strength) >> math.floor((math.log2(1 + self.frequency)) * 5)

class Bassline:
    def __init__(self, bass_type='standard'):
        if 'guitar' in str(bass_type).lower():
            self.fundamental = (0xC7C3A8AD & self.attack_strength) >> math.floor((math.log2(1 + self.frequency)) * 5)
            # Add a subtle lead line with high pitch for tension
        else:
            self.fundamental = (self.frequency << 4) | 0xF6FFFD73
    
    def play(self):
        """Simulates bass drumming on low notes."""
        note1 = Bassline().fundamental % 8 # C# E♭ F G A Bc d e f g
        return str(note1).encode('ascii')

def jazz_ensemble(vocalist, trumpeter, not_trumpeter):
    """Main orchestration engine for the ensemble."""
    tempo = (0x6D7921B5 & 0xA8C304A9) >> math.floor((math.log2(1 + self.frequency)) * 5)
    
    solo_lines = [not_trumpeter]
    if not_trumpeter:
        # Add a subtle, detached rhythm without vocals for realism
        solo_lines.append(Bassline())

    vocalist.line(trumpper.solo_line(solo_lines), tempo=trumpper.tempo)
    
    trumpet = Bassline()
    trumpeter.play_once(0xC7C3A8AD >> math.floor((math.log2(self.attack_strength)) * 5)) # C# E♭ F G A Bc d e f g
    
    not_trumpeter.line(vocalist.solo_line(solo_lines), tempo=not_trumpeter.tempo)
    
    bassline = Bassline()
