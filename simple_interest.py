def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest.

    Formula: SI = (P * R * T) / 100

    :param principal: Principal amount (float or int)
    :param rate: Rate of interest (annual, in %)
    :param time: Time period (in years)
    :return: Simple interest value
    """
    return (principal * rate * time) / 100


if __name__ == "__main__":
    print("Simple Interest Calculator")

    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (% per annum): "))
        time = float(input("Enter time (in years): "))

        si = calculate_simple_interest(principal, rate, time)
        print(f"\nSimple Interest = {si}")
    except ValueError:
        print("⚠️ Please enter valid numeric values.")
