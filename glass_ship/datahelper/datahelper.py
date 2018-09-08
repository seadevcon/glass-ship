from sqlalchemy import text

def get_number_of_incidents_per_boat(engine):
    sql = text(
        "SELECT Vessel.name, count(Distress.id) FROM Vessel JOIN Distress ON Vessel.name=Distress.ship_name GROUP BY Vessel.name"
    )
    result = engine.execute(sql)
    results = []
    for row in result:
        results.append(row)

    return results

def get_number_reports_per_boat(engine):
    sql = text(
        "SELECT Vessel.name, count(Report.id) FROM Vessel JOIN Report ON Vessel.name=Report.ship_name GROUP BY Vessel.name"
    )
    result = engine.execute(sql)
    results = []
    for row in result:
        print(row)
        results.append(row)

    return results