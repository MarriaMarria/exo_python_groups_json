import random
import logging
import json

logging.basicConfig(filename='text.log', level=logging.INFO,
format='%(asctime)s:%(levelname)s:%(message)s') 

logging.info("getting text file: start")
f = open("list_of_names.txt", "r")
names = f.read()
print(names)
logging.info("getting text file: end")

logging.info("getting a list: start")
my_list = names.split(",") # list of names to divide in groups
logging.info("getting a list: end")

# I create dictionary to store the data from the loop
my_dict = dict()

def group_division():
    nb_par_group = 2
    nb_of_groups = 1


    file_with_groups = open("file_groups.txt", "w")
    out_file = open("myfile.json", "w") # I will save my data in JSON file

    logging.info("loop to divide ppl in groups: start")
    while my_list:

        if len(my_list) >= nb_par_group: # if I have 2+ ppl left
            selected = random.sample(my_list, nb_par_group) # I choose randomly two ppl from my list of names 
        else:
            selected = my_list # if one person rest he forms his own group of one
        
        my_dict['group'] = selected # I add names to my dict
        print(my_dict)
        json.dump(my_dict, out_file, indent=4, sort_keys=False)

        logging.info("GROUP #%s : %s" % (nb_of_groups, selected))
        
        for sel in selected:
            my_list.remove(sel)



        file_with_groups.write(f"Group {nb_of_groups}: {selected} \r")
        

        
        
        nb_of_groups = nb_of_groups + 1

    file_with_groups.close()

    return my_dict

    
group_division()


logging.info("loop to divide ppl in groups: end")
