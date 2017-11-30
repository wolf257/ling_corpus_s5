#!/usr/bin/env python3
#-*- coding : utf8 -*-

## NOTE : Ne surtout pas déplacer ce fichier !! Sinon tous les paths changeront !!

import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__ + "/../../"))
CURRENT_ROOT = os.path.abspath(os.path.dirname(__file__))
CORPUS_ROOT = os.path.join(PROJECT_ROOT, 'corpus/')
CORPUS_TEST_ROOT = os.path.join(PROJECT_ROOT, 'corpus_litterature/')
MORPHALO_ROOT = os.path.join(PROJECT_ROOT, 'morphalo/')
RESULT_RAPPORT_ROOT = os.path.join(PROJECT_ROOT, 'resultats_et_rapport/')
TREETAGGER_ROOT = os.path.join(PROJECT_ROOT, 'from_outside_treetagger/')

def main():
    print(PROJECT_ROOT) #nous donne la base du dossier
    print(CURRENT_ROOT)
    print(CORPUS_ROOT)
    print(CORPUS_TEST_ROOT)
    print(MORPHALO_ROOT)
    print(RESULT_RAPPORT_ROOT)

if __name__ == '__main__':
    main()
