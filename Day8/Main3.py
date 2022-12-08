def main():
    p1 = p2 = 0
    trees = []

    with open('C:/Users/Kyleq/OneDrive/src/AOC2022/Day8/test.txt') as f:
        for line in f:
            trees.append([int(t) for t in line.strip()])
        print(trees)
        
    for i, row in enumerate(trees):
        for j, height in enumerate(row):
            score = 1
            isVisible = False
            treelines = [
                row[:j][::-1],
                row[j + 1 :],
                [r[j] for r in trees[:i]][::-1],
                [r[j] for r in trees[i + 1 :]],
            ]

            for treeline in treelines:
                for dist, h in enumerate(treeline, 1):
                    if h >= height:
                        score *= dist
                        break
                else:
                    isVisible = True
                    score *= max(1, len(treeline))

            p1 += int(isVisible)
            p2 = max(p2, score)

    print(f"p1: {p1}, p2: {p2}")


if __name__ == "__main__":
    main()