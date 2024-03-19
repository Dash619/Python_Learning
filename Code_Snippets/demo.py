if __name__ == '__main__':
    n = int(input())
    arr = input().split()

    scores = [int(score) for score in arr]
    max_score = max(scores)
    while max_score in scores:
        scores.remove(max_score)
    runner_up_score = max(scores)
    print(runner_up_score)