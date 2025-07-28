import csv
import matplotlib.pyplot as plt

genres = []
counts = []

with open("genre_count.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        genres.append(row["Genre"])
        counts.append(int(row["TotalCount"]))

# Remove garbage genre (if any)
if "genres" in genres:
    i = genres.index("genres")
    genres.pop(i)
    counts.pop(i)

plt.figure(figsize=(14, 7))
plt.bar(genres, counts, color="skyblue")
plt.xlabel("Genre")
plt.ylabel("Number of Movies")
plt.title("Movie Count per Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.savefig("genre_plot.png")
plt.show()

