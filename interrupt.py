import threading

interrupt_flag = False  # Flag to indicate interruption


def listen_for_interrupt():
    global interrupt_flag
    while True:
        command = input("Enter 'i' to interrupt response generation and enter a new command: ")
        if command.lower() == 'i':
            print("Interrupting response generation...")
            interrupt_flag = True  # Set interruption flag to True
            break
        else:
            print("Invalid command. Please enter 'i'.")


def start_interrupt():
    command_thread = threading.Thread(target=listen_for_interrupt)
    command_thread.start()
    command_thread.join()  # Wait for the interrupt thread to finish
    print("Response generation interrupted.")
