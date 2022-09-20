from rich.traceback import install

install(show_locals=True)


def will_it_run():
    x = 5

    class SomeClass:
        x = 17
        y = (x for i in range(10))

    assert list(SomeClass.y)[0] == 5

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
