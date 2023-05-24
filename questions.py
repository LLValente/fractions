import random as rd
QUESTIONS_START =   {'': '', 
                    '': '', 
                    '': '', 
                    '': ''}

QUESTIONS_END =     {'': '', 
                    '': '', 
                    '': '', 
                    '': ''}       
def main():

    NUMBERS_DICT_9 =    {"1": 'Um',
                        "2": 'Dois',
                        "3": 'Três',
                        "4": 'Quatro',
                        "5": 'Cinco',
                        "6": 'Seis',
                        "7": 'Sete',
                        "8": 'Oito',
                        "9": 'Nove'}

    NUMBERS_DICT_20 =   {"10": 'Dez',
                        "11": 'Onze',
                        "12": 'Doze',
                        "13": 'Treze',
                        "14": 'Quatorze',
                        "15": 'Quinze',
                        "16": 'Dezesseis',
                        "17": 'Dezessete',
                        "18": 'Dezoito',
                        "19": 'Dezenove',
                        "20": 'Vinte'}

    NUMBERS_DICT_TWO_ALG =  {"20": 'Vinte',
                            "30": 'Trinta',
                            "40": 'Quarenta',
                            "50": 'Cinquenta',
                            "60": 'Sessenta',
                            "70": 'Setenta',
                            "80": 'Oitenta',
                            "90": 'Noventa',
                            "100": 'Cem'}

    NUMBERS_DICT_FRACTIONAL =   {"2": "meio",
                                "3": "terço",
                                "4": 'quarto',
                                "5": 'quinto',
                                "6": 'sexto',
                                "7": 'sétimo',
                                "8": 'oitavo',
                                "9": 'nono',
                                "10": 'décimo',
                                "100": 'centésimo'}

class Question:

    def __init__(self):

        #self.start = QUESTIONS_START[self.type]
        #self.end = QUESTIONS_START[self.type]
        self.items = self.items()
        self.answears = ''

    def items(self, items_numbers = 6):

        fractions = []

        i = 1

        while i <= items_numbers:

            fraction = Fracao()
            fractions.append(fraction)

            i += 1

        return fractions

    
    # Gera as frações e salva na lista 'fractions'
    # TODO: Adicionar as frações que envolvam os "avos".
    def reading_question(fractions = []):

        print("\t\\item Escreva os nomes das frações a seguir:")
        print("\t\t\\begin" + r"{center}")
        print("\t\t\t\\begin" + r"{enumerate}" + "\n")
        

        if fractions is []:

            fractions = generate_fractions(6)
        
        for fraction in fractions:

            print('\t\t\t\t\\item $\\frac{'+ str(fraction[0]) +'}{' + str(fraction[1]) + '}$')

        print("\n\t\t\t\\end" + r"{enumerate}")
        print("\t\t\\end" + r"{center}" + "\n")

        return fractions

    def answears_to_reading_question(fractions):

        answears = []

        print("\t\t\\begin" + r"{center}")
        print("\t\t\t\\begin" + r"{enumerate}" + "\n")
        
        for fraction in fractions:

            numerator = fraction[0]
            denominator = fraction[1]

            first_part_name = ''
            second_part_name = ''

            if numerator <= 20:

                try:

                    first_part_name = NUMBERS_DICT_9[str(numerator)]

                except:

                    first_part_name = NUMBERS_DICT_20[str(numerator)]

            elif numerator > 20:

                first_part_name = NUMBERS_DICT_TWO_ALG[str(numerator//10 * 10)]
                
                if numerator % 10 == 0:

                    next
                
                else:

                    first_part_name = first_part_name + " e " + NUMBERS_DICT_9[str(numerator % 10)].lower()

            if denominator <= 10 or denominator == 100:

                second_part_name = NUMBERS_DICT_FRACTIONAL[str(denominator)]

            if denominator <= 20 and denominator < 10:

                try:

                    second_part_name = NUMBERS_DICT_9[str(denominator)].lower()

                except:

                    second_part_name = NUMBERS_DICT_20[str(denominator)].lower()

            elif denominator > 20:

                second_part_name = NUMBERS_DICT_TWO_ALG[str(denominator//10 * 10)].lower()
                
                if denominator % 10 == 0:

                    next
                
                else:

                    second_part_name = second_part_name + " e " + NUMBERS_DICT_9[str(denominator % 10)].lower() + " avos"

            answear = first_part_name + " " + second_part_name

            answears.append(answear)

        return answears

    # Gera questão sobre a correspondência de uma fração com um número decimal
    def questao_representacao(items_quantity = 6, fractions = [], kind = "half"):

        answears = []

        if len(fractions) == 0:

            fractions = gerar_fracoes(items_quantity)
        
        # Este tipo gera metade decimal -> fração, metade fração -> decimal
        if kind == "half":

            for i in range(0, len(fractions)):

                if i < len(fractions)/2:

                    ltxLine = "\\item \\frac" + "{" + str(fractions[i][0]) + "}" + "{" + str(fractions[i][1]) + "}" + "\n"

                    print(ltxLine, end='')
                    
                    answears.append(fractions[i][0]/fractions[i][1])

                elif i >= len(fractions)/2:

                    decimal = fractions[i][0] / fractions[i][1]

                    ltxLine = "\\item " + str(decimal) + "\n"
            
                    print(ltxLine, end='')

                    answears.append(fractions[i])
        
        # Este tipo gera metade fração -> decimal
        if kind == "decimal":

            for fraction in fractions:

                ltxLine = "\\item \\frac" + "{" + str(fraction[0]) + "}" + "{" + str(fraction[1]) + "}" + "\n"
        
                print(ltxLine, end='')

                answears.append(fraction[0]/fraction[1])

        # Este tipo gera metade decimal -> fração
        if kind == "fraction":

            for i in range(len(fractions)):

                    decimal = fractions[i][0] / fractions[i][1]

                    ltxLine = "\\item " + str(decimal) + "\n"
            
                    print(ltxLine, end='')

                    answears.append(fractions[i])

        return answears

