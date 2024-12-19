from csv import reader

import orjson

data: list[dict[str, str | float]] = []


with open("data.csv", "r", encoding="utf-8") as file:
    csv = reader(file)

    # skip the first row
    next(csv)

    for row in csv:
        data.append(
            {
                "country_code": row[0],
                "region_name": row[1],
                "iata": row[2],
                "icao": row[3],
                "airport": row[4],
                "latitude": float(row[5]),
                "longitude": float(row[6]),
            }
        )

with open("data.json", "wb") as file:
    file.write(orjson.dumps(data))
