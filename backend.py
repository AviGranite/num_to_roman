import re

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


def num_to_roman(x):
    

    """Convert an integer to a Roman numeral between 1-3999"""

        
    while int(x) < 4000 and int(x) > 0:
        result = []
        result_h = []
        result_t = []
        result_o = []
        
        ###dividing and categorizing digits###

        parts = [d for d in str(x)]
        
        if len(str(x)) == 4:
            result = (int(x) // 1000) * 'M'
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

    

roman = {
    'I' : 1,
    'IV' : 4,
    'V' : 5,
    'IX' : 9,
    'X' : 10,
    'XL' : 40,
    'L' : 50,
    'XC' : 90,
    'C' : 100,
    'CD' :  400,
    'D' : 500,
    'CM' : 900,
    'M' : 1000,
    '' : 0
    } 

def roman_convert(x):
    
    """Converts roman numeral to number"""
    
    x = x.upper()
    
    while re.match("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", x):     ###validating roman numeral input###        
          
        s = re.split(r"(IV|IX|XL|XC|CD|CM|I|V|X|L|C|D|M)", x)                          ###split everything up####
        r = sum([roman[t] for t in s])                                                 ###add together values from dict###

        return r
        break
    
    else:

        return "That's not a Roman Numeral!"                                            ###account for user error ###

