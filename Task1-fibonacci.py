from functools import cache
from timeit import timeit


@cache
def factorial(n: int) -> int:
    """This function is for calculating n-factorial element

    Args:
        n (int): input, which element you want to calculate

    Returns:
        int: calculated n-factorial element
    """

    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    """
    Main part in which we'll execute our [factorial] function
    and check execution time.
    """
    while True:
        try:
            # define entered number by user
            console_num = int(
                input("Please enter which number you want to calculate: ")
            )
            time_to_run = timeit(lambda n=console_num: factorial(n), number=1)
            print(
                f"We've calculated the [{console_num}] position of Fibonacci\n" +
                f"The result is - {factorial(console_num)}\n" +
                f"Time to calculate the current num is - {'{:.16f}'.format(time_to_run)}"
            )

        except (ValueError, RecursionError) as e:
            print("Something went wrong. See the details below.")
            print(e)


if __name__ == "__main__":
    main()
