import ThumbnailProgram.py#First I made it import the other programs
import LogoProgram.py
import MirrorProgram.py
print('Hello, Which of these languages do you prefer, English or Spanish?')#Then it asks you what language you prefer
input()#I have inputs afer each question
if input == English:#The English selection starts this tree
    print('Hello, would you like to make an image a thumbnail size?')#It then asks if you would like to use stated program
    input()
    if input() == yes:#If you put yes it will start the program and affect each image
        os.system("ThumbnailProgram.py")
    elif input() == no:
        print('Would you like to add a logo?')
        input()
        if input() == yes:
            os.system("LogoProgram.py")
        elif input() == no:
            print('Then would you like to mirror the image?')
            input()
            if input() == yes:
                os.system("MirrorProgram")
            elif input() == no:
                Print('All done')#Once it is finished it will print that it is done
elif input == Spanish:#The Spanish input starts this tree and everything afer is the same just in a different language
    print('¿Hola, le gustaría para hacer la imagen un tamaño de miniatura ?')
    input()
    if input() == si:
        os.system("ThumbnailProgram.py")
    elif input() == no:
        print('¿Queres poner una logotipo?')
        input()
        if input() == si:
            os.system("LogoProgram.py")
        elif input() == no:
            print('¿A continuación, le gustaría para invertir la imagen?')
            input()
            if input() == si:
                os.system("MirrorProgram")
            elif input() == no:
                Print('Todo Listo')
    
exit
        
   
    
