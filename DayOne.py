import InputVars

        
elf_list = []
new_list = []

for line in InputVars.input.split('\n'):
       
           if line != "":
                 new_list.append(int(line.strip()))
           #elf_list.append(new_list)

           if line == '':
                elf_list.append(sum(new_list))
                new_list = []

         # elf_list.append(new_list)


elf_list.sort(reverse=True)

print(max(elf_list))
total = elf_list[0] + elf_list[1] + elf_list[2]

print(total)



        
                
        







