import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

print ("Hello there!")
# 1 Create a Virtual Enviornment (VE)
        # Command to create VE: py -3 -m venv *myvenv*
            # *myvenv* is a placeholder name for your virtual enviornments name
# 2 Activate your VE
        # Command:.\myvenv\Scripts\activate
            # Use your virtual enviornment name in the first section
# 3 Install 3rd party library 
    # Command: pip3 install matplotlib

# Difference between source and version control:
    # Version control: Everything related to the document (Code, pictures, documents)
    # Source control: Specifically tThe code related to the document (For a website the html code)