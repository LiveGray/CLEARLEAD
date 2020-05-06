# Clear_Lead
The name is clear, the concept is simple. Run this to assess the external footprint of a given
website. Hopefully, there will be a clear lead to follow. 

# How It Works
In a nutshell, it takes in targets from targets.txt per line. 

Then runs OWASP's amass against each target in the file. 

After looping through every target, those targets are then scanned using NMaps Top 20.

Once looped through, the amass output files are dropped into Aquatone for validation. 

Sit back and wait... :D

# Installation & Usage (Test on Kali 2020)
Clear_Lead is a breeze to use. Simply clone the directory, and cd into it.

Assuming installation is on a kali system, amass is installed by default. 

Once within the cloned directory, please install aquatone here. 

Aquatone can be installed by reviewing: https://github.com/michenriksen/aquatone

Once Aquatone is installed, and executable, setup a targets.txt file in the same directory. 



# Usage Example
![alt text](https://github.com/nins3i/Clear_Lead/blob/master/cl.png)
