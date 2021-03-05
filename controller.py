import json, os, sys, pygame, time 


pygame.init()

joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()
    
    
with open(os.path.join("ps4_keys.json"), 'r+') as file:
    button_keys = json.load(file)
    
button_keys_list = list(button_keys)
    
# 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
# 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
analog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1 }


joysticks[0].get_numbuttons()
joysticks[0].get_numhats()

instructions = {
    'turn_in_place' : False,
    'driving_mode' : 0,
    'steering_angle' : 0.0,
    'velocity' : 0.0,
    'running' : True
}

run = True

while run:
    outfile = open("instructions.json", "w")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            pass
        
        
        # HANDLES BUTTON PRESSES
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == button_keys["share"]:
                run = False
                print("end")
        
            elif event.button == button_keys["PS"]:
                print("turn in place")
            elif event.button == button_keys["touchpad"]:
                print("switch driving mode")
            else:
                print(button_keys_list[event.button])

            
        #HANDLES ANALOG INPUTS
        if event.type == pygame.JOYAXISMOTION:
            analog_keys[event.axis] = event.value
            #print(analog_keys)
            
            # Horizontal Analog
            if abs(analog_keys[0]) > .05:
                turn_degree = round(-30 * analog_keys[0], 1)
                instructions['steering_angle'] = turn_degree
                #if analog_keys[0] < -.075:
                    #print("turn left ", turn_degree, " degrees")
                #elif analog_keys[0] > .075:
                    #print("turn right ", abs(turn_degree), " degrees")
                #else:
                    #print("straight")
                    
            # Vertical Analog
            if abs(analog_keys[1]) > .4:
                if analog_keys[1] < -.7:
                    print("speed up")
                elif analog_keys[1] > .7:
                    print("slow down")
                else:
                    print("stop accel")
                print() 

        print(instructions['steering_angle'])
        json_object = json.dumps(instructions, indent = 5) 
                
        outfile.write(json_object) 

    outfile.close()