from typing import List


class FileSystem:
    def __init__(self):
        pass

    def ls(self, path: str) -> List[str]:
        pass

    def mkdir(self, path: str) -> None:
        pass

    def addContentToFile(self, file_path: str, content: str) -> None:
        pass

    def readContentFromFile(self, file_path: str) -> str:
        pass
