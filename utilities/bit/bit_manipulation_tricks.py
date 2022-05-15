def clear_all_bits_from_lsb_to_ith_bit(x: int, i: int) -> int:
    """
    Clear all bits from LSB to ith bit

    Logic: To clear all bits from LSB to i-th bit, we have to AND x with mask having LSB to i-th bit 0.
    To obtain such mask, first left shift 1 i times. Now if we minus 1 from that, all the bits
    from 0 to i-1 become 1 and remaining bits become 0. Now we can simply take complement of mask to
    get all first i bits to 0 and remaining to 1.

    :param x:
    :param i:
    :return:
    """
    mask = ~((1 << i + 1) - 1)
    x &= mask

    return x


def clear_all_bits_from_msb_to_ith_bit(x: int, i: int) -> int:
    """
    Clear all bits from MSB to the ith bit

    Logic: To clear all bits from MSB to i-th bit, we have to AND x with mask having MSB to i-th bit 0.
    To obtain such mask, first left shift 1 i times. Now if we minus 1 from that, all the bits
    from 0 to i-1 become 1 and remaining bits become 0.

    :param x:
    :param i:
    :return:
    """
    mask = (1 << i) - 1
    x &= mask

    return x


def divide_by_two(x: int) -> int:
    x >>= 1

    return x


def multiply_by_two(x: int) -> int:
    x <<= 1

    return x


def to_lowercase_eng(ch: str) -> str:
    asc = ord(ch)

    asc |= ord(" ")

    return chr(asc)


def to_uppercase_eng(ch: str) -> str:
    asc = ord(ch)

    asc &= ord("_")

    return chr(asc)


def kernighan(n: int):
    """
     Count set bits in integer

    :return:
    """
    count = 0

    while n:
        # n & (n - 1) unsets the rightmost bit
        n &= n - 1
        count += 1

    return count


def find_log_base2_of_32bit_int(n: int) -> int:
    """
    Find log base 2 of 32 bit integer

    Logic: We right shift x repeatedly until it becomes 0, meanwhile we keep count on the shift operation.
    This count value is the log2(x)

    :param n:
    :return:
    """
    result = 0

    while n:
        result += 1
        n >>= 1

    return result


def is_power_of_2(n: int) -> bool:
    """
    Logic: All the power of 2 have only single bit set e.g. 16 (00010000).
    If we minus 1 from this, all the bits from LSB to set bit get toggled, i.e., 16-1 = 15 (00001111).
    Now if we AND x with (x-1) and the result is 0 then we can say that x is power of 2 otherwise not.
    We have to take extra care when x = 0.

    :param n:
    :return:
    """
    return n and not (n & (n - 1))
