from rich.traceback import install
install(show_locals=True)

def will_it_run():
    # Get a slice of this!

    x = list(range(10))

    assert x[0] == 0

    assert x[-100:100] == list(range(10))

    y = list(range(10))
    y[1::2] = '#####'
    assert y == [0, '#', 2, '#', 4, '#', 6, '#', 8, '#']

    y[1::2] = 'xxxx'
    assert y == [0, 'x', 2, 'x', 4, 'x', 6, 'x', 8, 'x']

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()