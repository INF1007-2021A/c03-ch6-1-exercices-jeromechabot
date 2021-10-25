#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        valuesType = None
        while(len(values)<10):
            values.append(input("Enter a value "))
        
    values.sort()
        
    return values


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words=[]
        words.append(input("Entrer le premier mot "))
        words.append(input("Entrer le deuxieme mot "))
    
    return sorted(list(words[0])) == sorted(list(words[1]))
    



def contains_doubles(items: list) -> bool:
    items.sort()
    return list(set(items)) != items


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_student_dict = {}
    best_grade = 0
    best_student = ""
    for cles in student_grades:
        if (sum(student_grades[cles]) / len(student_grades[cles])) > best_grade:
            best_student = cles
            best_grade = sum(student_grades[cles]) / len(student_grades[cles])
    best_student_dict[best_student] = best_grade
        
    return best_student_dict


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequence_dict = {}
    for lettre in sentence:
        if lettre in frequence_dict:
            frequence_dict[lettre]+=1
        else:
            frequence_dict[lettre] = 1
    liste_de_comptes = list(frequence_dict.values())
    liste_de_comptes.sort(reverse=True)

    final_dict = {}

    for compte in liste_de_comptes:
        if compte>=5:
            for lettre in frequence_dict:
                if frequence_dict[lettre] == compte:
                    final_dict[lettre] = compte
                    del frequence_dict[lettre]
                    break
        else:
            break
    

    return final_dict


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    # print(f"On essaie d'ordonner les valeurs...")
    # order()

    # print(f"On vérifie les anagrammes...")
    # print(anagrams())

    # my_list = [3, 3, 5, 6, 1, 1]
    # print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
