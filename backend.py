ones = {
    1 : 'I',
    4 : 'IV',
    5 : 'V',
    9 : 'IX',
    }

tens = {
    1 : 'X',
    4 : 'XL',
    5 : 'L',
    9 : 'XC'
    }

hundreds = {
    1 : 'C',
    4 : 'CD',
    5 : 'D',
    9 : 'CM'
    }


def NumToRoman(x):
    

    """Coverts any number to roman numeral (max 3999)"""
    try:
        x = int(x)
        
        while x < 4000 and x > 0:
            result = []
            result_h = []
            result_t = []
            result_o = []
            
            ###dividing and categorizing digits###

            parts = [d for d in str(x)]
            
            if len(str(x)) == 4:
                result = int(x // 1000) * 'M'
                h = parts[1]                
                t = parts[2]
                o = parts[3]

            elif len(str(x)) == 3:
                h = parts[0]
                t = parts[1]
                o = parts[2]

            elif len(str(x)) == 2:
                h = None
                t = parts[0]
                o = parts[1]
                
            else:
                h = None
                t = None
                o = parts[0]
              

            ### filtering values ###

            
            if h is None:
                pass
            elif int(h) in hundreds:
                result_h = hundreds[int(h)] 
            elif int(h) in range(2, 4):
                result_h = int(h) * 'C'
            elif int(h) == 0:
                result_h = ''    
            else:
                result_h = 'D' + int(int(h) - 5) * 'C'

            

            if t is None:
                pass

            elif int(t) in tens:
                result_t = tens[int(t)]                 
            elif int(t) in range(2, 4):
                result_t = int(t) * 'X'
            elif int(t) == 0:
                result_t = ''    
            else:
                result_t = 'L' + int(int(t) - 5) * 'X'
                

            if int(o) in ones:
                result_o = ones[int(o)]                    
            elif int(o) in range(2, 4):
                result_o = int(o) * 'I'
            elif int(o) == 0:
                result_o = ''
            else:
                result_o = 'V' + int(int(o) - 5) * 'I' 
            
                

            if len(str(x)) == 4:
                togo = result + str(result_h) + str(result_t) + str(result_o)
            elif len(str(x)) == 3:
                togo = str(result_h) + str(result_t) + str(result_o)
            elif len(str(x)) == 2:
                togo = str(result_t) + str(result_o)
            else:
                togo = str(result_o)
            


            return togo
            break
        else:
            return "That's not a number between 1 and 3999"
    except:
        return "Only numbers please!"

