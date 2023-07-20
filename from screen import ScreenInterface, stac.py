from python1 import ScreenInterface, stack


def main()
    interface1 = ScreenInterface(title="App Home page")
    interface2 = ScreenInterface(title="Product 1 Page")
    interface3 = ScreenInterface(title="Product 2 Page")

    stack = stack()
    stack.push(interface1)
    stack.push(interface2)
    stack.push(interface3)


    stack.pop()
    stack.pop()


    stack.iterate()

    print("Stack:",vars(stack))

if __name__ == "__main__":
    main()      