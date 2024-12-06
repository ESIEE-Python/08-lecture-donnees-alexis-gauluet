"""bienvenue, joyeux hunger games"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, 'r',encoding='utf8') as f:
        r = csv.reader(f,delimiter=';')
        l=[[int(x) for x in line] for line in r]
    return l

def get_list_k(data, k):
    """retourne la ligne d'indice k"""
    return data[k]

def get_first(l):
    """retourne le premier élément de la liste"""
    return int(l[0])

def get_last(l):
    """retourne le dernier element de la liste"""
    return int(l[-1])

def get_max(l):
    """retourne l'element maximum de la liste"""
    return int(max(l))

def get_min(l):
    """retourne l'élément minimum de la liste"""
    return int(min(l))

def get_sum(l):
    """retourne la somme de tous les éléments de la liste"""
    s=0
    i=0
    while i<len(l) :
        s+=int(l[i])
        i+=1
    return s

#### Fonction principale


def main():
    """fonction principale"""
    data = read_data(FILENAME)
    print (data)
    #for i, l in enumerate(data):
    #     print(i, l)
    # k = -1
    # print (get_list_k(data,k))


if __name__ == "__main__":
    main()
