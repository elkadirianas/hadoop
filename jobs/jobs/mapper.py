#!/usr/bin/env python3
import sys

genres = ["unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime", 
          "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
          "Romance", "Sci-Fi", "Thriller", "War", "Western"]

for line in sys.stdin:
    parts = line.strip().split('|')
    if len(parts) < 24:
        continue  # Malformed line
    for i in range(19):  # Genre columns start from index 5 to 23
        if parts[5 + i] == '1':
            print("{}\t1".format(genres[i]))


