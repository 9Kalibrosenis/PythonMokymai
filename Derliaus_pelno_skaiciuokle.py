import requests
azotiniu_trasu_rusys = {
    "1": "Amonio salietra",
    "2": "Amonio sulfatas",
    "3": "Kalcio amonio salietra",
    "4": "Karbamidas"
}
kompleksiniu_trasu_rusys = {
    "1": [0.05, 0.205, 0.36],
    "2": [0.06, 0.18, 0.36],
    "3": [0.10, 0.26, 0.26],
    "4": [0.16, 0.16, 0.16]
}
rajonai = {
    "1": "Vilniaus",
    "2": "Kauno",
    "3": "Klaipedos",
    "4": "Siauliu",
    "5": "Kedainiu",
    "6": "Rokiskio",
    "7": "Alytaus",
    "8": "Marijampoles",
    "9": "Ignalinos",
    "10": "Mazeikiu"
}
kultura = {
    "1": 0.85,
    "2": 0.92,
    "3": 1,
    "4": 0.50
}
veiklioji_medziaga_azotines_trasos = {
    "Amonio salietra": 0.32,
    "Amonio sulfatas": 0.21,
    "Kalcio amonio salietra": 0.27,
    "Karbamidas": 0.46
}
klaida = "Toks pasirinkimas negalimas"
klaida_2 = ",iveskite skaiciu"
azotiniu_trasu_pasirinkimas = "0"
kompleksiniu_trasu_pasirinkimas = "0"
rajono_pasirinkimas = "0"
kulturos_pasirinkimas = "0"
pasirinkta_kultura = []
azotas_is_npk = []
fosforas = []
kalis = []
azotas_is_azotiniu = []

while rajono_pasirinkimas not in rajonai:
    rajono_pasirinkimas = input("Pasirinkite norima rajona: \n1 - Vilniaus;\n2 - Kauno;\n3 - Klaipedos;\n4 - Siauliu;\n5 - Kedainiu;"
"\n6 - Rokiskio;\n7 - Alytaus;\n8 - Marijampoles;\n9 - Ignalinos;\n10 - Mazeikiu: ")
    if rajono_pasirinkimas not in rajonai:
        print(klaida)
        continue
while kulturos_pasirinkimas not in kultura:
    kulturos_pasirinkimas = input("Pasirinkite auginama kultura: 1 - Kvieciai; 2 - Kvietrugiai; 3 - Mieziai; 4 - Rapsai: ")
    if kulturos_pasirinkimas not in kultura:
        print(klaida)
for i in kulturos_pasirinkimas:
    if i == "1":
        pasirinkta_kultura = kultura["1"]
    if i == "2":
        pasirinkta_kultura = kultura["2"]
    if i == "3":
        pasirinkta_kultura = kultura["3"]
    if i == "4":
        pasirinkta_kultura = kultura["4"]
while azotiniu_trasu_pasirinkimas not in azotiniu_trasu_rusys:
    azotiniu_trasu_pasirinkimas = input("Pasirinkite azotiniu trasu rusi: 1 - Amonio salietra; 2 - Amonio sulfatas; 3 - Kalcio amonio salietra; 4 - Karbamidas: ")
    if azotiniu_trasu_pasirinkimas not in azotiniu_trasu_rusys:
        print(klaida)
        continue
    try:
        azotiniu_trasu_kiekis = int(input("Iveskite norima trasu kieki: "))
    except ValueError:
        print(klaida, klaida_2)
        continue
    if azotiniu_trasu_pasirinkimas == "1":
       n_is_salietros = azotiniu_trasu_kiekis * veiklioji_medziaga_azotines_trasos["Amonio salietra"]
       azotas_is_azotiniu.append(n_is_salietros)
    elif azotiniu_trasu_pasirinkimas == "2":
        n_is_sulfato = azotiniu_trasu_kiekis * veiklioji_medziaga_azotines_trasos["Amonio sulfatas"]
        azotas_is_azotiniu.append(n_is_sulfato)
    elif azotiniu_trasu_pasirinkimas == "3":
        n_is_kalcio = azotiniu_trasu_kiekis * veiklioji_medziaga_azotines_trasos["Kalcio amonio salietra"]
        azotas_is_azotiniu.append(n_is_kalcio)
    elif azotiniu_trasu_pasirinkimas == "4":
        n_is_karbamido = azotiniu_trasu_kiekis * veiklioji_medziaga_azotines_trasos["Karbamidas"]
        azotas_is_azotiniu.append(n_is_karbamido)
while kompleksiniu_trasu_pasirinkimas not in kompleksiniu_trasu_rusys:
    kompleksiniu_trasu_pasirinkimas = input("Pasirinkite kompleksiniu trasu rusi: 1 - NPK(5-20.5-36); 2 - NPK(6-18-36); 3 - NPK(10-26-26); 4 - NPK(16-16-16): ")
    if kompleksiniu_trasu_pasirinkimas not in kompleksiniu_trasu_rusys:
        print(klaida)
        continue
    try:
        kompleksiniu_trasu_kiekis = int(input("Iveskite norima trasu kieki: "))
    except ValueError:
        print(klaida, klaida_2)
        continue
def npk_veikli_medziaga (kompleksiniu_trasu_rusys):
    for i in kompleksiniu_trasu_pasirinkimas:
        if i == "1":
            azoto_veikli = kompleksiniu_trasu_rusys["1"][0] * kompleksiniu_trasu_kiekis
            azotas_is_npk.append(int(azoto_veikli))
            fosforo_veikli = kompleksiniu_trasu_rusys["1"][1] * kompleksiniu_trasu_kiekis
            fosforas.append(fosforo_veikli)
            kalio_veikli = kompleksiniu_trasu_rusys["1"][2] * kompleksiniu_trasu_kiekis
            kalis.append(kalio_veikli)
        if i == "2":
            azoto_veikli = kompleksiniu_trasu_rusys["2"][0] * kompleksiniu_trasu_kiekis
            azotas_is_npk.append(int(azoto_veikli))
            fosforo_veikli = kompleksiniu_trasu_rusys["2"][1] * kompleksiniu_trasu_kiekis
            fosforas.append(fosforo_veikli)
            kalio_veikli = kompleksiniu_trasu_rusys["2"][2] * kompleksiniu_trasu_kiekis
            kalis.append(kalio_veikli)
        if i == "3":
            azoto_veikli = kompleksiniu_trasu_rusys["3"][0] * kompleksiniu_trasu_kiekis
            azotas_is_npk.append(int(azoto_veikli))
            fosforo_veikli = kompleksiniu_trasu_rusys["3"][1] * kompleksiniu_trasu_kiekis
            fosforas.append(fosforo_veikli)
            kalio_veikli = kompleksiniu_trasu_rusys["3"][2] * kompleksiniu_trasu_kiekis
            kalis.append(kalio_veikli)
        if i == "4":
            azoto_veikli = kompleksiniu_trasu_rusys["4"][0] * kompleksiniu_trasu_kiekis
            azotas_is_npk.append(int(azoto_veikli))
            fosforo_veikli = kompleksiniu_trasu_rusys["4"][1] * kompleksiniu_trasu_kiekis
            fosforas.append(fosforo_veikli)
            kalio_veikli = kompleksiniu_trasu_rusys["4"][2] * kompleksiniu_trasu_kiekis
            kalis.append(kalio_veikli)
npk_veikli_medziaga(kompleksiniu_trasu_rusys)
def bendras_azotas (azotiniu_trasu_pasirinkimas, azotas_is_npk):
    bendras_azotas = []
    for i in azotiniu_trasu_pasirinkimas:
        if i == "1":
            bendras_azotas.append(azotas_is_azotiniu)
            bendras_azotas.append(azotas_is_npk)
        if i == "2":
            bendras_azotas.append(azotas_is_azotiniu)
            bendras_azotas.append(azotas_is_npk)
        if i == "3":
            bendras_azotas.append(azotas_is_azotiniu)
            bendras_azotas.append(azotas_is_npk)
        if i == "4":
            bendras_azotas.append(azotas_is_azotiniu)
            bendras_azotas.append(azotas_is_npk)
    def bendro_azoto_suma_sk(bendras_azotas):
        global bendro_azoto_suma
        bendro_azoto_suma = 0
        for i in bendras_azotas:
            if (type(i) == type([])):
                bendro_azoto_suma = bendro_azoto_suma + bendro_azoto_suma_sk(i)
            else:
                bendro_azoto_suma = bendro_azoto_suma + i
                return bendro_azoto_suma
    bendro_azoto_suma_sk(bendras_azotas)
bendras_azotas(azotiniu_trasu_pasirinkimas, azotas_is_npk)
bendras_azotas = globals()["bendro_azoto_suma"]
with open("Bonitetiniai_balai.txt", "r") as f:
    a = []
    zodynas = {}
    for i in f.read().replace(",", "").split():
        a.append(i)
    for i in range(0, len(a), 2):
        zodynas[a[i]] = a[i + 1]
for i in rajono_pasirinkimas:
    if i == "1":
        bonitetinis_balas = int(zodynas["Vilniaus"])
    if i == "2":
        bonitetinis_balas = int(zodynas["Kauno"])
    if i == "3":
        bonitetinis_balas = int(zodynas["Klaipedos"])
    if i == "4":
        bonitetinis_balas = int(zodynas["Siauliu"])
    if i == "5":
        bonitetinis_balas = int(zodynas["Kedainiu"])
    if i == "6":
        bonitetinis_balas = int(zodynas["Rokiskio"])
    if i == "7":
        bonitetinis_balas = int(zodynas["Alytaus"])
    if i == "8":
        bonitetinis_balas = int(zodynas["Marijampoles"])
    if i == "9":
        bonitetinis_balas = int(zodynas["Ignalinos"])
    if i == "10":
        bonitetinis_balas = int(zodynas["Mazeikiu"])
def derlius (bendras_azotas, fosforas, kalis, bonitetinis_balas, pasirinkta_kultura):
    derlius = (bendras_azotas + fosforas[0] + kalis[0] + bonitetinis_balas) * pasirinkta_kultura
    return derlius
derliaus_koeficientas = derlius(bendras_azotas, fosforas, kalis, bonitetinis_balas, pasirinkta_kultura)
suapvalintas_derliaus_koeficientas = round(derliaus_koeficientas)
tonos_is_ha = []
if 0 <= suapvalintas_derliaus_koeficientas <= 114:
    tonos_is_ha.append(1)
if 115 <= suapvalintas_derliaus_koeficientas <= 171:
    tonos_is_ha.append(2)
if 172 <= suapvalintas_derliaus_koeficientas <= 227:
    tonos_is_ha.append(3)
if 228 <= suapvalintas_derliaus_koeficientas <= 285:
    tonos_is_ha.append(4)
if 286 <= suapvalintas_derliaus_koeficientas <= 342:
    tonos_is_ha.append(5)
if 343 <= suapvalintas_derliaus_koeficientas <= 399:
    tonos_is_ha.append(6)
if 400 <= suapvalintas_derliaus_koeficientas <= 456:
    tonos_is_ha.append(7)
if 457 <= suapvalintas_derliaus_koeficientas <= 514:
    tonos_is_ha.append(8)
if 515 <= suapvalintas_derliaus_koeficientas <= 570:
    tonos_is_ha.append(9)
if 571 <= suapvalintas_derliaus_koeficientas <= 599:
    tonos_is_ha.append(10)
print(f"Planuojamas derlius {tonos_is_ha} tonos is hektaro")
for i in kulturos_pasirinkimas:
     if i == "1":
        r = requests.get(f"https://commodities-api.com/api/latest?access_key=ivc2t8e6w4672p9k3x5c98mrxs5lk72hna49gl4a2s71oz8ih23u3vpyl915&base=EUR&symbols=WHEAT")
        i = r.json()
        pajamos = []
        data_is_web = i["data"]["rates"]["WHEAT"]
        kvieciu_kaina_realiu_laiku = 1/data_is_web * tonos_is_ha[0]
        print(f"{(round(kvieciu_kaina_realiu_laiku))} Eur/Ha")
     else:
        continue