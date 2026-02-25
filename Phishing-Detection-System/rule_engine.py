def rule_based_check(url):
    score = 0

    if len(url) > 75:
        score += 1

    if "@" in url:
        score += 1

    if url.count('.') > 3:
        score += 1

    if not url.startswith("https"):
        score += 1

    keywords = ["login", "verify", "secure", "update"]
    if any(word in url.lower() for word in keywords):
        score += 1

    return score
