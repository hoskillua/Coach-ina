from pynput import mouse


def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        print('(, {}, {})'.format(x, y))
        # Returning False if you need to stop the program when Left clicked.
        if x > 1500:
            return False


listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()
