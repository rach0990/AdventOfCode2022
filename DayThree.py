
import InputVars
lower_case = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

requirement_met = False
total = 0
for item in InputVars.backpack.split('\n'):
    compartment1, compartment2 = item[:len(item)//2], item[len(item)//2:]
    requirement_met = False
    for char in compartment1:
        if requirement_met == True :
            break
        for char2 in compartment2:
         if char ==char2 and char in lower_case:
            total += lower_case.index(char)+1
            requirement_met =True
         
         if requirement_met == True :
            break

        
#Part 2
count = 0
total = 0
requirement_met = False
for item in InputVars.backpack.split('\n'):
    
    if (count ==0):
        elf1 = item
        count+=1     
    elif (count == 1):
        elf2=item
        count+=1
    elif(count == 2) :
        elf3 = item
        count = 0
        for char in elf1:
            if char in elf2 and char in elf3:
             
                total += lower_case.index(char)+1
                requirement_met =True
                
                break   

print(total)

