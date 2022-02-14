number_of_wagons = int(input())
train_list = [0 for i in range(number_of_wagons)]
command_line = input()
while not command_line == "End":
    command = command_line.split(" ")[0]
    if command == "add":
        add, people = command_line.split(" ")
        train_list[-1] += int(people)
    elif command == "insert":
        insert, index , people = command_line.split(" ")
        train_list[int(index)] += int(people)
    elif command == "leave":
        command, index, people = command_line.split(" ")
        train_list [int(index)] -= int(people)

    command_line = input()

print(train_list)
