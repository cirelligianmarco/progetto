"""
Class implementing multiset
Created Nov 2, 2020
Updated Feb 7, 2024
by Giulio Iannello
"""
from copy import deepcopy, copy


class MultiSet(object):

    def __init__(self, elems=[]):
        """
        choose a representation
        """
        self.lista = elems
        self.lista.sort()
        
        pass

    def add(self, e):
        """
        add an element to the multiset

        Parameters
        ----------
        e : any hashable type
            element to be added.

        Returns
        -------
        None.

        """
        self.lista.append(e)
        self.lista.sort()

    def remove(self, e):
        """
        decrease multiplicity of an element if it is > 0

        Parameters
        ----------
        e : any hashable type
            element whose multiplicity must be decreased

        Returns
        -------
        None.

        """
        if e in self.lista:
            self.lista.pop(e)

    def membership_test(self, e):
        """
        returns True if element e has multiplicity > 1

        Parameters
        ----------
        e : any hashable type
            element to be checked.

        Returns
        -------
        Boolean
            if element e has multiplicity > 1

        """
        if self.lista.count(e) >= 1:
            return True
        else:
            return False

    def union(self, ms):
        """
        return the multiset which is the union
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be joined

        Returns
        -------
        new_ms : Multiset
            the union between the object and ms
        """
        l = self.lista + ms.lista
        l.sort()
        new_ms = MultiSet(l)

        return new_ms

    def intersection(self, ms):
        """
        return the multiset which is the itersection
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be intersected

        Returns
        -------
        new_ms : Multiset
            the intersection between the object and ms
        """
        copy_ms = deepcopy(ms)
        l = []
        for element in self.lista:

            if element in copy_ms.lista:

                l.append(element)
                copy_ms.lista.remove(element)

        new_ms = MultiSet(l)

        return new_ms

    def difference(self,ms):
        """
        return the multiset which is the difference
        of the object with multiset ms

        Parameters
        ----------
        ms : Multiset
            multiset to be subtracted

        Returns
        -------
        new_ms : Multiset
            the difference between the object and ms
        """
        new_ms = deepcopy(self)
        for element in ms.lista:
            new_ms.lista.remove(element)
        
        return new_ms
    


if __name__ == "__main__":
    ms1 = MultiSet([1, 1, 2, 4])        # ms1 = { 1, 1, 2,          4       }
    print(ms1.lista)
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3,    4       }
    ms1.add(3)                          # ms1 = { 1, 1, 2,    3, 3, 4       }
    ms1.add(2)                          # ms1 = { 1, 1, 2, 2, 3, 3, 4       }
    print(ms1.lista)
    ms1.remove(1)                       # ms1 = { 1,    2, 2, 3, 3, 4       }
    print(ms1.lista)
    ms2 = ms1.union(MultiSet([4,5]))    # ms2 = { 1,    2, 2, 3, 3, 4, 4, 5 }
    print(ms2.lista)
    ms2.remove(2)                       # ms2 = { 1,    2,    3, 3, 4, 4, 5 }
    print(ms2.lista)
    ms3 = ms1.intersection(ms2)         # ms3 = { 1,    2,    3, 3, 4       }
    print(ms3.lista)
    ms1 = ms1.difference(ms3)           # ms1 = {       2                   }
    print(ms1.lista)                 
    print(ms1.membership_test(2))       # True
    print(ms1.membership_test(5))       # False
    
    print('Fine')