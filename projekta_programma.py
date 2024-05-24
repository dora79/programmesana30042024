def rek_uzturv(m, s, p, o):
    miltu = {'k': 364, 'o': 10, 't': 1, 'og': 76}
    sviests = {'k': 717, 'o': 0.85, 't': 81, 'og': 0.06}
    piens = {'k': 42, 'o': 3.4, 't': 1, 'og': 5}
    olas = {'k': 68, 'o': 6, 't': 5, 'og': 1}

    kcal = (m / 100 * miltu['k'] + s / 100 * sviests['k'] +
            p / 100 * piens['k'] + o * olas['k'])

    olb = (m / 100 * miltu['o'] + s / 100 * sviests['o'] +
           p / 100 * piens['o'] + o * olas['o'])

    tauki = (m / 100 * miltu['t'] + s / 100 * sviests['t'] +
             p / 100 * piens['t'] + o * olas['t'])

    ogļ = (m / 100 * miltu['og'] + s / 100 * sviests['og'] +
           p / 100 * piens['og'] + o * olas['og'])

    print("Kopējās uzturvērtības kūkai:")
    print(f"Kalorijas: {kcal:.2f} kcal")
    print(f"Olbaltumvielas: {olb:.2f} g")
    print(f"Tauki: {tauki:.2f} g")
    print(f"Ogļhidrāti: {ogļ:.2f} g")

def ievad_m(msg, max_value=10000):
    svars = -1
    while svars <= 0 or svars > max_value:
        svars = float(input(msg))
        if svars <= 0:
            print("Lūdzu, ievadiet pozitīvu skaitli.")
        elif svars > max_value:
            print("Lūdzu, ievadiet skaitli mazāku par 10 000 g.")
    return svars

def ievad_piena_m():
    pareizi = False
    while not pareizi:
        izvele = input("Vai vēlaties ievadīt piena svaru gramos (g) vai mililitros (ml)? (ievadiet 'g' vai 'ml')...").strip().lower()
        if izvele == 'g':
            piens = ievad_m("Piena svars (g)... ")
            pareizi = True
        elif izvele == 'ml':
            piens = ievad_m("Piena tilpums (ml)... ")
            pareizi = True
        else:
            print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")
    return piens

def ievad_olu_m():
    pareizi = False
    while not pareizi:
        izvele = input("Vai vēlaties ievadīt olu skaitu (gab) vai svaru gramos (g)? (ievadiet 'gab' vai 'g')... ").strip().lower()
        if izvele == 'gab':
            olas = ievad_m("Olu skaits (gab)... ")
            pareizi = True
        elif izvele == 'g':
            olas = ievad_m("Olu svars (g)... ")
            pareizi = True
        else:
            print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")
    return olas

milti = ievad_m("Miltu svars (g)... ")
sviests = ievad_m("Sviesta svars (g)... ")
piens = ievad_piena_m()
olas = ievad_olu_m()

rek_uzturv(milti, sviests, piens, olas)
