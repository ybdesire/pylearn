# this code shoudle be run at Linux environment
import os 
  
  
# Create a child process 
# using os.fork() method  
pid = os.fork() 
  
# pid greater than 0 represents 
# the parent process  
if pid > 0 : 
    print("I am parent process:") 
    print("Process ID:", os.getpid()) 
    print("Child's process ID:", pid) 
  
# pid equal to 0 represnts 
# the created child process 
else : 
    print("\nI am child process:") 
    print("Process ID:", os.getpid()) 
    print("Parent's process ID:", os.getppid()) 
