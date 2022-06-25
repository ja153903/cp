from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict, List


@dataclass
class File:
    filename: str
    content: str


@dataclass
class Directory:
    is_dir: bool = False
    files: DefaultDict[str, File] = field(default_factory=defaultdict)
    directories: DefaultDict[str, "Directory"] = field(default_factory=defaultdict)


class FileSystem:
    def __init__(self):
        self.root = Directory(is_dir=True)

    def ls(self, path: str) -> List[str]:
        _dirs = self._parse_path(path)
        current = self.root
        if _dirs:
            last = _dirs[-1]
            _dirs = _dirs[:-1]

            for _dir in _dirs:
                if _dir not in current.directories:
                    return []

                current = current.directories[_dir]

            if last in current.files:
                return [current.files[last].filename]

            current = current.directories.get(last)
            if not current:
                return []

        files = list(current.files.keys())
        dirs = list(current.directories.keys())

        return sorted([*files, *dirs])

    def mkdir(self, path: str) -> None:
        _dirs = self._parse_path(path)
        current = self.root
        for _dir in _dirs:
            if _dir not in current.directories:
                current.directories[_dir] = Directory()
            current = current.directories[_dir]

        current.is_dir = True

    def _parse_path(self, path: str) -> List[str]:
        _dirs = [_dir for _dir in path.split("/") if _dir]
        return _dirs

    def addContentToFile(self, file_path: str, content: str) -> None:
        _dirs = self._parse_path(file_path)
        filename = _dirs[-1]
        _dirs = _dirs[:-1]

        current = self.root

        for _dir in _dirs:
            if _dir not in current.directories:
                current.directories[_dir] = Directory()
            current = current.directories[_dir]

        current.is_dir = True
        if filename in current.files:
            current.files[filename].content += content
        else:
            current.files[filename] = File(filename=filename, content=content)

    def readContentFromFile(self, file_path: str) -> str:
        _dirs = self._parse_path(file_path)
        filename = _dirs[-1]
        _dirs = _dirs[:-1]

        current = self.root

        for _dir in _dirs:
            if _dir not in current.directories:
                return ""
            current = current.directories[_dir]

        if filename not in current.files:
            return ""

        return current.files[filename].content
