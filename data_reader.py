from alchemy import Location, db
import csv
from sqlalchemy import exc


def read_data_from_file(filename):
    with open(filename, newline='') as csv_file:
        data_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        for i, row in enumerate(data_reader):
            if i == 0:
                continue
            row[0] = int(row[0])
            row[3] = float(row[3])
            row[4] = float(row[4])
            row[5] = int(row[5])
            new_loc = Location(*row)
            try:
                db.session.add(new_loc)
            except exc.IntegrityError as e:
                print("Integrity error:" + e.__str__())
                db.session().rollback()
            db.session.commit()


if __name__ == '__main__':
    read_data_from_file('data/texada_data3.csv')