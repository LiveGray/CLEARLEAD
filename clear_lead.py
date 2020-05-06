import os

class clear_lead:
    def __init__(self):
       print("Initiating connection to the matrix...")
       print("Enjoy your stay. :p")
    
    def check_dir(self):
        try:
            folders = ['./Amass-Output/', './Aquatone_Output', './NMap']
            for folder in folders:
                if not os.path.isdir(folder):
                    os.makedirs(folder)
                else:
                    pass        
        except Exception as e:
            print("Error encountered... \nReview the following: " + str(e))
       
    def amass_enum(self):
        try:
            with open('targets.txt') as f:
                for line in f:
                    line = line.rstrip()
                    amass_cmd = "amass enum -d " + line + " -o ./Amass-Output/" + line + ".txt"                   
                    os.system(amass_cmd)
                
        except Exception as e:
            print("Error encountered... \nReview the following: " + str(e))

    def aquatone_enum(self):
        files = [x for x in os.listdir("./Amass-Output") if x.endswith("txt")]
        for file in files:
            aqua_cmd = "cat Amass-Output/" + file + " | ./aquatone -ports medium -out ./Aquatone_Output/" + file       
            os.system(aqua_cmd)
            
def run():
    Clear_Lead = clear_lead()
    Clear_Lead.aquatone_enum()
        
def main():
    Clear_Lead = clear_lead()
    Clear_Lead.check_dir()
    Clear_Lead.amass_enum()

if __name__ == '__main__':
    try:
        main()
        run()
     
    except KeyboardInterrupt:
        print('\n \033[1;31m[!] Ctrl + C Detected, Quitting...')
exit(0)