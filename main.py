def scoreboard(who_ate_what):
    points = {
        "chickenwings": 5,
        "hamburgers": 3,
        "hotdogs": 2
    }

    results = []

    for participant in who_ate_what:
        score = (participant.get("chickenwings", 0) * points["chickenwings"] +
                 participant.get("hamburgers", 0) * points["hamburgers"] +
                 participant.get("hotdogs", 0) * points["hotdogs"])
        results.append({"name": participant["name"], "score": score})

    results.sort(key=lambda x: (-x["score"], x["name"]))

    return results