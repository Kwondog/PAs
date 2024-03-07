# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:52:38 2024

@author: LAKwon
"""
import random as rand
from tabulate import tabulate
import time

def one_dim(steps):
    step_choices = [-1, 1]
    position = 0
    count = 0
    
    for i in range(steps):
        position += rand.choice(step_choices)
        if position == 0:
            count += 1
            break
    position = 0
    return count

def two_dim(steps):
    axes_choices = [-1, 1]
    step_choices = [-1, 1]
    y_position = 0
    x_position = 0
    count = 0
    
    for i in range(steps):
        axes_picker = rand.choice(axes_choices)
        if axes_picker == -1:
            x_position += rand.choice(step_choices)
        elif axes_picker == 1:
            y_position += rand.choice(step_choices)
        if x_position == 0 and y_position == 0:
            count += 1
            break
    x_position = 0
    y_position = 0
    return count

def three_dim(steps):
    axes_choices = [-1, 1, 3]
    step_choices = [-1, 1]
    y_position = 0
    x_position = 0
    z_position = 0
    count = 0
    
    for i in range(steps):
        axes_picker = rand.choice(axes_choices)
        if axes_picker == -1:
            x_position += rand.choice(step_choices)
        elif axes_picker == 1:
            y_position += rand.choice(step_choices)
        elif axes_picker == 3:
            z_position += rand.choice(step_choices)
        if x_position == 0 and y_position == 0 and z_position == 0:
            count += 1
            break
    x_position = 0
    y_position = 0
    z_position = 0
    return count

def main(percent):
    #data dimension lists
    one_dim_steps = ['1D']
    two_dim_steps = ['2D']
    three_dim_steps = ['3D']
    time_steps = ['3D']
    count_list = [20, 200, 2000, 20000, 200000, 2000000]

    
    #runs percent loop 100 times for 1D and 2D
    for i in range(len(count_list)):
        counter1 = 0
        counter2 = 0
        for percent1 in range(percent):
            count1 = one_dim(count_list[i])
            count2 = two_dim(count_list[i])
            if count1 == 1:
                counter1 += 1
            if count2 == 1:
                counter2 += 1
        one_dim_steps.append(counter1)
        two_dim_steps.append(counter2)
        counter1 = 0
        counter2 = 0
        
    #timer for 3D
    for i in range(len(count_list)):
        start_time = time.time()
        counter3 = 0
        for percent1 in range(percent):
            count3 = three_dim(count_list[i])
            if count3 == 1:
                counter3 += 1
        three_dim_steps.append(counter3)
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_steps.append(elapsed_time)
        counter3 = 0
        
    #makes and prints table
    data = [
        one_dim_steps,
        two_dim_steps,
        three_dim_steps
        ]
    
    time_data = [time_steps]
    #table headers
    headers = ["Number of Steps:", "20", "200", "2000", "20000", "200000", "2000000"]
    #makes table
    table = tabulate(data, headers, tablefmt="grid")
    time_table = tabulate(time_data, headers, tablefmt='grid')
    print('Percentage table')
    print(table)
    print("Time table (seconds)")    
    print(time_table)
    
main(100)
