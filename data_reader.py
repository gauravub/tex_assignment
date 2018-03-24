from alchemy import Location, db
import csv
from sqlalchemy import exc


with open('/home/gaurav/Documents/texada_data3.csv', newline='') as csv_file:
    data_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    for i, row in enumerate(data_reader):
        if i == 0:
            continue
        print(row)
        # print(', '.join(row))
        row[0] = int(row[0])
        row[3] = float(row[3])
        row[4] = float(row[4])
        row[5] = int(row[5])
        # new_loc = Location(1, 'Cesna 120', '2016-10-12T12:00:00-05:00', 43.2583264, -81.8149807, 500)
        new_loc = Location(*row)
        # mapper = inspect(new_loc)
        try:
            db.session.add(new_loc)
            db.session.commit()
        except exc.IntegrityError as e:
            print("Integrity error:" + e.__str__())
            db.session().rollback()