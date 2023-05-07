from bs4 import BeautifulSoup
from collections import OrderedDict


def main():
    # open and parse html file with playlist exported from Traktor Pro 3
    f = open("solaris.html", "r")
    soup = BeautifulSoup(f.read(), features="html.parser")
    f.close()
    ths = soup.select('th')
    labels = []
    for th in ths:
        h = str(th).replace("<th>", "").replace("</th>", "")
        labels.append(h)
    tds = soup.select('td')
    records = []
    record = []
    counter = 1
    for td in tds:
        h = str(td).replace("<td>", "").replace("</td>", "")
        record.append(h)
        if counter == len(labels):
            counter = 0
            records.append(record)
            record = []
        counter += 1
    all_tracks = []

    # convert into list od dicts
    for r in records:
        l_counter = 0
        track = OrderedDict()
        for entry in r:
            track[labels[l_counter]] = entry
            l_counter += 1
        all_tracks.append(track)

    # create nice tracklist
    tracklist = []
    for track in all_tracks:
        tracklist.append(track["Artist"] + " - " + track["Title"] + "\n")

    # save tracklist to txt file
    t = open("tracklist.txt", "x")
    t.writelines(tracklist)


if __name__ == '__main__':
    main()
