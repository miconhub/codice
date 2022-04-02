#-*- coding: utf-8 -*-
#Programma 2

import sys
import nltk
import math
from nltk import bigrams
from nltk import trigrams

listaPunteggiatura=[".", ",", "?", "!", ";", "(", ")"] #creo una lista della punteggiatura

#Estrarre e ordinare in sequenza decrescente e indicando la frequenza le 10 POS più frequenti, 
#10 bigrammi POS più frequenti, 10 trigrammi POS più frequenti, 20 aggettivi e avverbi più frequenti

def TestoTokensPOS(frasi):
    tokensTOT=[] #lista contenente i tokens, inizialmente vuota
    tokensPOStot=[] #lista delle Part-Of-Speech dei tokens, inizialmente vuota
    bigTOT=[] #lista dei bigrammi, inizialmente vuota
    trigTOT=[] #lista dei trigrammi, inizialmente vuota
    bigPOS=[] #lista dei bigrammi di POS, inizialmente vuota
    trigPOS=[] #lista dei trigrammi di POS, inizialmente vuota
    for frase in frasi: #scorro le frasi
        tokens=nltk.word_tokenize(frase) #il testo della frase viene diviso in tokens
        tokensPOS=nltk.pos_tag(tokens) #viene eseguita l'analisi morfo-sintattica dei tokens
        bigToken=list(bigrams(tokens)) #estraggo i bigrammi di tokens
        trigTOK=list(trigrams(tokens)) #estraggo i trigrammi di tokens
        bigTOT=bigTOT+bigToken #aggiorno la lista dei bigrammi di tokens
        trigTOT=trigTOT+trigTOK #aggiorno la lista dei trigrammi di tokens
        bPOS=list(bigrams(tokensPOS)) #estraggo i bigrammi di POS
        tPOS=list(trigrams(tokensPOS)) #estraggo i trigrammi di POS
        bigPOS=bigPOS+bPOS #aggiorno la lista dei bigrammi di POS
        trigPOS=trigPOS+tPOS #aggiorno la lista dei trigrammi di POS
        tokensTOT=tokensTOT+tokens #la lista tokensTOT viene riempita con i tokens
        tokensPOStot=tokensPOStot+tokensPOS #la lista tokensPOStot viene riempita con le Part-Of-Speech dei tokens
    return tokensTOT, tokensPOStot, bigTOT, trigTOT, bigPOS, trigPOS

#10 POS più frequenti
def FrequenzaPOS(tokensPOS, tokens):
    listaPOS=[] #creo una lista vuota per le POS
    vocabolario=set(list(tokens)) #creo il vocabolario usando set
    for tok in vocabolario: #scorro il vocabolario
        for pos in tokensPOS:
            if pos not in listaPunteggiatura: #seleziono le POS che non sono segni di punteggiatura
                listaPOS.append(pos) #le inserisco nella lista
                frequenzaPOS=nltk.FreqDist(listaPOS) #calcolo la loro frequenza
                dieciPOS=frequenzaPOS.most_common(10) #seleziono le 10 più frequenti
    return dieciPOS
    

#10 bigrammi POS più frequenti
def FrequenzaBigrammi(tokensPOS, bigrammiPOS):
    listaB=[] #creo una lista vuota in cui inserire i bigrammi
    for big in bigrammiPOS: #scorro la lista sei bigrammi
        if big not in listaPunteggiatura: #seleziono quelli diversi dalla punteggiatura
            listaB.append(big) #e li inserisco nella lista vuota, andandola a riempire
            freqB=nltk.FreqDist(listaB) #calcolo la loro frequenza
            frequenzaBigrammi=freqB.most_common(10) #e seleziono i 10 bigrammi POS più frequenti
    return frequenzaBigrammi
    
    
 #10 trigrammi POS più frequenti       
def FrequenzaTrigrammi(tokensPOS, trigrammi):
    listaT=[] #creo una lista vuota
    for tri in trigrams: #scorro i trigrammi
        if tri not in listaPunteggiatura: #prendo quelli che non appartengono alla lista punteggiaturaa
            listaB.append(tri) #li aggiungo alla lista che inizialmente era vuota
            freqT=nltk.FreqDist(listaT) #calcolo le frequenze
            frequenzaTrigrammi=freqT.most_common(10) #seleziono i 10 trigrammi POS più frequenti
    return frequenzaTrigrammi


def FreqAggAvv(tokensPOS):
    agg=['JJ', 'JJR', 'JJS'] #creo una lista con i POS tag che identificano gli aggettivi
    avv=['RB', 'RBR', 'RBS'] #creo una lista con i POS tag che identificano gli avverbi
    listAgg=[] #creo una lista vuota per gli aggettivi
    listAvv=[] #e una lista vuota per gli avverbi
    for pos in tokensPOS: #scorro le POS
        if pos in agg: #se una POS è taggata come aggettivo
            listAgg.append(pos) #la aggiungo alla lista vuota creata per gli aggettivi
            freqAgg=nltk.FreqDist(listAgg) #calcolo le frequenze
            frequenzaAgg=freqAgg.most_common(20) #prendo le 20 più frequenti
        if pos in avv: #se invece la POS è taggata come avverbio
            listAvv.append(pos) #la aggiungo alla lista vuota creata per gli avverbi
            freqAvv=nltk.FreqDist(listAvv) #calcolo le frequenze
            frequenzaAvv=freqAvv.most_common(20) #seleziono le 20 più frequenti
    return frequenzaAgg, frequenzaAvv

def BigAggSos(tokensPOS, bigrammiPOS): 
    listBig=[] #creo una lista vuota
    lAgg=['JJ', 'JJR', 'JJS'] #creo la lista dei tag degli aggettivi
    lSos=['NN', 'NNS', 'NNP', 'NNPS'] #creo la lista dei tag dei sostantivi
    for big in bigrammiPOS: #scorro i bigrammi di POS
        pos1=big[0][0] #primo elemento del bigramma
        pos2=big[0][1] #secondo elemento del bigramma 
        fpos1=pos1.FreqDist #calcolo la frequenza del primo elemento
        fpos2=pos2.FreqDist #e del secondo
        if fpos1>3 and fpos2>3: #se sono maggiori di 3
            if pos1 in lAgg and pos2 in lSos: #e se il primo elemento è un aggettivo e il secondo un sostantivo
                listBig.append(big) #aggiungo il bigramma alla lista vuota
                distAggSos=nltk.freqDist(listBig) #calcolo la frequenza dei bigrammi
                distOrd=distAggAvv.most_common(10) #seleziono i 10 più frequenti
    return distOrd

#Frequenza massima
def FreqMax(bigrammiAggSos):
    for bigramma in bigrammAggSos: #scorro la lista dei bigrammi aggettivo-sostantivo
        freqBigrammi=nltk.FreqDist(bigAggSos) #calcolo la frequenza
        ventiBig=freqBigrammi.most_common(20) #seleziono i 20 più frequenti
    return freqBigrammi, ventiBig

#Probabilità condizionata massima
def ProbCondeLMI(tokens, bigrammiAggSos):
    lunghezzaCorpus=len(tokensTOT) #creo la variabile con la lunghezza del corpus
    dizionarioPcond={} #creo un dizionario vuoto per la probabilità condizionata
    dizionarioLMI={} #creo un altro dizionario vuoto, in questo caso per la Local Mutual Informatio
    for bigramma in bigrammAggSos: #scorro i bigrammi formati da aggettivo e sostantivo
        token1=bigramma[0] #seleziono il primo token del bigramma
        token2=bigramma[1] #e il secondo token
        freqToken1=tokens.count(token1) #calcolo la frequenza del primo token
        freqToken2=tokens.count(token2) #calcolo la frequenza del secondo token
        freqBigrammiAS=bigrammiAggSos.count(bigramma) #calcolo la frequenza dei bigrammi
        probCond=freqBigrammiAggAvv*1.0/freqToken1*1.0 #calcolo la probabilità condizionata
        dizionarioPcond[bigramma]=probCond #riempio il dizionario della probabilità condizionata
        probToken1=freqToken1*1.0/len(tokensPOS)*1.0 #calcolo la probabilità del primo token
        probToken2=freqToken2*1.0/len(tokensPOS)*1.0 #calcolo anche la probabilità del secondo token
        LMI=freqBigrammiAS*math.log((freqBigrammiAS/lunghezzaCorpus)/(freqToken1*freqToken2)) #calcolo la LMI
        dizionarioLMI[bigramma]=LMI #e riempio il dizionario della LMI
        
    dizPc=sorted(dizionarioPcond.items(), key=lambda x:x[1], reverse=True) #ordino il primo dizionario
    dizlmi=sorted(dizionarioLMI.items(), key=lambda x:x[1], reverse=True) #ordino anche il secondo dizionario
        
    return dizPC, dizlmi

def EstraiFrasi(frase, tokens):
    dist=0.0 #inizializzo la variabile per la distribuzione a 0.0
    freqToken=0.0 #inizializzo la variabile per la frequenza dei token a 0.0
    freqTokenTOT=0.0 #inizializzo la variabile per le distribuzioni di frequenza a 0.0
    for frase in frasi: #scorro le frasi
       	for tok in tokens: #scorro i tokens
            if len(frase)>6 and len(frase)<25 and tokens.count(tok)>=2: #se la lunghezza della frase è compresa tra 6 e 25 e il token ha una frequenza maggiore o uguale a 2
                freqToken=nltk.freqDist(token) #calcolo la distribuzione di frequenza 
                freqTokenTOT=freqTokenTOT+freqToken #sommo le distribuzioni
                dist=freqTokenTot/len(frase) #e le divido per la lunghezza della frase 
    return dist

def ProbMarkov2(frase, tokens, trigrammi):
    lungCorpus=len(tokensTOT) #creo una variabile con la lunghezza del corpus
    lungVocabolario=len(set(tokens)) #creo una variabile con la lunghezza del vocabolario
    lungFrase=len(frase) #creo una variabile con la lunghezza della frase
    distFreqTokens=nltk.FreqDist(tokens) #creo una variabile con la frequenza dei tokens
    distFreqTrig=nltk.FreqDist(trigrammi) #creo una variabile con la frequenza dei trigrammi
    probMax=1.0 #creo una variabile per la probabilità massima
    token1=trigrammi[0] #seleziono il primo token del trigramma
    token2=trigrammi[1] #seleziono il secondo token del trigramma
    token3=trigrammi[2] #seleziono il terzo token del trigramma
    probabilita=(DistFreqToken[token1]*1.0/LunghezzaCorpus) #calcolo la probabilita del primo token 
    for trig in trigrammi: #socrro i trigrammi
            if lungFrase>=6 and lungFrase<25 and distFreqTokens>=2: #controllo che la lunghezza della frase sia compresa tra 0 e 25 e che il token compaia almen 2 volte nel corpus
                fTrig=(distFreqTrig[trigramma]) #calcolo la frequenza del trigramma
                freqA=(distFreqToken[trigramma[0]]) #calcolo la frequenza del primo elemento
                freqB=(distFreqTokens[trigramma[1]]) #del secondo
                freqC=(distFreqTokens[trigramma[2]]) #e del terzo
                probCond=(distFreqTrig[trig]*1.0/(distFreqTokens(token1))*(distFreqTokens(token2))) #calcolo la probabilità condizionata
    prob=probabilita*probCond #moltiplico le due probabilita calcolate
    probMax=math.max(prob) #e seleziono la probabilità massima
    trigrammaMax=trig #seleziono il trigramma con probabilita massima
    return probMax, trigrammaMax
    
def NEtagging(tokensPOStot):
    listaPERSON=[] #creo una lista vuota per le NE taggate PERSON
    listaGPE=[] #creo una lista vuota per le NE taggate GPE
    listaORG=[] #creo una lista per le NE taggate ORG
    analisi=nltk.ne_chunk(tokensPOStot) #utilizzo la funzione ne_chunk per ottenere la rappresentazione ad albero
    IOBFormat=nltk.chunk.tree2conllstr(analisi) #questa funzione trasforma l'albero ottenuto in precedenza in un formato IOB
    for nodo in analisi: #scorro i nodi
        NE='' #inizializzo la NE con una stringa vuota
        if hasattr(nodo, 'label'): #controllo la posizione del nodo nell'albero
            if nodo.label()=='PERSON': #se hanno l'attributo PERSON
                for partNE in nodo.leaves(): #se la NE è nelle foglie del nodo
                    NE=NE+' '+partNE[0] #la aggiungo alla lista
                listaPERSON.append(NE) #e quindi vado a riempire la lista
            if nodo.label()=='GPE': #ripeto il procedimento precedente per le GPE
                for partNE in nodo.leaves():
                    NE=NE+' '+partNE[0]
                listaGPE.append(NE)
            if nodo.label()=='ORGANIZATION': #ripeto il procedimento per le ORGANIZATION
                for partNE in nodo.leaves():
                    NE=NE+' '+partNE[0]
                listaORG.append(NE)
    freqNomiPropri=nltk.FreqDist(listaPERSON)
    

def main (Corpus1, Corpus2):
    fileInput1=open(Corpus1, mode='r', encoding='utf-8')
    fileInput2=open(Corpus2, mode='r', encoding='utf-8')
    raw1=fileInput1.read()
    raw2=fileInput2.read()
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    frasi1=sent_tokenizer.tokenize(raw1)
    frasi2=sent_tokenizer.tokenize(raw2)
    tokens1, tokensPOS1, bigrammi1, trigrammi1, bigrammiPOS1, trigrammiPOS1=TestoTokensPOS(frasi1)
    tokens2, tokensPOS2, bigrammi2, trigrammi2, bigrammiPOS2, trigrammiPOS2=TestoTokensPOS(frasi2)
    
    #stampo i risultati dell'analisi del primo corpus
    print('Risultati analisi corpus1:') 
    print()
    #stampo le 10 POS più frequenti
    freqPOS1=FrequenzaPOS(tokensPOS1, tokens1)
    print ('Le 10 POS più frequenti sono:')
    for pos in freqPOS1:
        print('Part-of-speech:', pos[0], '\tFrequenza POS:', pos[1])
    #stampo i 10 bigrammiPOS più frequenti    
    FreqBigrammiPOS1=FrequenzaBigrammi(tokensPOS1, bigrammiPOS1)
    print('I 10 bigrammi POS più frequenti sono:')
    for big in FreqBigrammiPOS1:
        print('Bigramma POS:', big[0], '\tFrequenza:', big[1])
    #e i 10 trigrammi POS più frequenti    
    FreqTrigrammiPOS1=FrequenzaTrigrammi(tokensPOS1, trigrammiPOS1)
    print('I 10 trigrammi POS più frequenti sono:')
    for trig in FreqTrigrammiPOS1:
        print('Trigramma POS:', trig[0], '\tFrequenza:', trig[1])
    #stampo i 20 aggettivi e i 20 avverbi più frequenti
    FreqAggAvv1=FreqAggAvv(tokensPOS1)
    print('I 20 aggettivi e i 20 avverbi più frequenti sono:')
    for a in FreqAggAvv1:
        print('Aggettivi e avverbi:', a[0], '\tFrequenza:', a[1])
    #stampo i 20 bigrammi aggettivo-sostantivo: 
    #più frequenti
    BigAggSos1=BigAggSos(tokensPOS1, bigrammiPOS1)
    print('I 20 bigrammi aggettivo-sostantivo più frequenti sono:')
    for b in BigAggSos1:
        print('Bigramma:', b[0][0], b[0][1], '\tFrequenza:', b[1])
    #con la frequenza massima
    FreqAggSos1=FreqMax(BigAggSos1)
    print('I 20 bigrammi aggettivo-sostantivo con frequenza massima sono:')
    for f in FreqAggSos1:
        print('Bigramma:', f[0][0], f[0][1], '\tFrequenza:', f[1])
    #con probabilità condizionata massima    
    ProbCondLMI1=ProbCondeLMI(BigAggSos1)
    print('I 20 bigrammi aggettivo-sostantivo con probabilità condizionata massima sono:')
    for bas in ProbCondLMI1:
        for pc in dizPc:
            print('Bigramma:', pc[0][0], pc[0][1], '\tProbabilità condizionata:', pc[1])
    #con la Local Mutual Information maggiore    
    print('I 20 bigrammi aggettivo-sostantivo con Local Mutual Information massima sono:')
    for clmi in ProbCondLMI1:
        for l in dizlmi:
            print('Bigramma:', l[0][0], l[0][1], '\tLMI:', l[1])
    #stampo la frase con distribuzione media più alta    
    Distrib1=EstraiFrasi(frasi1, tokens1)
    print('La distribuzione media più alta in una frase è:')
    for d in Distrib1:
        print('Frase:', d[0], '\tDistribuzione:', math.max(d[1]))
    #stampo le frasi con la relativa probabilità calcolata con un modello markoviano di ordine 2        
    Markov1=ProbMarkov2(frasi1, tokens1, trigrammi1)
    print('La probabilita delle frasi calcolata con un modello di Markov di ordine 2 è:')
    for m in Markov1:
        print('Frase:', m[0], '\tProbabilità:', m[1])
    #stampo le i5 NE di nomi propri con frequenza maggiore    
    NEtag1=NEtagging(tokensPOS1)
    print('Le 15 NE di nomi propri più frequenti sono:')
    for n in NEtag1:
        print('Entità nominata:', n[0], '\tFrequenza:', n[1])
    #stampo i risultati dell'analisi del secondo corpus 
    print()    
    print('Risultati analisi corpus2:')
    print()
    #stampo le 10 POS più frequenti
    freqPOS2=FrequenzaPOS(tokensPOS2, tokens2)
    print ('Le 10 POS più frequenti sono:')
    for pos in freqPOS2:
        print('Part-of-speech:', pos[0], '\tFrequenza POS:', pos[1])
    #stampo i 10 bigrammiPOS più frequenti     
    FreqBigrammiPOS2=FrequenzaBigrammi(tokensPOS2, bigrammiPOS2)
    print('I 10 bigrammi POS più frequenti sono:')
    for big in FreqBigrammiPOS2:
        print('Bigramma POS:', big[0], '\tFrequenza:', big[1])
    #e i 10 trigrammi POS più frequenti    
    FreqTrigrammiPOS2=FrequenzaTrigrammi(tokensPOS2, trigrammiPOS2)
    print('I 10 trigrammi POS più frequenti sono:')
    for trig in FreqTrigrammiPOS2:
        print('Trigramma POS:', trig[0], '\tFrequenza:', trig[1])
    #stampo i 20 aggettivi e i 20 avverbi più frequenti
    FreqAggAvv2=FreqAggAvv(tokensPOS2)
    print('I 20 aggettivi e i 20 avverbi più frequenti sono:')
    for a in FreqAggAvv2:
        print('Aggettivi e avverbi:', a[0], '\tFrequenza:', a[1])
    #stampo i 20 bigrammi aggettivo-sostantivo: 
    #più frequenti
    BigAggSos2=BigAggSos(tokensPOS2, bigrammiPOS2)
    print('I 20 bigrammi aggettivo-sostantivo più frequenti sono:')
    for b in BigAggSos2:
        print('Bigramma:', b[0][0], b[0][1], '\tFrequenza:', b[1])
    #con la frequenza massima
    FreqAggSos2=FreqMax(BigAggSos2)
    print('I 20 bigrammi aggettivo-sostantivo con frequenza massima sono:')
    for f in FreqAggSos2:
        print('Bigramma:', f[0][0], f[0][1], '\tFrequenza:', f[1])
    #con probabilità condizionata massima
    ProbCondLMI2=ProbCondeLMI(BigAggSos2)
    print('I 20 bigrammi aggettivo-sostantivo con probabilità condizionata massima sono:')
    for pcl in ProbCondLMI2:
        for pc in dizPc:
            print('Bigramma:', pc[0][0], pc[0][1], '\tProbabilità condizionata:', pc[1])
    #con la Local Mutual Information maggiore      
    print('I 20 bigrammi aggettivo-sostantivo con Local Mutual Information massima sono:')
    for lm in ProbCondLMI2:
        for l in dizlmi:
            print('Bigramma:', l[0][0], l[0][1], '\tLMI:', l[1])
    #stampo la frase con distribuzione media più alta   
    Distrib2=EstraiFrasi(frasi2, tokens2)
    print('La distribuzione media più alta in una frase è:')
    for d in Distrib2:
        print('Frase:', d[0], '\tDistribuzione:', math.max(d[1]))
     #stampo le frasi con la relativa probabilità calcolata con un modello markoviano di ordine 2       
    Markov2=ProbMarkov2(frasi2, tokens2, trigrammi2)
    print('La probabilita delle frasi calcolata con un modello di Markov di ordine 2 è:')
    for m in Markov2:
        print('Frase:', m[0], '\tProbabilità:', m[1])
    #stampo le i5 NE di nomi propri con frequenza maggiore
    NEtag2=NEtagging(tokensPOS2)
    print('Le 15 NE di nomi propri più frequenti sono:')
    for n in NEtag2:
        print('Entità nominata:', n[0], '\tFrequenza:', n[1])
        
main(sys.argv[1], sys.argv[2])
    
    
    












        

            
    