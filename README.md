# Access-Point-Automation
A python script that automates setting up an access point without the need for a controller. For my Cisco CCNP class at school.

# To run this script you must:

  1. Install the dependencies, which can be done with the following command (remember to navigate to the folder:
  ```
  pip install -r requirements.txt
  ```
  
  2. Must have the specified OS file to install, or have your own and replace it in the code.
  
  3. Set the ip address of you computer to ```172.28.128.7``` with subnet mask ```255.255.255.0```.
  
  4. Install tftpd32 software and navigate in the file system to your specified OS file to be installed on the access point.
  
  5. Plug in the access point and boot in ROM mode.
  
  6. Run the script using the following command
  ```
  python accesspoint.py
  ```
  
  7. Let the program do the rest of the work!
