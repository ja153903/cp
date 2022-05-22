from typing import List


MODULO_RES = 10**9 + 7


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # TLE
        cache = {}

        result = 0
        for i in range(len(strength)):
            single_repr = f"min([{strength[i]}]) * sum([{strength[i]})"
            if single_repr not in cache:
                product = strength[i] ** 2
                cache[single_repr] = product

            result += cache[single_repr]

            for j in range(i + 1, len(strength)):
                slce = strength[i : j + 1]
                rpr = f"min({slce}) * sum({slce})"

                if rpr not in cache:
                    product = min(slce) * sum(slce)
                    cache[rpr] = product

                result += cache[rpr]

        return result % MODULO_RES
