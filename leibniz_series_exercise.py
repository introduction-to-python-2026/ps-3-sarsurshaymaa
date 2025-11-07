def approximate_pi(n_terms):
    series_sum = 0.0
    for n in range(n_terms):
        num = (-1) ** n
        denom = (2 * n) + 1
        term = num / denom
        series_sum += term
    approx_pi = 4 * series_sum
    return approx_pi
