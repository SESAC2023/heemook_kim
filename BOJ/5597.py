# BOJ 5597번
total = [_ for _ in range(1, 31)]
subed = [int(input()) for _ in range(28)]

[print(_) for _ in total if _ not in subed]
