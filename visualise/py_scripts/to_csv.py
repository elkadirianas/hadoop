import csv

with open("genre_count.txt", "r") as infile, open("genre_count.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Genre", "TotalCount"])

    for line in infile:
        parts = line.strip().split("\t")
        if len(parts) == 3:
            genre, _, total = parts
            writer.writerow([genre, total])

