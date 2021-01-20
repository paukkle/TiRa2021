def count(n):
    if n <= 3:
        return 0

    def osumat(vap, etais):
        if vap == 0:
            return 2 ** (1 + vap) + etais
        return 2 ** (1 + vap) + etais * 2

    def etaisyydet(kohta, vap):
        et_1 = min([kohta - vap, 2])
        et_2 = min([(n - 1 - vap) - kohta, 2])
        return et_1, et_2

    def kuningatar(n, vap):
        return (n * 2 - 1) + (n - 1) + 2 * vap

    safespotit = 0
    alue = ""
    ruudut = n ** 2

    for rivi in range(n):
        for sarake in range(n):

            osumakohdat = 0

            if (rivi == 0 or rivi == n - 1) or (sarake == 0 or sarake == n - 1):
                vap = 0
                alue = "ur"
            elif (rivi == 1 or rivi == n - 2) or (sarake == 1 or sarake == n - 2):
                vap = 1
                alue = "sr"
            else:
                alue = "muu"
                vap = min([n-rivi - 1, rivi, sarake, n-sarake - 1])

            # Jos ollaan ulkoreunalla
            if alue == "ur":
                if (rivi == 0 or rivi == n - 1):
                    et_v, et_o = etaisyydet(sarake, vap)
                    osumakohdat += osumat(vap, min([et_v, et_o]))

                    
                elif (sarake == 0 or sarake == n - 1):
                    et_y, et_a = etaisyydet(rivi, vap)
                    osumakohdat += osumat(vap, min([et_y, et_a]))

                osumakohdat += kuningatar(n, vap)
             
            # Jos ollaan yksi reuna sisemmällä
            elif alue == "sr":
                if (rivi == 1 or rivi == n - 2):
                    et_v, et_o = etaisyydet(sarake, vap)
                    et_y, et_a = etaisyydet(rivi, 0)
                    if rivi == 1:
                        osumakohdat += osumat(vap, min([et_v, et_o, et_y]))
                    if rivi == n - 2:
                        osumakohdat += osumat(vap, min([et_v, et_o, et_a]))
                elif (sarake == 1 or sarake == n - 2):
                    et_v, et_o = etaisyydet(sarake, 0)
                    et_y, et_a = etaisyydet(rivi, vap)
                    if sarake == 1:
                        osumakohdat += osumat(vap, min([et_y, et_a, et_v]))
                    if sarake == n - 2:
                        osumakohdat += osumat(vap, min([et_y, et_a, et_o]))
                osumakohdat += kuningatar(n, vap)
            # Mikä tahansa muu "reuna"
            elif alue == "muu":
                osumakohdat += 8
                osumakohdat += kuningatar(n, vap)
            safespotit += ruudut - osumakohdat

    return safespotit


if __name__ == "__main__":
    #print(count(3))  # 0
    print(count(4))  # 40
    print(count(5))
    print(count(7))  # 184
