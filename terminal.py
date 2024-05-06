import sys, subprocess
class Terminal():
    @staticmethod
    def clear():
        subprocess.run('cls', shell=True)  
        
        
def test():
    print("this is a test ")
    Terminal.clear()
    
if __name__ == '__main__':
    test()