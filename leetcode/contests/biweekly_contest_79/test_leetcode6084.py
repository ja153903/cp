import pytest

from .leetcode6084 import Solution

solution = Solution()


@pytest.mark.parametrize(
    "messages,senders,expected",
    [
        (
            [
                "tP x M VC h lmD",
                "D X XF w V",
                "sh m Pgl",
                "pN pa",
                "C SL m G Pn v",
                "K z UL B W ee",
                "Yf yo n V U Za f np",
                "j J sk f qr e v t",
                "L Q cJ c J Z jp E",
                "Be a aO",
                "nI c Gb k Y C QS N",
                "Yi Bts",
                "gp No g s VR",
                "py A S sNf",
                "ZS H Bi De dj dsh",
                "ep MA KI Q Ou",
            ],
            [
                "OXlq",
                "IFGaW",
                "XQPeWJRszU",
                "Gb",
                "HArIr",
                "Gb",
                "FnZd",
                "FnZd",
                "HArIr",
                "OXlq",
                "IFGaW",
                "XQPeWJRszU",
                "EMoUs",
                "Gb",
                "EMoUs",
                "EMoUs",
            ],
            "FnZd",
        )
    ],
)
def test_largest_word_count(messages, senders, expected):
    assert solution.largestWordCount(messages, senders) == expected
