import csv


def lire_csv(filepath, delimiter= " ", encoding = "latin-1"):
    with open(filepath, newline='', encoding= encoding) as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return list(reader)

    
def list_of_dicts_to_csv(data, filepath, delimiter=' ', encoding='latin-1'):
    if not data:
        return
    with open(filepath, 'w', newline='', encoding=encoding) as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)
