#!/usr/bin/env python
# Name: Sebastiaan Schneider
# Student number: 10554769

import csv
import json

movies = []
jsondict = {}


def preprocessing():
    with open("Section6-Homework-Data.csv", 'r') as reader:
        data = csv.DictReader(reader)
        for row in data:
            movie = row["Movie Title"]
            studio = row["Studio"]
            release = row["Release Date"]
            genre = row["Genre"]
            runtime = row["Runtime (min)"]
            budget = row["Budget ($mill)"]
            gross = row["Adjusted Gross ($mill)"]
            rating = row["IMDb Rating"]
            list = [movie, studio, release, genre, runtime, budget, gross, rating]
            movies.append(list)


def filter_write():
    with open("data.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Studio", "Release Date", "Genre", "Runtime" "Budget", "Gross", "IMDb Rating"])
        for movie in movies:
            writer.writerow(movie)


def json_write():
    for film in movies:
        jsondict[film[0]] = {"Studio": [film[1]], "Release Date": [film[2]],
                          "Genre": [film[3]], "Runtime": [film[4]],
                          "Budget": [film[5]], "Gross": [film[6]],
                          "IMDb Rating": [film[7]]}

    with open("data.json", 'w') as output:
        json.dump(jsondict, output)


    # df = pd.DataFrame(pd.read_csv("data.csv")).sort_values(by=["Studio", "Release Date"])
    # print(df)


    # print(df["Studio"] for df["Studio"] == "WB")
    # df.plot(df["Studio"], df["Gross"])
    # print(sort)
    # plt.bar(x=df["Studio"], height=df["Gross"])
    # plt.show()
# studio = df["Studio"]
# print(dates)
# gross = df["Adjusted Gross ($mill)"]
# print(gross)
# plt.bar(x=studio, height=gross)
# plt.show()


if __name__ == "__main__":
    preprocessing()
    filter_write()
    json_write()