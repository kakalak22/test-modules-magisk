from pathlib import Path
from typing import Optional, List

from ..model import (
    ConfigJson,
    TrackJson,
    OnlineModule,
    UpdateJson,
    VersionItem
)
from ..track import LocalTracks
from ..utils import Log


class Check:
    _log: Log

    _local_folder: Path
    _modules_folder: Path
    _config: ConfigJson
    _tracks: LocalTracks

    def __init__(self, root_folder: Path, config: ConfigJson): ...
    def _get_file_url(self, module_id: str, file: Path) -> str: ...
    def _get_tracks(self, module_ids: Optional[List[str]], new: bool) -> List[TrackJson]: ...
    def _check_folder(self, track: TrackJson, target_id: str) -> bool: ...
    def _get_new_version_item(self, track: TrackJson, item: VersionItem) -> Optional[VersionItem]: ...
    def _check_update_json(self, track: TrackJson, update_json: UpdateJson, check_id: bool)-> bool: ...
    def get_online_module(self, module_id: str, zip_file: Path) -> Optional[OnlineModule]: ...
    def url(self, module_ids: Optional[List[str]] = ..., new: bool = ...): ...
    def ids(self, module_ids: Optional[List[str]] = ..., new: bool = ...): ...
    def old(self, module_ids: Optional[List[str]] = ..., new: bool = ...): ...