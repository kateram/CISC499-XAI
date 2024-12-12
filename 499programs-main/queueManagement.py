def queue_management(commands):
    queue = []
    outputs = []

    for inp in commands:
        if inp == 'x':
            outputs.append("Exiting. Remaining names in the queue:")
            outputs.extend(queue)
            break

        if inp == 's':
            outputs.append(f"The size of the queue is: {len(queue)}")
            continue

        if inp == 'n':
            if len(queue) > 0:
                outputs.append(f"Next is: {queue.pop(0)}")
            else:
                outputs.append("The queue is empty")
            continue
        queue.append(inp)
        outputs.append(f"Added '{inp}' to the queue")
    
    return outputs

if __name__ == "__main__":
    commands = ["Alice", "Bob", "s", "n", "n", "s", "x"]
    results = queue_management(commands)
    for result in results:
        print(result)