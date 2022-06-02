#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:34:47 2022

@author: princefaa-ez
"""

import random

def game(play):

    if play == 'Unicorn':
        print('\n''Lets build a Unicorn''\n')
        
        leg = [] # Need 4 legs to complete the set
        eye = [] # Need 2 eyes to complete the set
        
        unicorn = [] # Body parts of Unicorn collected in order of collection, whilst subject to game rules.
        numbers = [] # Dice roll numbers in order of dice collected
        count = 0    # Initial count before the game starts
        
        while len(unicorn) < 7: # When the length of the unicorn list reaches the desired mark (7), then the while loop will end.
            roll = random.randint(1, 8) # Randomly generate a dice number for each roll
            count+=1
            print('The dice rolls number:',roll) # Prints the number of the dice rolled.
      
            if roll != 1 and 'Body' not in unicorn: # Number 1 references the body. If there is no body then no other number will have their part printed
                numbers.append(roll) # Add the rolled number to the numbers list. 
                print('A Body is needed first before any other part')
            else:
                numbers.append(roll) # Add the rolled number to the numbers list
                
                '''' Remainding If statements nested within the first in order to comply with first condition of the body having to be called first'''

                if roll == 1 and 'Body' not in unicorn: # Conditon of the roll equationg to 1 and the string 'Body' isn't in the unicorn list, then the set rule will apply
                    print('Body acquired')
                    unicorn.append('Body')
                    
                if roll == 2 and 'Tail' not in unicorn:
                    if 'Body' not in unicorn:
                        print('A Body is needed first before any other part')
                    else:
                        print('Tail acquired')
                        unicorn.append('Tail')
                
                if roll == 3 and 'Leg' not in unicorn:
                    if 'Body' not in unicorn:
                        print('A Body is needed first before any other part')
                    elif 'Body' in unicorn:
                        leg.append('leg')
                        if len(leg) <= 3:
                            if len(leg) == 1:
                                print('1st leg acquired')
                            elif len(leg) == 2:
                                print('2nd leg acquired')
                            elif len(leg) == 3:
                                print('3rd leg acquired')
                        else:
                            print('All legs acquired')
                            unicorn.append('Leg')
                            
                if roll == 4 and 'Head' not in unicorn:
                    if 'Body' not in unicorn:
                        print('A Body is needed first before any other part')
                    else:
                        print('Head acquired')
                        unicorn.append('Head')
                
                if roll == 5 and 'Eye' not in unicorn:
                    if 'Head' not in unicorn:
                        print('Need a head before eyes')
                    elif 'Head' in unicorn and len(eye) < 2:
                        eye.append('eye')
                        if len(eye) == 1:
                            print('1st Eye acquired')
                        else:
                            print('Both eyes acquired')
                            unicorn.append(('Eye'))
                
                if roll == 6 and 'Mouth' not in unicorn:
                    if 'Head' not in unicorn:
                        print('Need a head before a mouth')
                    else:
                        print('Mouth acquired')
                        unicorn.append('Mouth')
                
                if roll == 7:
                    print("The number '7' isn't callable in this game")
                
                if roll == 8 and 'Horn' not in unicorn:
                    if 'Head' not in unicorn:
                        print('Need a head before a horn')
                    else:
                        print('Horn acquired')
                        unicorn.append('Horn')
            
            print('\n''The dice numbers rolled so far are:',numbers)
            print('\n''This is the body list:',unicorn)
        print('\n''The total count is:',count,'\n')
        print('\n''The length of the "unicorn" list should be 7 to cut off the while loop')
        print('\n''The length of the "unicorn" list is:',len(unicorn))
        print('\n''The length of the dice numbers rolled should be equal to the total count')
        print('\n''The length of the dice numbers rolled is',len(numbers))
        assert len(unicorn) == 7
        
    elif play == 'Pegasus':
        print('\n''Lets build a Pegasus''\n')
        
        leg =  [] # Need 4 legs to complete the set
        eye =  [] # Need 2 eyes to complete the set
        wing = [] # Need 2 wings to complete the set
        
        pegasus = [] # Body parts of Pegasus collected in order of collection, whilst subject to game rules.
        numbers = [] # Dice roll numbers in order of dice collected
        count = 0    # Initial count before the game starts
        
        while len(pegasus) < 7:
            roll = random.randint(1, 8)
            count += 1
            print('The dice rolls number:', roll)
            
            if roll != 1 and 'Body' not in pegasus: 
                numbers.append(roll)
                print('A Body is needed first before any other part')
            else:
                numbers.append(roll)
                
                '''Remainding if statements nested within the first in order to comply with first condition of the body having to be called first'''
                if roll == 1 and 'Body' not in pegasus: 
                    print('Body acquired')
                    pegasus.append('Body')
                    
                if roll == 2 and 'Tail' not in pegasus:
                    if 'Body' not in pegasus:
                        print('A Body is needed first before any other part')
                    else:
                        print('Tail acquired')
                        pegasus.append('Tail')
                
                if roll == 3 and 'Leg' not in pegasus:
                    if 'Body' not in pegasus:
                        print('A Body is needed first before any other part')
                    elif 'Body' in pegasus:
                        leg.append('leg')
                        if len(leg) <= 3:
                            if len(leg) == 1:
                                print('1st leg acquired')
                            elif len(leg) == 2:
                                print('2nd leg acquired')
                            elif len(leg) == 3:
                                print('3rd leg acquired')
                        else:
                            print('All legs acquired')
                            pegasus.append('Leg')
                            
                
                if roll == 4 and 'Head' not in pegasus:
                    if 'Body' not in pegasus:
                        print('A Body is needed first before any other part')
                    else:
                        print('Head acquired')
                        pegasus.append('Head')
                
                if roll == 5 and 'Eye' not in pegasus:
                    if 'Head' not in pegasus:
                        print('Need a head before eyes')
                    elif 'Head' in pegasus and len(eye) < 2:
                        eye.append('eye')
                        if len(eye) == 1:
                            print('1st Eye acquired')
                        else:
                            print('Both eyes acquired')
                            pegasus.append(('Eye'))
                
                if roll == 6 and 'Mouth' not in pegasus:
                    if 'Head' not in pegasus:
                        print('Need a head before a mouth')
                    else:
                        print('Mouth acquired')
                        pegasus.append('Mouth')
                        
                if roll == 7 and 'Wing' not in pegasus:
                    if len(wing) < 2:
                        wing.append('wing')
                        if len(wing) == 1:
                            print('First wing acquired')
                        else:
                            print('Both wings acquired')
                            pegasus.append('Wing')
                
                if roll == 8:
                    print("The number '8' isn't callable in this game")
            
            print('\n''The dice numbers rolled so far are:',numbers)
            print('\n''This is the body list:',pegasus)
        print('\n''The total count is:',count,'\n')
        print('\n''The length of the "pegasus" list should be 7 to cut off the while loop')
        print('\n''The length of the "pegasus" list is:',len(pegasus))
        print('\n''The length of the dice numbers rolled should be equal to the total count')
        print('\n''The length of the dice numbers rolled is',len(numbers))
        assert len(pegasus) == 7
         
    else:
        print('Please input either "Unicorn" or "Pegasus"')
        game(input())
               
print('\n'"Welcome to DICE ROLL!!!!!"'\n''The aim of the game is to build either a Unicorn or a Pegasus in a particular order.''\n''Once the order has been completed, count how many dice rolls it took to complete the game.''\n')
print('There are some rules to the game.''\n''A body must be collected first.''\n''A head must be collected before an Eye, Mouth or Horn (if building a Unicorn)')
print('To play, please type "Unicorn" or "Pegasus".''\n''* Note: The letters are case sensistive')        
game(input())


if __name__ == "__main__":
    game(input())
    print('All good')
    
    
    