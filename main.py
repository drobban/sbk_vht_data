bhk_name_list = ['BHK', 'BK', 'hundklubb', 'ungdom']

def line_handle(line):
    data = line.split(",")
    if len(data) == 27:
        _, datum, _q, an_klubb, _plats, _plats_a, sport, gren, _gren, _startande, start, struken, _strukena, _t_id, _status, _status_a, _klubb_a, _ort, _ort_a, regnr, namn, ras, points, godkand, _, _, _ = data

        return sport, an_klubb, gren, start, regnr, struken
    return "", "", "", "", "", ""
           

def n_startande(q_sport):
    with open("input_data/2024_test.csv") as fp:

        stats = {}
        for line in fp.readlines():
            sport, an_klubb, gren, startande, regnr, struken = line_handle(line)

            if q_sport in sport and startande == "Ja":
                if gren in stats:
                    stats[gren] += 1
                else:
                    stats[gren] = 1

        for gren, antal in stats.items():
            print(f"{gren} : {antal}")

def n_bhk_startande(q_sport):
    with open("input_data/2024_test.csv") as fp:

        stats = {}
        for line in fp.readlines():
            sport, an_klubb, gren, startande, regnr, struken = line_handle(line)

            # To group by rasklubb or kennelklubb
            if True in [nl in an_klubb for nl in bhk_name_list]:
                bhk_club = "lokalklubb"
            else:
                bhk_club = "rasklubb"

            if q_sport in sport and startande == "Ja":
                if bhk_club in stats:
                    if gren in stats[bhk_club]:
                        stats[bhk_club][gren] += 1
                    else:
                        stats[bhk_club][gren] = 1
                else:
                    stats[bhk_club] = {}
                    if gren in stats[bhk_club]:
                        stats[bhk_club][gren] += 1
                    else:
                        stats[bhk_club][gren] = 1

        for bhk_club, gren_stats in stats.items():
            print(f"{bhk_club}")
            for gren, antal in gren_stats.items():
                print(f"{gren} : {antal}")

def n_individer(q_sport):
    with open("input_data/2024_test.csv") as fp:

        stats = {}
        for line in fp.readlines():
            sport, an_klubb, gren, startande, regnr, struken = line_handle(line)

            if q_sport in sport and startande == "Ja":
                if gren in stats:
                    stats[gren].add(regnr)
                else:
                    stats[gren] = set([regnr])
     
        for gren, individer in stats.items():
            print(f"{gren} : {len(individer)}")

def n_bhk_individer(q_sport):
    with open("input_data/2024_test.csv") as fp:

        stats = {}
        for line in fp.readlines():
            sport, an_klubb, gren, startande, regnr, struken = line_handle(line)

            # To group by rasklubb or kennelklubb
            if True in [nl in an_klubb for nl in bhk_name_list]:
                bhk_club = "lokalklubb"
            else:
                bhk_club = "rasklubb"

            if q_sport in sport and startande == "Ja":
                if bhk_club in stats:
                    if gren in stats[bhk_club]:
                        stats[bhk_club][gren].add(regnr)
                    else:
                        stats[bhk_club][gren] = set([regnr])
                else:
                    stats[bhk_club] = {}
                    if gren in stats[bhk_club]:
                        stats[bhk_club][gren].add(regnr)
                    else:
                        stats[bhk_club][gren] = set([regnr])

        for bhk_club, gren_stats in stats.items():
            print(f"{bhk_club}")
            for gren, individer in gren_stats.items():
                print(f"{gren} : {len(individer)}")


#print("Startande")
#n_startande("Bruks")
#n_startande("IGP")
#n_startande("Mondioring")
#n_startande("IPO-R")
#n_startande("Lydnad")
#n_startande("Rallylydnad")

# n_bhk_startande("Bruks")
# n_bhk_startande("IGP")
# n_bhk_startande("Mondioring")
# n_bhk_startande("IPO-R")
# n_bhk_startande("Lydnad")
# n_bhk_startande("Rallylydnad")


print("Individer")
#n_individer("Bruks")
#n_individer("IGP")
#n_individer("Mondioring")
#n_individer("IPO-R")
#n_individer("Lydnad")
#n_individer("Rallylydnad")

# n_bhk_individer("Bruks")
# n_bhk_individer("IGP")
# n_bhk_individer("Mondioring")
# n_bhk_individer("IPO-R")
n_bhk_individer("Lydnad")
#n_bhk_individer("Rallylydnad")


