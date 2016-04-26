import ThumbnailProgram.py
import LogoProgram.py
import MirrorProgram.py
print('Hello, Which of these languages do you prefer, English or Spanish?')
input()
if input == English:
    print('Hello, would you like to make an image a thumbnail size?')
    input()
    if input() == yes:
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
                Print('All done')
elif input == Spanish:
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
        
   
    
