def general_probability(coins_prob: list[float], events_prob: list[float]) -> float:
    """Function developed ro find the general probability

    Args:
        coins_prob (list[float]): probability of each coin
        events_prob (list[float]): probability of getting current side

    Returns:
        float: probability of getting the current side
    """
    return sum(
        coin_prob * event_prob for coin_prob, event_prob in zip(coins_prob, events_prob)
    )


def refresh_possibs(
    coins_possib: list[float], events_possib: list[float], gen_prob: float
) -> list[float]:
    """List of possibilities to get the current coin next time

    Args:
        coins_possib (list[float]): list of coins possibilities
        events_possib (list[float]): list of getting current side
        gen_prob (float): probability of getting current side

    Returns:
        list[float]: refreshed list of getting current side
    """
    return [
        (coin_possib * event_prob) / gen_prob
        for coin_possib, event_prob in zip(coins_possib, events_possib)
    ]


def calc_possibilities(
    sequence: list[str], coins_quantity: int, general_possibility: dict
) -> list[float]:
    """Get a List of possibilities for getting H side of coin through the several times

    Args:
        sequence (list[str]): Sides coin list for which the possibilities will be calculated.
        coins_quantity (int): Number of coins that we have and can choose
        general_possibility (dict): possibilities for each side of coin

    Returns:
        list[float]: final result of possibilities for [H] side
    """
    H_possibs = []

    coin_possibs = [1 / coins_quantity] * coins_quantity

    for side in sequence:
        H_possibs.append(general_probability(coin_possibs, general_possibility["H"]))
        coin_possibs = refresh_possibs(
            coin_possibs,
            general_possibility[side],
            general_probability(coin_possibs, general_possibility[side]),
        )

    return H_possibs[1:]


def main():
    """Main function"""
    coin_possib_H = [0.1, 0.2, 0.4, 0.8, 0.9]
    general_possibility = {
        "H": coin_possib_H,
        "T": [1 - item for item in coin_possib_H],
    }

    sequence = list("HHHTHTHHH")

    coins_quantity = 5

    print(
        [
            round(elem, 2)
            for elem in calc_possibilities(
                sequence, coins_quantity, general_possibility
            )
        ]
    )


if __name__ == "__main__":
    main()
