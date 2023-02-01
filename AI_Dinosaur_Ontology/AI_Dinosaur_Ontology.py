from owlready2 import *

onto_path.append("C:/Users/Simov/source/repos/AI_Dinosaur_Ontology/AI_Dinosaur_Ontology")
dinosaur_onto = get_ontology("http://test.org/dinosaur_onto.owl")


###DINOSAUR ONTOLOGY PYTHON 3 OWLREADY2 IMPLEMENTATION
###The code below is work in progress and only creates the class hierarchy
###TODO: Add properties and instances and save ontology locally

#Simplified family tree of Dinosauria based on the Saurischia model

#ROOT
class Dinosauria(Thing):
    namespace = dinosaur_onto


#ROOT of Left Subtree
class Ornithischia(Dinosauria):
    pass

#ROOT of Right Subtree of Ornithischia
class Heterodontosauridae(Ornithischia):
    pass

#ROOT of Left Subtree of Ornithischia
class Saphornithischia(Ornithischia):
    pass

class Genasauria(Saphornithischia):
    pass

class Thyreophora(Genasauria):
    pass

class Stegosauria(Thyreophora):
    pass

class Ankylosauria(Thyreophora):
    pass

class Nodosauridae(Ankylosauria):
    pass

class Nodosaurinae(Nodosauridae):
    pass

class Neornithischia(Genasauria):
    pass

class Cerapoda(Neornithischia):
    pass

class Ornithopoda(Cerapoda):
    pass

class Marginocephalia(Cerapoda):
    pass

class Iguanodontia(Ornithopoda):
    pass

class Pachycephalosauria(Marginocephalia):
    pass

class Ceratopsia(Marginocephalia):
    pass




#ROOT of Right Subtree
class Saurischia(Dinosauria):
    pass

#ROOT of Left Subtree of Saurischia
class Herrasauria(Saurischia):
    pass

#ROOT of Right Subtree of Saurischia
class Eusaurischia(Saurischia):
    pass

#ROOT of Left Subtree of Eusaurischia
class Sauropodomorpha(Eusaurischia):
    pass

class Prosauropoda(Sauropodomorpha):
    pass

class Sauropoda(Sauropodomorpha):
    pass

#ROOT of main Subtree of Sauropoda
class Eusauropoda(Sauropoda):
    pass

#ROOT of Left Subtree of Eusauropoda
class Mamenchisauridae(Eusauropoda):
    pass

#ROOT of Right Subtree of Eusauropoda
class Neosauropoda(Eusauropoda):
    pass

class Diplodocoidea(Neosauropoda):
    pass

class Rebbachisauridae(Diplodocoidea):
    pass

class Dicraeosauridae(Diplodocoidea):
    pass

class Diplodocidae(Diplodocoidea):
    pass

class Macronaria(Neosauropoda):
    pass

class Titanosauriformes(Macronaria):
    pass

class Titanosauria(Titanosauriformes):
    pass

class Saltasauridae(Titanosauria):
    pass

class Theropoda(Eusaurischia):
    pass

#ROOT of Right Subtree of Theropoda
class Neotheropoda(Theropoda):
    pass

class Coelophysoidea(Neotheropoda):
    pass

class Dilophosauridae(Neotheropoda):
    pass

class Averostra(Neotheropoda):
    pass

class Ceratosauria(Averostra):
    pass

class Tetanurae(Averostra):
    pass

class Megalosauroidea(Tetanurae):
    pass

class Avetheropoda(Tetanurae):
    pass

class Allosauroidea(Avetheropoda):
    pass

class Coelurosauria(Avetheropoda):
    pass

class Tyrannosauroidea(Coelurosauria):
    pass

class Compsognathidae(Coelurosauria):
    pass

#ROOT of Right-most Subtree of Coelurosauria
class Maniraptoriformes(Coelurosauria):
    pass

class Ornithomimosauria(Maniraptoriformes):
    pass

class Maniraptora(Maniraptoriformes):
    pass

class Alvarezsauria(Maniraptora):
    pass

class Therizinosauria(Maniraptora):
    pass

class Pennaraptora(Maniraptora):
    pass

class Oviraptorosauria(Pennaraptora):
    pass

class Paraves(Pennaraptora):
    pass

class Scansoriopterygidae(Paraves):
    pass

class Eosinopteryx(Paraves):
    pass

class Eumaniraptora(Paraves):
    pass

class Dromaeosauridae(Eumaniraptora):
    pass

class Averaptora(Eumaniraptora):
    pass

class Troodontidae(Averaptora):
    pass

#Clade containing the only living modern dinosaurs, the birds
class Avialae(Averaptora):
    pass


