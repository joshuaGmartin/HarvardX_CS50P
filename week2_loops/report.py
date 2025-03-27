def main():
    # spacecraft = {"V1": "163", "V2": "136", "P10": "80 AU", "NH": "58", "P11": "44 AU"}

    # spacecraft = {"name": "V1", "distance": 163}

    # spacecraft = {"name": "JWST"}
    # # spacecraft["distance"] = 0.01

    spacecraft = {"name": "JWST"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})

    print(create_report(spacecraft))


def create_report(spacecraft):
    # return f"""
    # ========= REPORT =========

    # Name: {spacecraft["name"]}
    # Distance: {spacecraft["distance"]} AU

    # ==========================
    # """
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU 
    Orbit: {spacecraft.get("orbit", "Unknown")} 

    ==========================
    """


main()
