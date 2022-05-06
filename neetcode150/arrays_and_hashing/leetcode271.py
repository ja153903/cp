from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = []

        for s in strs:
            encoded.append(f"{len(s)}/{s}")

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded = []
        start = 0

        while start < len(s):
            slash = s.find("/", start)
            # we can assume that this will always exist
            s_len = int(s[start: slash])

            decoded.append(s[slash + 1: slash + 1 + s_len])

            start = slash + 1 + s_len

        return decoded
