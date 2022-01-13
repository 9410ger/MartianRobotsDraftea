from sys import stdin

def set_up():
    N = {"R" : "E", "F" : [0,1], "L" : "W"}
    E = {"R" : "S", "F" : [1,0], "L" : "N"}
    S = {"R" : "W", "F" : [0,-1], "L" : "E"}
    W = {"R" : "N", "F" : [-1,0], "L" : "S"}
    movements = {"N" : N, "E" : E, "S" : S, "W" : W}
    lost_positions = set()
    return movements, lost_positions

def robot_moves(matrix_size, initial_position, instructions, movements, lost_positions):
    last_orientation = initial_position[2]
    robot_x_position = int(initial_position[0])
    robot_y_position = int(initial_position[1])
    lost_robot = False
    for instruction in instructions:
        if(not lost_robot):
            if(instruction == "F"):
              robot_x_position += movements[last_orientation][instruction][0]
              robot_y_position += movements[last_orientation][instruction][1]
              if(robot_x_position < 0 or robot_x_position >= matrix_size[0] or robot_y_position < 0 or robot_y_position >= matrix_size[1]):
                  if(not(robot_x_position,robot_y_position) in lost_positions):
                      lost_robot = True
                      lost_positions.add((robot_x_position, robot_y_position))
                  robot_x_position -= movements[last_orientation][instruction][0]
                  robot_y_position -= movements[last_orientation][instruction][1]
                      
            if(instruction == "R" or instruction == "L"):
                last_orientation = movements[last_orientation][instruction]
    robot_x = str(robot_x_position)
    robot_y = str(robot_y_position)
    if(lost_robot):
        print(robot_x+" "+robot_y+" "+last_orientation+" "+"LOST")
    else:
        print(robot_x+" "+robot_y+" "+last_orientation)
    return lost_positions
        


def main():
    movements, lost_positions = set_up()
    matrix_size = [int(x) + 1 for x in stdin.readline().strip().split()]
    all_file = stdin.readlines()
    i = 0
    while(i < len(all_file)):
        initial_position = all_file[i].strip().split(' ')
        i += 1
        instructions = all_file[i].strip()
        i += 2
        lost_positions = robot_moves(matrix_size, initial_position, instructions, movements, lost_positions) 
        

main()
