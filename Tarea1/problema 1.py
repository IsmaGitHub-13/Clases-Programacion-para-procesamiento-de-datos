#Problema 1 
Calificacion = 10
if (Calificacion < 0 or Calificacion > 10) :
    print("nota no valida")
else :
    if (Calificacion >= 0 and Calificacion < 5 ) : 
        print("suspenso")
    else :
         if (Calificacion >= 5 and Calificacion < 6) :
            print("suficiente") 
         else :
             if  (Calificacion >= 6 and Calificacion < 7) :
               print("bien") 
             else :
                if (Calificacion >= 7 and Calificacion < 9):
                 print("notable")
                else :
                   if (Calificacion >= 9 and Calificacion <= 10) :
                     print("Sobresaliente")
