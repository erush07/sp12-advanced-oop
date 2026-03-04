'''
OPTIONAL AI GUIDANCE PROMPT
---------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions
to a practice problem that my professor gave me to try before class.
Please be my kind tutor and walk me through how to solve the problem step
by step.

Don't just give me the full solution all at once (unless I later ask for
it). Instead, help me work through it gradually, with clear explanations
and small, easy-to-understand examples. Please use everyday language and
explain things in a simple, friendly way.

INSTRUCTIONS:
-------------
Another look at aggregation, collecting independent objects.
1. Create a Track class storing title and duration_seconds.
2. Create a Playlist class that keeps a list of Track objects.
3. add_track(self, track) appends a Track to the list.
4. total_duration(self) loops through tracks (no list comprehension)
   to sum seconds, then returns the result as minutes:seconds text.
5. Make three tracks, add them, then print total_duration().
'''

class Track:
   def __init__(self, title, duration_seconds):
      self.title = title
      self.duration_seconds = duration_seconds
class Playlist:
   def __init__(self):
      self.track_list = []

   def add_track(self, track):
      self.track_list.append(track)

   def total_duration(self):
      total = 0
      for track in self.track_list:
         total += track.duration_seconds
         minutes = total//60
         seconds = total % 60
      return f"{minutes}:{seconds:02}"

track_1 = Track("Hello", 120)
track_2 = Track("Goodbye", 375)
track_3 = Track("Happy", 235)

playlist_1 = Playlist()
playlist_1.add_track(track_1)
playlist_1.add_track(track_2)
playlist_1.add_track(track_3)

print(playlist_1.total_duration())