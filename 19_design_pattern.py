"""
DESIGN PATTERN:
Creational patterns
Structural patterns
Behavioral patterns
Architectural patterns
"""

# creational pattern: factory method
# gunakan factory method untuk create instances dari concrete media players
from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename):
        pass


class AudioPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing Audio file {filename}")


class VideoPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing video file {filename}")


# factory method
class MediaPlayerFactory:
    @staticmethod
    def create_media_player(media_type):
        if media_type == "audio":
            return AudioPlayer()
        elif media_type == "video":
            return VideoPlayer()
        else:
            raise ValueError


class Player:
    def __init__(self, media_type):
        self.media_player = MediaPlayerFactory.create_media_player(media_type)

    def play_media(self, filename):
        self.media_player.play(filename)


# usage
player1 = Player(media_type="audio")
player1.play_media("song.mp3")

player2 = Player("video")
player2.play_media("movie.mp4")


# STRUCTURAL PATTERN: ADAPTER
# use adapter pattern to make different media players conform a common interface
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename):
        pass


class AudioPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing audio file: {filename}")


class VideoPlayer:
    def play_video(self, filename):
        print(f"Playing video file: {filename}")


class VideoPlayerAdapter(MediaPlayer):  # ADAPTER pattern
    def __init__(self, video_player):
        self.video_player = video_player

    def play(self, filename):
        self.video_player.play_video(filename)


class Player:
    def __init__(self, media_player):
        self.media_player = media_player

    def play_media(self, filename):
        self.media_player.play(filename)


# Usage
audio_player = AudioPlayer()
video_player = VideoPlayerAdapter(VideoPlayer())

player1 = Player(audio_player)
player1.play_media("song.mp3")  # Output: Playing audio file: song.mp3

player2 = Player(video_player)
player2.play_media("movie.mp4")  # Output: Playing video file: movie.mp4


# BEHAVIORAL PATTERN: strategy pattern to encapsulate different playback strategies
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename):
        pass


class AudioPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing audio file: {filename}")


class VideoPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing video file: {filename}")


# strategy pattern
class Player:
    def __init__(self, media_player):
        self.media_player = media_player

    def play_media(self, filename):
        self.media_player.play(filename)


# Usage
audio_player = AudioPlayer()
video_player = VideoPlayer()

player1 = Player(audio_player)
player1.play_media("song.mp3")  # Output: Playing audio file: song.mp3

player2 = Player(video_player)
player2.play_media("movie.mp4")  # Output: Playing video file: movie.mp4


# ARCHITECTURAL PATTERN: MVC (MODEL-VIEW-CONTROLLER)
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, filename):
        pass


class AudioPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing audio file: {filename}")


class VideoPlayer(MediaPlayer):
    def play(self, filename):
        print(f"Playing video file: {filename}")


class Controller:
    def __init__(self):
        self.media_player = None

    def set_media_player(self, media_player):
        self.media_player = media_player

    def play_media(self, filename):
        self.media_player.play(filename)


# Usage
audio_player = AudioPlayer()
video_player = VideoPlayer()

controller1 = Controller()
controller1.set_media_player(audio_player)
controller1.play_media("song.mp3")  # Output: Playing audio file: song.mp3

controller2 = Controller()
controller2.set_media_player(video_player)
controller2.play_media("movie.mp4")  # Output: Playing video file: movie.mp4
