import logging
import queue

import pykka
from mopidy import core

from mopidy_vfd.character_display_noritake import CharacterDisplayNoritake
from mopidy_vfd.display_controller import DisplayController
from mopidy_vfd.player_status import PlayerState, PlayerStatus

logger = logging.getLogger(__name__)


class MopidyClient(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super().__init__()
        self.core = core
        self.confg = config
        self.status_queue = None

    def on_start(self):
        self.player_status = PlayerStatus()
        self.status_queue = queue.Queue()

        self.display_controller = DisplayController(
            self.status_queue, CharacterDisplayNoritake()
        )
        self.display_controller.start()

    def on_stop(self):
        self.display_controller.stop()
        self.display_controller = None
        self.status_queue.join()

    def seeked(self, time_position):
        self.player_status.elapsed = time_position
        self.status_queue.put(self.player_status, block=False)

    def stream_title_changed(self, title):
        self.player_status.part = title
        self.status_queue.put(self.player_status, block=False)

    def track_playback_ended(self, tl_track, time_position):
        self._update(tl_track.track, time_position, PlayerState.Stopped)

    def track_playback_paused(self, tl_track, time_position):
        self._update(tl_track.track, time_position, PlayerState.Paused)

    def track_playback_resumed(self, tl_track, time_position):
        self._update(tl_track.track, time_position, PlayerState.Playing)

    def track_playback_started(self, tl_track):
        self._update(tl_track.track, 0.0, PlayerState.Playing)

    def _update(self, track, elapsed, state):

        performer = ""
        composer = ""
        oeuvre = ""
        part = ""

        if track.performers is not None:
            performer = ", ".join(
                [performer.name for performer in track.performers]
            )

        if track.composers is not None:
            composer = ", ".join(
                [composer.name for composer in track.composers]
            )
        elif track.artists is not None:
            composer = ", ".join([artist.name for artist in track.artists])

        if track.album is not None and track.album.name is not None:
            oeuvre = track.album.name

        if track.name is not None:
            part = track.name

        self.player_status.state = state
        self.player_status.elapsed = elapsed
        self.player_status.performer = performer
        self.player_status.composer = composer
        self.player_status.oeuvre = oeuvre
        self.player_status.part = part

    def volume_changed(self, volume):
        if volume is not None:
            self.player_status.volume = volume
            self.status_queue.put(self.player_status, block=False)
