def tournamentWinner(competitions, results):
    # Write your code here.
    out = ""
    n = len(results)

    for i in range(0,n):
        k = results[i]
        print(competitions[k])
        

    return out




competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

results = [0, 0, 1]

tournamentWinner(competitions, results)