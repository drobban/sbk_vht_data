

def line_handle(line):
    data = line.split(",")
    if len(data) == 27:
        _, datum, _q, _klubb, _plats, _plats_a, sport, gren, _gren, _startande, start, struken, _strukena, _t_id, _status, _status_a, _klubb_a, _ort, _ort_a, regnr, namn, ras, points, godkand, _, _, _ = data

        return sport, gren, start, regnr, struken
    return "", "", "", "", ""
           

# Bruks
def n_startande(q_sport):
    with open("input_data/2024_test.csv") as fp:

        stats = {}
        for line in fp.readlines():
            sport, gren, startande, regnr, struken = line_handle(line)

            if q_sport in sport and startande == "Ja":
                if gren in stats:
                    stats[gren] += 1
                else:
                    stats[gren] = 1

        for gren, antal in stats.items():
            print(f"{gren} : {antal}")


# Bruks
def n_individer(q_sport):
    with open("input_data/2024_test.csv") as fp:

        stats = {}
        for line in fp.readlines():
            sport, gren, startande, regnr, struken = line_handle(line)

            if q_sport in sport and startande == "Ja":
                if gren in stats:
                    stats[gren].add(regnr)
                else:
                    stats[gren] = set([regnr])
     
        for gren, individer in stats.items():
            print(f"{gren} : {len(individer)}")


print("Startande")
#n_startande("Bruks")
#n_startande("IGP")
#n_startande("Mondioring")
#n_startande("IPO-R")
#n_startande("Lydnad")
n_startande("Rallylydnad")
print("Individer")
#n_individer("Bruks")
#n_individer("IGP")
#n_individer("Mondioring")
#n_individer("IPO-R")
n_individer("Rallylydnad")
