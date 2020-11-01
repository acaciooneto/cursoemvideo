def readint(msg):
    while True:
        try:
            inside = int(input(msg))
            return inside
        except KeyboardInterrupt:
            print("\n\033[31mERROR! The user didn't want to complete the task, i'll assume the value as 0.\033[m")
            return 0
        except:
            print("\033[31mERROR! Say a valid integral number.\033[m")

def readfloat(msg):
    while True:
        try:
            inside = float(input(msg))
            return inside
        except KeyboardInterrupt:
            print("\n\033[31mERROR! The user didn't want to complete the task, i'll assume the value as 0.\033[m")
            return 0
        except:
            print('\033[31mERROR! Say a valid real number.\033[m')

nint = readint('Say some integral number: ')
nfloat = readfloat('Now say a real number: ')
print(f'The integral informed value was {nint}, and the real value was {nfloat}')
