#Gerremy Ferguson

# originals --------------------------------
everything = []
pattern_template = []
sequence_of_numbers = []
player_card = []

# later additions ---------------------------------------
start_of_player_card = len(everything) - 25
copy_of_start_of_player_card = start_of_player_card
sequence_of_numbers_start = 25
sequence_of_numbers_counter = 25
player_marked_card = []
last_number_is_in_bingo = False
last_number_is_in_bingo_90 = False
last_number_is_in_bingo_180 = False
last_number_is_in_bingo_270 = False
pattern_template_copy = []
pattern_template_90 = []
pattern_template_180 = []
pattern_template_270 = []

#------------------------------------------------------------------------------------

def read_input():
    global everything
    global sequence_of_numbers_start
    global pattern_template
    global copy_of_start_of_player_card
    global player_card
    global sequence_of_numbers
    global sequence_of_numbers_counter
    global start_of_player_card

    all_input = []
    for i in range (13):
        all_input += input().split()
    everything = list(map(int, all_input))
    #now we have a scanner. All of the input should be read into everything
    
    for i in range (25):
        pattern_template.append(everything[i])
    #now we have the pattern template in a row of 25 integers
    
    for i in range (25):
        player_card.append(everything[copy_of_start_of_player_card])
        copy_of_start_of_player_card += 1
    #now we have the player card in a row of 25 integers
    
    holder = len(everything) - 50
    for i in range (holder):
        sequence_of_numbers.append(everything[sequence_of_numbers_counter])  #ERROR HERE
        sequence_of_numbers_counter += 1
    #we should now have the sequence of numbers called stored in an array
    
#---------------------------------------------------------------------------------------------------------------------

def is_it_crazy (lst):
    crazy_counter = 0
    for i in range (len(lst)):
        if lst[i] == 4:
            crazy_counter += 1
    
    if (crazy_counter > 0):
        return True
    else:
        return False

#---------------------------------------------------------------------------------------------------------------------

def marker():
    
    global player_marked_card
    global start_of_player_card
    global sequence_of_numbers_start
    global player_card
    global sequence_of_numbers
    global pattern_template
    global everything
    holder = len(everything) - 50
    
    for i in range (25):
        player_marked_card.append(0)
    
    marker_counter = 0
    sequence_marker_counter = 0
    
    for sequence_marker_counter in range (holder):
        for marker_counter in range (25):
            if player_card[marker_counter] == sequence_of_numbers[sequence_marker_counter]:
                if is_it_crazy(pattern_template) == True:
                    player_marked_card[marker_counter] = 4
                else:
                    player_marked_card[marker_counter] = 1
            marker_counter += 1
        marker_counter = 0
        sequence_marker_counter += 1

    if is_it_crazy(pattern_template) == True:
        player_marked_card[12] = 4
    else:
        player_marked_card[12] = 1

#---------------------------------------------------------------------------------------------------------------------

def rotation_checker ():
    
    global pattern_template
    global pattern_template_90
    global pattern_template_180
    global pattern_template_270
    
    if (is_it_crazy(pattern_template) == True):
        for i in range (25):
            pattern_template_90.append(0)
            pattern_template_180.append(0)
            pattern_template_270.append(0)

        for i in range (25):
            if i == 0:
                pattern_template_90[4] = pattern_template[0]
            if i == 1:
                pattern_template_90[9] = pattern_template[1]
            if i == 2:
                pattern_template_90[14] = pattern_template[2]
            if i == 3:
                pattern_template_90[19] = pattern_template[3]
            if i == 4:
                pattern_template_90[24] = pattern_template[4]
            if i == 5:
                pattern_template_90[3] = pattern_template[5]
            if i == 6:
                pattern_template_90[8] = pattern_template[6]
            if i == 7:
                pattern_template_90[13] = pattern_template[7]
            if i == 8:
                pattern_template_90[18] = pattern_template[8]
            if i == 9:
                pattern_template_90[23] = pattern_template[9]
            if i == 10:
                pattern_template_90[2] = pattern_template[10]
            if i == 11:
                pattern_template_90[7] = pattern_template[11]
            if i == 12:
                pattern_template_90[12] = pattern_template[12]
            if i == 13:
                pattern_template_90[7] = pattern_template[13]
            if i == 14:
                pattern_template_90[22] = pattern_template[14]
            if i == 15:
                pattern_template_90[1] = pattern_template[15]
            if i == 16:
                pattern_template_90[6] = pattern_template[16]
            if i == 17:
                pattern_template_90[11] = pattern_template[17]
            if i == 18:
                pattern_template_90[16] = pattern_template[18]
            if i == 19:
                pattern_template_90[21] = pattern_template[19]
            if i == 20:
                pattern_template_90[0] = pattern_template[20]
            if i == 21:
                pattern_template_90[5] = pattern_template[21]
            if i == 22:
                pattern_template_90[10] = pattern_template[22]
            if i == 23:
                pattern_template_90[15] = pattern_template[23]
            if i == 24:
                pattern_template_90[20] = pattern_template[24]
        
        for i in range (25):
            if i == 0:
                pattern_template_180[4] = pattern_template_90[0]
            if i == 1:
                pattern_template_180[9] = pattern_template_90[1]
            if i == 2:
                pattern_template_180[14] = pattern_template_90[2]
            if i == 3:
                pattern_template_180[19] = pattern_template_90[3]
            if i == 4:
                pattern_template_180[24] = pattern_template_90[4]
            if i == 5:
                pattern_template_180[3] = pattern_template_90[5]
            if i == 6:
                pattern_template_180[8] = pattern_template_90[6]
            if i == 7:
                pattern_template_180[13] = pattern_template_90[7]
            if i == 8:
                pattern_template_180[18] = pattern_template_90[8]
            if i == 9:
                pattern_template_180[23] = pattern_template_90[9]
            if i == 10:
                pattern_template_180[2] = pattern_template_90[10]
            if i == 11:
                pattern_template_180[7] = pattern_template_90[11]
            if i == 12:
                pattern_template_180[12] = pattern_template_90[12]
            if i == 13:
                pattern_template_180[7] = pattern_template_90[13]
            if i == 14:
                pattern_template_180[22] = pattern_template_90[14]
            if i == 15:
                pattern_template_180[1] = pattern_template_90[15]
            if i == 16:
                pattern_template_180[6] = pattern_template_90[16]
            if i == 17:
                pattern_template_180[11] = pattern_template_90[17]
            if i == 18:
                pattern_template_180[16] = pattern_template_90[18]
            if i == 19:
                pattern_template_180[21] = pattern_template_90[19]
            if i == 20:
                pattern_template_180[0] = pattern_template_90[20]
            if i == 21:
                pattern_template_180[5] = pattern_template_90[21]
            if i == 22:
                pattern_template_180[10] = pattern_template_90[22]
            if i == 23:
                pattern_template_180[15] = pattern_template_90[23]
            if i == 24:
                pattern_template_180[20] = pattern_template_90[24]
        
        for i in range (25):
            if i == 0:
                pattern_template_270[4] = pattern_template_180[0]
            if i == 1:
                pattern_template_270[9] = pattern_template_180[1]
            if i == 2:
                pattern_template_270[14] = pattern_template_180[2]
            if i == 3:
                pattern_template_270[19] = pattern_template_180[3]
            if i == 4:
                pattern_template_270[24] = pattern_template_180[4]
            if i == 5:
                pattern_template_270[3] = pattern_template_180[5]
            if i == 6:
                pattern_template_270[8] = pattern_template_180[6]
            if i == 7:
                pattern_template_270[13] = pattern_template_180[7]
            if i == 8:
                pattern_template_270[18] = pattern_template_180[8]
            if i == 9:
                pattern_template_270[23] = pattern_template_180[9]
            if i == 10:
                pattern_template_270[2] = pattern_template_180[10]
            if i == 11:
                pattern_template_270[7] = pattern_template_180[11]
            if i == 12:
                pattern_template_270[12] = pattern_template_180[12]
            if i == 13:
                pattern_template_270[7] = pattern_template_180[13]
            if i == 14:
                pattern_template_270[22] = pattern_template_180[14]
            if i == 15:
                pattern_template_270[1] = pattern_template_180[15]
            if i == 16:
                pattern_template_270[6] = pattern_template_180[16]
            if i == 17:
                pattern_template_270[11] = pattern_template_180[17]
            if i == 18:
                pattern_template_270[16] = pattern_template_180[18]
            if i == 19:
                pattern_template_270[21] = pattern_template_180[19]
            if i == 20:
                pattern_template_270[0] = pattern_template_180[20]
            if i == 21:
                pattern_template_270[5] = pattern_template_180[21]
            if i == 22:
                pattern_template_270[10] = pattern_template_180[22]
            if i == 23:
                pattern_template_270[15] = pattern_template_180[23]
            if i == 24:
                pattern_template_270[20] = pattern_template_180[24]
            
#checks to see if you need to rotate the array, and if so, rotates array passed as the parameter

#---------------------------------------------------------------------------------------------------------------------

def is_it_a_winner ():
    
    global last_number_is_in_bingo
    global last_number_is_in_bingo_90
    global last_number_is_in_bingo_180
    global last_number_is_in_bingo_270
    global player_card
    global pattern_template
    global player_marked_card
    global pattern_template_90
    global pattern_template_180
    global pattern_template_270
    
    counter_one = 0
    counter_two = 0
    counter_two_90 = 0
    counter_two_180 = 0
    counter_two_270 = 0
    sequence_of_numbers_limit = len(sequence_of_numbers) - 1
    sequence_of_numbers_last_number = sequence_of_numbers[sequence_of_numbers_limit]
    
    #---------------------------------------------------
    
    #for i in range (25):
    #    print(pattern_template[i])
    
    # for i in range (len(sequence_of_numbers)):
    #     print(sequence_of_numbers[i])
    
    #for i in range (25):
    #    print(player_card[i])
    
    #for i in range (25):
    #    print(player_marked_card[i])
    
    #for i in range (len(everything)):
    #    print(everything[i])
    
    # for i in range (25):
    #     print(pattern_template_180[i])
    
    # for i in range (25):
    #     print(player_marked_card[i])
    
    #----------------------------------------------------
     

    if (is_it_crazy(pattern_template) == False):
        for i in range (25):
            if (pattern_template[i] != 0):
                if (player_card[i] == sequence_of_numbers_last_number):
                    last_number_is_in_bingo = True
            if (pattern_template[i] != 0 and pattern_template[i] != player_marked_card[i]):
                counter_one += 1
        if (last_number_is_in_bingo == False):
            return "NO BINGO"
        else:
            if (counter_one > 0):
                return "NO BINGO"
            else:
                return "VALID BINGO"
    else:
        for i in range (25):
            if (pattern_template[i] != 0):
                if (player_card[i] == sequence_of_numbers_last_number):
                    last_number_is_in_bingo = True
            if (pattern_template[i] != 0 and pattern_template[i] != player_marked_card[i]):
                counter_two += 1
            
        for i in range (25):
            if (pattern_template_90[i] != 0):
                if (player_card[i] == sequence_of_numbers_last_number):
                    last_number_is_in_bingo_90 = True
            if (pattern_template_90[i] != 0 and pattern_template_90[i] != player_marked_card[i]):
                counter_two_90 += 1
        
        for i in range (25):
            if (pattern_template_180[i] != 0):
                if (player_card[i] == sequence_of_numbers_last_number):
                    last_number_is_in_bingo_180 = True
            if (pattern_template_180[i] != 0 and pattern_template_180[i] != player_marked_card[i]):
                counter_two_180 += 1
            
        for i in range (25):
            if (pattern_template_270[i] != 0):
                if (player_card[i] == sequence_of_numbers_last_number):
                    last_number_is_in_bingo_270 = True
            if (pattern_template_270[i] != 0 and pattern_template_270[i] != player_marked_card[i]):
                counter_two_270 += 1
            
        if (last_number_is_in_bingo == False and last_number_is_in_bingo_90 == False and last_number_is_in_bingo_180 == False and last_number_is_in_bingo_270 == False):
            return "NO BINGO"
        else:
            if (counter_two != 0 and counter_two_90 != 0 and counter_two_180 != 0 and counter_two_270 != 0):
                return "NO BINGO"
            else:
                return "VALID BINGO"
            
#------------------------------------------------------------------------------------------------------------------

def main ():
    read_input()
    marker()
    rotation_checker()
    print(is_it_a_winner())
    
main ()