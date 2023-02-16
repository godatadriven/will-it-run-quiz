from rich.traceback import install

install(show_locals=True)

def hello(name):
    return "hello {name}!"

def will_it_run():
    output = hello("Krzysztof")
    expected = "hello Krzysztof!"
    assert output == expected

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
