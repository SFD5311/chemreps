import numpy as np


class Molecule:
    """
    Class to store molecule information
    Data Structures:
    ---------------
    n_atom : int
        number of atoms
    xyz : float
        xyz coordinates. Size: (n_atom,3)
    sym :  string
        List of atomic symbol. Size: (n_atom,1)
    at_num :
        List of atomic numbers. Size: (n_atom,1)
    """
    __nuc = {'H': 1, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9,
             'P': 15, 'S': 16, 'Cl': 17, 'Se': 34, 'Br': 35, 'I': 53}

    def __init__(self):
        return None

    def sym2num(self, sym):
        """
        Given a chemical symbol, returns the atomic number defined within the class
        Parameters:
        -----------
        sym : string
                chemical symbol
        Returns:
        --------
        at_num : int
            atomic number for symbol argument
        """
        try:
            atomic_number = Molecule.__nuc['{}'.format(sym)]
            return atomic_number
        except:
            print('{} is not defined.'.format(sym))

    def import_file(self, fname):
        ftype = fname.split('.')[1]
        if ftype == 'xyz':
            self.import_xyz(fname)
        if ftype == 'sdf' or ftype == 'mol':
            self.import_sdf(fname)

    def import_xyz(self, fname):
        """
        Imports xyz file as with Molecule class instance
        Parameters:
        -----------
        fname : string
            xyz filename
        """
        with open(fname) as f:
            lines = f.readlines()
        self.n_atom = int(lines[0].split()[0])

        # reading lines to build up class data
        self.sym = []
        self.at_num = []
        self.xyz = np.zeros((self.n_atom, 3))
        for i, line in enumerate(lines[2:]):
            tmp = line.split()
            self.sym.append(tmp[0])
            self.at_num.append(self.sym2num(tmp[0]))
            self.xyz[i, 0] = float(tmp[1])
            self.xyz[i, 1] = float(tmp[2])
            self.xyz[i, 2] = float(tmp[3])

    def import_sdf(self, fname):
        """
        Imports xyz file as with Molecule class instance
        Parameters:
        -----------
            fname : string
                sdf or mol file name
        """
        with open(fname) as f:
            lines = f.readlines()
        print(lines[1])
        self.n_atom = int(lines[3].split()[0])
        print(self.n_atom)
        self.sym = []
        self.at_num = []
        self.xyz = np.zeros((self.n_atom, 3))
        for i, line in enumerate(lines[4:4+self.n_atom]):
            tmp = line.split()
            self.sym.append(tmp[3])
            self.at_num.append(self.sym2num(tmp[3]))
            self.xyz[i, 0] = float(tmp[0])
            self.xyz[i, 1] = float(tmp[1])
            self.xyz[i, 2] = float(tmp[2])