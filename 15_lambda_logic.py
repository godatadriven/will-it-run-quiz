from rich.traceback import install

install(show_locals=True)

def will_it_run():
    def raise_to_power(a, pow):
        return a**pow

    powers_to_execute = [
        lambda number: raise_to_power(number, power) for power in [1, 2, 3]
    ]

    powers_of_2 = [execute_power(2) for execute_power in powers_to_execute]

    assert powers_of_2 == [2,4,8]

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")

if __name__ == "__main__":
    will_it_run()
