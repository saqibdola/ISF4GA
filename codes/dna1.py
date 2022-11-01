LEUL = ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']
PHEF = ['TTT', 'TTC']
SERS= ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC']
TYRY = ['TAT', 'TAC']
STOP = ['TAA', 'TAG', 'TGA']
CYSC = ['TGT', 'TGC']
PROP = ['CCT', 'CCC', 'CCA', 'CCG']
HISH = ['CAT', 'CAC']
GINQ = ['CAA', 'CAG']
ARGR = ['CGT', 'CGC', 'CGA', 'CGG', 'AGA','AGG']
IIEI = ['ATT', 'ATC', 'ATA']
THRT =['ACT', 'ACC', 'ACA', 'ACG']
ASNN = ['AAT', 'AAC']
LYSK = ['AAA', 'AAG']
VALV = ['GTT', 'GTC', 'GTA', 'GTG']
ALAA = ['GCT', 'GCC', 'GCA', 'GCG']
ASPD = ['GAT', 'GAC']
GIUE = ['GAA', 'GAG']
GIYG = ['GGT', 'GGC', 'GGA', 'GGG']
TRPW = ['TGG']
METM = ['ATG']

def checking(asdf, asdfg):

    if asdf in LEUL and asdfg in LEUL:
        print('PNC')
    elif asdf in PHEF and asdfg in PHEF:
        print('PNC')
    elif asdf in SERS and asdfg in SERS:
        print('PNC')
    elif asdf in TYRY and asdfg in TYRY:
        print('PNC')
    elif asdf in STOP and asdfg in STOP:
        print('PNC')
    elif asdf in CYSC and asdfg in CYSC:
        print('PNC')
    elif asdf in PROP and asdfg in PROP:
        print('PNC')
    elif asdf in HISH and asdfg in HISH:
        print('PNC')
    elif asdf in GINQ and asdfg in GINQ:
        print('PNC')
    elif asdf in ARGR and asdfg in ARGR:
        print('PNC')
    elif asdf in IIEI and asdfg in IIEI:
        print('PNC')
    elif asdf in THRT and asdfg in THRT:
        print('PNC')
    elif asdf in ASNN and asdfg in ASNN:
        print('PNC')
    elif asdf in LYSK and asdfg in LYSK:
        print('PNC')
    elif asdf in VALV and asdfg in VALV:
        print('PNC')
    elif asdf in ALAA and asdfg in ALAA:
        print('PNC')
    elif asdf in ASPD and asdfg in ASPD:
        print('PNC')
    elif asdf in GIUE and asdfg in GIUE:
        print('PNC')
    elif asdf in GIYG and asdfg in GIYG:
        print('PNC')
    else:
        print('PROPtien is changed')
        if asdf in LEUL and asdfg in PHEF:
            print('LEUL (L) is changes to PHEF')
        elif asdf in LEUL and asdfg in SERS:
            print('LEUL is changes to SERS')
        elif asdf in LEUL and asdfg in TYRY:
            print('LEUL is changes to TYRY')
        elif asdf in LEUL and asdfg in STOP:
            print('LEUL is changes to STOP')
        elif asdf in LEUL and asdfg in CYSC:
            print('LEUL is changes to CYSC')
        elif asdf in LEUL and asdfg in PROP:
            print('LEUL is changes to PROP')
        elif asdf in LEUL and asdfg in HISH:
            print('LEUL is changes to HISH')
        elif asdf in LEUL and asdfg in GINQ:
            print('LEUL is changes to GINQ')
        elif asdf in LEUL and asdfg in ARGR:
            print('LEUL is changes to ARGR')
        elif asdf in LEUL and asdfg in IIEI:
            print('LEUL is changes to IIEI')
        elif asdf in LEUL and asdfg in THRT:
            print('LEUL is changes to THRT')
        elif asdf in LEUL and asdfg in ASNN:
            print('LEUL is changes to ASNN')
        elif asdf in LEUL and asdfg in LYSK:
            print('LEUL is changes to LYSK')
        elif asdf in LEUL and asdfg in VALV:
            print('LEUL is changes to VALV')
        elif asdf in LEUL and asdfg in ALAA:
            print('LEUL is changes to ALAA')
        elif asdf in LEUL and asdfg in ASPD:
            print('LEUL is changes to ASPD')
        elif asdf in LEUL and asdfg in GIUE:
            print('LEUL is changes to GIUE')
        elif asdf in LEUL and asdfg in GIYG:
            print('LEUL is changes to GIYG')
        elif asdf in LEUL and asdfg in TRPW:
            print('LEUL is changes to TRPW')
        elif asdf in LEUL and asdfg in METM:
            print('LEUL is changes to METM')


        elif asdf in PHEF and asdfg in LEUL:
            print('PHEF is changes to LEUL')
        elif asdf in PHEF and asdfg in SERS:
            print('PHEF is changes to SERS')
        elif asdf in PHEF and asdfg in TYRY:
            print('PHEF is changes to TYRY')
        elif asdf in PHEF and asdfg in STOP:
            print('PHEF is changes to STOP')
        elif asdf in PHEF and asdfg in CYSC:
            print('PHEF is changes to CYSC')
        elif asdf in PHEF and asdfg in PROP:
            print('PHEF is changes to PROP')
        elif asdf in PHEF and asdfg in HISH:
            print('PHEF is changes to HISH')
        elif asdf in PHEF and asdfg in GINQ:
            print('PHEF is changes to GINQ')
        elif asdf in PHEF and asdfg in ARGR:
            print('PHEF is changes to ARGR')
        elif asdf in PHEF and asdfg in IIEI:
            print('PHEF is changes to IIEI')
        elif asdf in PHEF and asdfg in THRT:
            print('PHEF is changes to THRT')
        elif asdf in PHEF and asdfg in ASNN:
            print('PHEF is changes to ASNN')
        elif asdf in PHEF and asdfg in LYSK:
            print('PHEF is changes to LYSK')
        elif asdf in PHEF and asdfg in VALV:
            print('PHEF is changes to VALV')
        elif asdf in PHEF and asdfg in ALAA:
            print('PHEF is changes to ALAA')
        elif asdf in PHEF and asdfg in ASPD:
            print('PHEF is changes to ASPD')
        elif asdf in PHEF and asdfg in GIUE:
            print('PHEF is changes to GIUE')
        elif asdf in PHEF and asdfg in GIYG:
            print('PHEF is changes to GIYG')
        elif asdf in PHEF and asdfg in TRPW:
            print('PHEF is changes to TRPW')
        elif asdf in PHEF and asdfg in METM:
            print('PHEF is changes to METM')


        elif asdf in SERS and asdfg in LEUL:
            print('SERS is changes to LEUL')
        elif asdf in SERS and asdfg in PHEF:
            print('SERS is changes to PHEF')
        elif asdf in SERS and asdfg in TYRY:
            print('SERS is changes to TYRY')
        elif asdf in SERS and asdfg in STOP:
            print('SERS is changes to STOP')
        elif asdf in SERS and asdfg in CYSC:
            print('SERS is changes to CYSC')
        elif asdf in SERS and asdfg in PROP:
            print('SERS is changes to PROP')
        elif asdf in SERS and asdfg in HISH:
            print('SERS is changes to HISH')
        elif asdf in SERS and asdfg in GINQ:
            print('SERS is changes to GINQ')
        elif asdf in SERS and asdfg in ARGR:
            print('SERS is changes to ARGR')
        elif asdf in SERS and asdfg in IIEI:
            print('SERS is changes to IIEI')
        elif asdf in SERS and asdfg in THRT:
            print('SERS is changes to THRT')
        elif asdf in SERS and asdfg in ASNN:
            print('SERS is changes to ASNN')
        elif asdf in SERS and asdfg in LYSK:
            print('SERS is changes to LYSK')
        elif asdf in SERS and asdfg in VALV:
            print('SERS is changes to VALV')
        elif asdf in SERS and asdfg in ALAA:
            print('SERS is changes to ALAA')
        elif asdf in SERS and asdfg in ASPD:
            print('SERS is changes to ASPD')
        elif asdf in SERS and asdfg in GIUE:
            print('SERS is changes to GIUE')
        elif asdf in SERS and asdfg in GIYG:
            print('SERS is changes to GIYG')
        elif asdf in SERS and asdfg in TRPW:
            print('SERS is changes to TRPW')
        elif asdf in SERS and asdfg in METM:
            print('SERS is changes to METM')


        elif asdf in TYRY and asdfg in LEUL:
            print('TYRY is changes to LEUL')
        elif asdf in TYRY and asdfg in PHEF:
            print('TYRY is changes to PHEF')
        elif asdf in TYRY and asdfg in SERS:
            print('TYRY is changes to SERS')
        elif asdf in TYRY and asdfg in STOP:
            print('TYRY is changes to STOP')
        elif asdf in TYRY and asdfg in CYSC:
            print('TYRY is changes to CYSC')
        elif asdf in TYRY and asdfg in PROP:
            print('TYRY is changes to PROP')
        elif asdf in TYRY and asdfg in HISH:
            print('TYRY is changes to HISH')
        elif asdf in TYRY and asdfg in GINQ:
            print('TYRY is changes to GINQ')
        elif asdf in TYRY and asdfg in ARGR:
            print('TYRY is changes to ARGR')
        elif asdf in TYRY and asdfg in IIEI:
            print('TYRY is changes to IIEI')
        elif asdf in TYRY and asdfg in THRT:
            print('TYRY is changes to THRT')
        elif asdf in TYRY and asdfg in ASNN:
            print('TYRY is changes to ASNN')
        elif asdf in TYRY and asdfg in LYSK:
            print('TYRY is changes to LYSK')
        elif asdf in TYRY and asdfg in VALV:
            print('TYRY is changes to VALV')
        elif asdf in TYRY and asdfg in ALAA:
            print('TYRY is changes to ALAA')
        elif asdf in TYRY and asdfg in ASPD:
            print('TYRY is changes to ASPD')
        elif asdf in TYRY and asdfg in GIUE:
            print('TYRY is changes to GIUE')
        elif asdf in TYRY and asdfg in GIYG:
            print('TYRY is changes to GIYG')
        elif asdf in TYRY and asdfg in TRPW:
            print('TYRY is changes to TRPW')
        elif asdf in TYRY and asdfg in METM:
            print('TYRY is changes to METM')


        elif asdf in STOP and asdfg in LEUL:
            print('STOP is changes to LEUL')
        elif asdf in STOP and asdfg in PHEF:
            print('STOP is changes to PHEF')
        elif asdf in STOP and asdfg in SERS:
            print('STOP is changes to SERS')
        elif asdf in STOP and asdfg in TYRY:
            print('STOP is changes to TYRY')
        elif asdf in STOP and asdfg in CYSC:
            print('STOP is changes to CYSC')
        elif asdf in STOP and asdfg in PROP:
            print('STOP is changes to PROP')
        elif asdf in STOP and asdfg in HISH:
            print('STOP is changes to HISH')
        elif asdf in STOP and asdfg in GINQ:
            print('STOP is changes to GINQ')
        elif asdf in STOP and asdfg in ARGR:
            print('STOP is changes to ARGR')
        elif asdf in STOP and asdfg in IIEI:
            print('STOP is changes to IIEI')
        elif asdf in STOP and asdfg in THRT:
            print('STOP is changes to THRT')
        elif asdf in STOP and asdfg in ASNN:
            print('STOP is changes to ASNN')
        elif asdf in STOP and asdfg in LYSK:
            print('STOP is changes to LYSK')
        elif asdf in STOP and asdfg in VALV:
            print('STOP is changes to VALV')
        elif asdf in STOP and asdfg in ALAA:
            print('STOP is changes to ALAA')
        elif asdf in STOP and asdfg in ASPD:
            print('STOP is changes to ASPD')
        elif asdf in STOP and asdfg in GIUE:
            print('STOP is changes to GIUE')
        elif asdf in STOP and asdfg in GIYG:
            print('STOP is changes to GIYG')
        elif asdf in STOP and asdfg in TRPW:
            print('STOP is changes to TRPW')
        elif asdf in STOP and asdfg in METM:
            print('STOP is changes to METM')


        elif asdf in CYSC and asdfg in LEUL:
            print('CYSC is changes to LEUL')
        elif asdf in CYSC and asdfg in PHEF:
            print('CYSC is changes to PHEF')
        elif asdf in CYSC and asdfg in SERS:
            print('CYSC is changes to SERS')
        elif asdf in CYSC and asdfg in TYRY:
            print('CYSC is changes to TYRY')
        elif asdf in CYSC and asdfg in STOP:
            print('CYSC is changes to STOP')
        elif asdf in CYSC and asdfg in PROP:
            print('CYSC is changes to PROP')
        elif asdf in CYSC and asdfg in HISH:
            print('CYSC is changes to HISH')
        elif asdf in CYSC and asdfg in GINQ:
            print('CYSC is changes to GINQ')
        elif asdf in CYSC and asdfg in ARGR:
            print('CYSC is changes to ARGR')
        elif asdf in CYSC and asdfg in IIEI:
            print('CYSC is changes to IIEI')
        elif asdf in CYSC and asdfg in THRT:
            print('CYSC is changes to THRT')
        elif asdf in CYSC and asdfg in ASNN:
            print('CYSC is changes to ASNN')
        elif asdf in CYSC and asdfg in LYSK:
            print('CYSC is changes to LYSK')
        elif asdf in CYSC and asdfg in VALV:
            print('CYSC is changes to VALV')
        elif asdf in CYSC and asdfg in ALAA:
            print('CYSC is changes to ALAA')
        elif asdf in CYSC and asdfg in ASPD:
            print('CYSC is changes to ASPD')
        elif asdf in CYSC and asdfg in GIUE:
            print('CYSC is changes to GIUE')
        elif asdf in CYSC and asdfg in GIYG:
            print('CYSC is changes to GIYG')
        elif asdf in CYSC and asdfg in TRPW:
            print('CYSC is changes to TRPW')
        elif asdf in CYSC and asdfg in METM:
            print('CYSC is changes to METM')


        elif asdf in PROP and asdfg in LEUL:
            print('PROP is changes to LEUL')
        elif asdf in PROP and asdfg in PHEF:
            print('PROP is changes to PHEF')
        elif asdf in PROP and asdfg in SERS:
            print('PROP is changes to SERS')
        elif asdf in PROP and asdfg in TYRY:
            print('PROP is changes to TYRY')
        elif asdf in PROP and asdfg in STOP:
            print('PROP is changes to STOP')
        elif asdf in PROP and asdfg in CYSC:
            print('PROP is changes to CYSC')
        elif asdf in PROP and asdfg in HISH:
            print('PROP is changes to HISH')
        elif asdf in PROP and asdfg in GINQ:
            print('PROP is changes to GINQ')
        elif asdf in PROP and asdfg in ARGR:
            print('PROP is changes to ARGR')
        elif asdf in PROP and asdfg in IIEI:
            print('PROP is changes to IIEI')
        elif asdf in PROP and asdfg in THRT:
            print('PROP is changes to THRT')
        elif asdf in PROP and asdfg in ASNN:
            print('PROP is changes to ASNN')
        elif asdf in PROP and asdfg in LYSK:
            print('PROP is changes to LYSK')
        elif asdf in PROP and asdfg in VALV:
            print('PROP is changes to VALV')
        elif asdf in PROP and asdfg in ALAA:
            print('PROP is changes to ALAA')
        elif asdf in PROP and asdfg in ASPD:
            print('PROP is changes to ASPD')
        elif asdf in PROP and asdfg in GIUE:
            print('PROP is changes to GIUE')
        elif asdf in PROP and asdfg in GIYG:
            print('PROP is changes to GIYG')
        elif asdf in PROP and asdfg in TRPW:
            print('PROP is changes to TRPW')
        elif asdf in PROP and asdfg in METM:
            print('PROP is changes to METM')


        elif asdf in HISH and asdfg in LEUL:
            print('HISH is changes to LEUL')
        elif asdf in HISH and asdfg in PHEF:
            print('HISH is changes to PHEF')
        elif asdf in HISH and asdfg in SERS:
            print('HISH is changes to SERS')
        elif asdf in HISH and asdfg in TYRY:
            print('HISH is changes to TYRY')
        elif asdf in HISH and asdfg in STOP:
            print('HISH is changes to STOP')
        elif asdf in HISH and asdfg in CYSC:
            print('HISH is changes to CYSC')
        elif asdf in HISH and asdfg in PROP:
            print('HISH is changes to PROP')
        elif asdf in HISH and asdfg in GINQ:
            print('HISH is changes to GINQ')
        elif asdf in HISH and asdfg in ARGR:
            print('HISH is changes to ARGR')
        elif asdf in HISH and asdfg in IIEI:
            print('HISH is changes to IIEI')
        elif asdf in HISH and asdfg in THRT:
            print('HISH is changes to THRT')
        elif asdf in HISH and asdfg in ASNN:
            print('HISH is changes to ASNN')
        elif asdf in HISH and asdfg in LYSK:
            print('HISH is changes to LYSK')
        elif asdf in HISH and asdfg in VALV:
            print('HISH is changes to VALV')
        elif asdf in HISH and asdfg in ALAA:
            print('HISH is changes to ALAA')
        elif asdf in HISH and asdfg in ASPD:
            print('HISH is changes to ASPD')
        elif asdf in HISH and asdfg in GIUE:
            print('HISH is changes to GIUE')
        elif asdf in HISH and asdfg in GIYG:
            print('HISH is changes to GIYG')
        elif asdf in HISH and asdfg in TRPW:
            print('HISH is changes to TRPW')
        elif asdf in HISH and asdfg in METM:
            print('HISH is changes to METM')


        elif asdf in GINQ and asdfg in LEUL:
            print('GINQ is changes to LEUL')
        elif asdf in GINQ and asdfg in PHEF:
            print('GINQ is changes to PHEF')
        elif asdf in GINQ and asdfg in SERS:
            print('GINQ is changes to SERS')
        elif asdf in GINQ and asdfg in TYRY:
            print('GINQ is changes to TYRY')
        elif asdf in GINQ and asdfg in STOP:
            print('GINQ is changes to STOP')
        elif asdf in GINQ and asdfg in PROP:
            print('GINQ is changes to PROP')
        elif asdf in GINQ and asdfg in HISH:
            print('GINQ is changes to HISH')
        elif asdf in GINQ and asdfg in ASPD:
            print('GINQ is changes to ASPD')
        elif asdf in GINQ and asdfg in ARGR:
            print('GINQ is changes to ARGR')
        elif asdf in GINQ and asdfg in IIEI:
            print('GINQ is changes to IIEI')
        elif asdf in GINQ and asdfg in THRT:
            print('GINQ is changes to THRT')
        elif asdf in GINQ and asdfg in ASNN:
            print('GINQ is changes to ASNN')
        elif asdf in GINQ and asdfg in LYSK:
            print('GINQ is changes to LYSK')
        elif asdf in GINQ and asdfg in VALV:
            print('GINQ is changes to VALV')
        elif asdf in GINQ and asdfg in ALAA:
            print('GINQ is changes to ALAA')
        elif asdf in GINQ and asdfg in ASPD:
            print('GINQ is changes to ASPD')
        elif asdf in GINQ and asdfg in GIUE:
            print('GINQ is changes to GIUE')
        elif asdf in GINQ and asdfg in GIYG:
            print('GINQ is changes to GIYG')
        elif asdf in GINQ and asdfg in TRPW:
            print('GINQ is changes to TRPW')
        elif asdf in GINQ and asdfg in METM:
            print('GINQ is changes to METM')


        elif asdf in ARGR and asdfg in LEUL:
            print('ARGR is changes to LEUL')
        elif asdf in ARGR and asdfg in PHEF:
            print('ARGR is changes to PHEF')
        elif asdf in ARGR and asdfg in SERS:
            print('ARGR is changes to SERS')
        elif asdf in ARGR and asdfg in TYRY:
            print('ARGR is changes to TYRY')
        elif asdf in ARGR and asdfg in STOP:
            print('ARGR is changes to STOP')
        elif asdf in ARGR and asdfg in CYSC:
            print('ARGR is changes to CYSC')
        elif asdf in ARGR and asdfg in PROP:
            print('ARGR is changes to PROP')
        elif asdf in ARGR and asdfg in HISH:
            print('ARGR is changes to HISH')
        elif asdf in ARGR and asdfg in GINQ:
            print('ARGR is changes to GINQ')
        elif asdf in ARGR and asdfg in IIEI:
            print('ARGR is changes to IIEI')
        elif asdf in ARGR and asdfg in THRT:
            print('ARGR is changes to THRT')
        elif asdf in ARGR and asdfg in ASNN:
            print('ARGR is changes to ASNN')
        elif asdf in ARGR and asdfg in LYSK:
            print('ARGR is changes to LYSK')
        elif asdf in ARGR and asdfg in VALV:
            print('ARGR is changes to VALV')
        elif asdf in ARGR and asdfg in ALAA:
            print('ARGR is changes to ALAA')
        elif asdf in ARGR and asdfg in ASPD:
            print('ARGR is changes to ASPD')
        elif asdf in ARGR and asdfg in GIUE:
            print('ARGR is changes to GIUE')
        elif asdf in ARGR and asdfg in GIYG:
            print('ARGR is changes to GIYG')
        elif asdf in ARGR and asdfg in TRPW:
            print('ARGR is changes to TRPW')
        elif asdf in ARGR and asdfg in METM:
            print('ARGR is changes to METM')


        elif asdf in IIEI and asdfg in LEUL:
            print('IIEI is changes to LEUL')
        elif asdf in IIEI and asdfg in PHEF:
            print('IIEI is changes to PHEF')
        elif asdf in IIEI and asdfg in SERS:
            print('IIEI is changes to SERS')
        elif asdf in IIEI and asdfg in TYRY:
            print('IIEI is changes to TYRY')
        elif asdf in IIEI and asdfg in STOP:
            print('IIEI is changes to STOP')
        elif asdf in IIEI and asdfg in CYSC:
            print('IIEI is changes to CYSC')
        elif asdf in IIEI and asdfg in PROP:
            print('IIEI is changes to PROP')
        elif asdf in IIEI and asdfg in HISH:
            print('IIEI is changes to HISH')
        elif asdf in IIEI and asdfg in GINQ:
            print('IIEI is changes to GINQ')
        elif asdf in IIEI and asdfg in ARGR:
            print('IIEI is changes to ARGR')
        elif asdf in IIEI and asdfg in THRT:
            print('IIEI is changes to THRT')
        elif asdf in IIEI and asdfg in ASNN:
            print('IIEI is changes to ASNN')
        elif asdf in IIEI and asdfg in LYSK:
            print('IIEI is changes to LYSK')
        elif asdf in IIEI and asdfg in VALV:
            print('IIEI is changes to VALV')
        elif asdf in IIEI and asdfg in ALAA:
            print('IIEI is changes to ALAA')
        elif asdf in IIEI and asdfg in ASPD:
            print('IIEI is changes to ASPD')
        elif asdf in IIEI and asdfg in GIUE:
            print('IIEI is changes to GIUE')
        elif asdf in IIEI and asdfg in GIYG:
            print('IIEI is changes to GIYG')
        elif asdf in IIEI and asdfg in TRPW:
            print('IIEI is changes to TRPW')
        elif asdf in IIEI and asdfg in METM:
            print('IIEI is changes to METM')


        elif asdf in THRT and asdfg in LEUL:
            print('THRT is changes to LEUL')
        elif asdf in THRT and asdfg in PHEF:
            print('THRT is changes to PHEF')
        elif asdf in THRT and asdfg in SERS:
            print('THRT is changes to SERS')
        elif asdf in THRT and asdfg in TYRY:
            print('THRT is changes to TYRY')
        elif asdf in THRT and asdfg in STOP:
            print('THRT is changes to STOP')
        elif asdf in THRT and asdfg in CYSC:
            print('THRT is changes to CYSC')
        elif asdf in THRT and asdfg in PROP:
            print('THRT is changes to PROP')
        elif asdf in THRT and asdfg in HISH:
            print('THRT is changes to HISH')
        elif asdf in THRT and asdfg in GINQ:
            print('THRT is changes to GINQ')
        elif asdf in THRT and asdfg in ARGR:
            print('THRT is changes to ARGR')
        elif asdf in THRT and asdfg in IIEI:
            print('THRT is changes to IIEI')
        elif asdf in THRT and asdfg in ASNN:
            print('THRT is changes to ASNN')
        elif asdf in THRT and asdfg in LYSK:
            print('THRT is changes to LYSK')
        elif asdf in THRT and asdfg in VALV:
            print('THRT is changes to VALV')
        elif asdf in THRT and asdfg in ALAA:
            print('THRT is changes to ALAA')
        elif asdf in THRT and asdfg in ASPD:
            print('THRT is changes to ASPD')
        elif asdf in THRT and asdfg in GIUE:
            print('THRT is changes to GIUE')
        elif asdf in THRT and asdfg in GIYG:
            print('THRT is changes to GIYG')
        elif asdf in THRT and asdfg in TRPW:
            print('THRT is changes to TRPW')
        elif asdf in THRT and asdfg in METM:
            print('THRT is changes to METM')


        elif asdf in ASNN and asdfg in LEUL:
            print('ASNN is changes to LEUL')
        elif asdf in ASNN and asdfg in PHEF:
            print('ASNN is changes to PHEF')
        elif asdf in ASNN and asdfg in SERS:
            print('ASNN is changes to SERS')
        elif asdf in ASNN and asdfg in TYRY:
            print('ASNN is changes to TYRY')
        elif asdf in ASNN and asdfg in STOP:
            print('ASNN is changes to STOP')
        elif asdf in ASNN and asdfg in CYSC:
            print('ASNN is changes to CYSC')
        elif asdf in ASNN and asdfg in PROP:
            print('ASNN is changes to PROP')
        elif asdf in ASNN and asdfg in HISH:
            print('ASNN is changes to HISH')
        elif asdf in ASNN and asdfg in GINQ:
            print('ASNN is changes to GINQ')
        elif asdf in ASNN and asdfg in ARGR:
            print('ASNN is changes to ARGR')
        elif asdf in ASNN and asdfg in IIEI:
            print('ASNN is changes to IIEI')
        elif asdf in ASNN and asdfg in THRT:
            print('ASNN is changes to THRT')
        elif asdf in ASNN and asdfg in LYSK:
            print('ASNN is changes to LYSK')
        elif asdf in ASNN and asdfg in VALV:
            print('ASNN is changes to VALV')
        elif asdf in ASNN and asdfg in ALAA:
            print('ASNN is changes to ALAA')
        elif asdf in ASNN and asdfg in ASPD:
            print('ASNN is changes to ASPD')
        elif asdf in ASNN and asdfg in GIUE:
            print('ASNN is changes to GIUE')
        elif asdf in ASNN and asdfg in GIYG:
            print('ASNN is changes to GIYG')
        elif asdf in ASNN and asdfg in TRPW:
            print('ASNN is changes to TRPW')
        elif asdf in ASNN and asdfg in METM:
            print('ASNN is changes to METM')

        elif asdf in LYSK and asdfg in PHEF:
            print('LYSK is changes to PHEF')
        elif asdf in LYSK and asdfg in SERS:
            print('LYSK is changes to SERS')
        elif asdf in LYSK and asdfg in TYRY:
            print('LYSK is changes to TYRY')
        elif asdf in LYSK and asdfg in STOP:
            print('LYSK is changes to STOP')
        elif asdf in LYSK and asdfg in CYSC:
            print('LYSK is changes to CYSC')
        elif asdf in LYSK and asdfg in PROP:
            print('LYSK is changes to PROP')
        elif asdf in LYSK and asdfg in HISH:
            print('LYSK is changes to HISH')
        elif asdf in LYSK and asdfg in GINQ:
            print('LYSK is changes to GINQ')
        elif asdf in LYSK and asdfg in ARGR:
            print('LYSK is changes to ARGR')
        elif asdf in LYSK and asdfg in IIEI:
            print('LYSK is changes to IIEI')
        elif asdf in LYSK and asdfg in THRT:
            print('LYSK is changes to THRT')
        elif asdf in LYSK and asdfg in ASNN:
            print('LYSK is changes to ASNN')
        elif asdf in LYSK and asdfg in LEUL:
            print('LYSK is changes to LEUL')
        elif asdf in LYSK and asdfg in VALV:
            print('LYSK is changes to VALV')
        elif asdf in LYSK and asdfg in ALAA:
            print('LYSK is changes to ALAA')
        elif asdf in LYSK and asdfg in ASPD:
            print('LYSK is changes to ASPD')
        elif asdf in LYSK and asdfg in GIUE:
            print('LYSK is changes to GIUE')
        elif asdf in LYSK and asdfg in GIYG:
            print('LYSK is changes to GIYG')
        elif asdf in LYSK and asdfg in TRPW:
            print('LYSK is changes to TRPW')
        elif asdf in LYSK and asdfg in METM:
            print('LYSK is changes to METM')

        elif asdf in VALV and asdfg in PHEF:
            print('VALV is changes to PHEF')
        elif asdf in VALV and asdfg in SERS:
            print('VALV is changes to SERS')
        elif asdf in VALV and asdfg in TYRY:
            print('VALV is changes to TYRY')
        elif asdf in VALV and asdfg in STOP:
            print('VALV is changes to STOP')
        elif asdf in VALV and asdfg in CYSC:
            print('VALV is changes to CYSC')
        elif asdf in VALV and asdfg in PROP:
            print('VALV is changes to PROP')
        elif asdf in VALV and asdfg in HISH:
            print('VALV is changes to HISH')
        elif asdf in VALV and asdfg in GINQ:
            print('VALV is changes to GINQ')
        elif asdf in VALV and asdfg in ARGR:
            print('VALV is changes to ARGR')
        elif asdf in VALV and asdfg in IIEI:
            print('VALV is changes to IIEI')
        elif asdf in VALV and asdfg in THRT:
            print('VALV is changes to THRT')
        elif asdf in VALV and asdfg in ASNN:
            print('VALV is changes to ASNN')
        elif asdf in VALV and asdfg in LEUL:
            print('VALV is changes to LEUL')
        elif asdf in VALV and asdfg in LYSK:
            print('VALV is changes to LYSK')
        elif asdf in VALV and asdfg in ALAA:
            print('VALV is changes to ALAA')
        elif asdf in VALV and asdfg in ASPD:
            print('VALV is changes to ASPD')
        elif asdf in VALV and asdfg in GIUE:
            print('VALV is changes to GIUE')
        elif asdf in VALV and asdfg in GIYG:
            print('VALV is changes to GIYG')
        elif asdf in VALV and asdfg in TRPW:
            print('VALV is changes to TRPW')
        elif asdf in VALV and asdfg in METM:
            print('VALV is changes to METM')

        elif asdf in ALAA and asdfg in PHEF:
            print('ALAA is changes to PHEF')
        elif asdf in ALAA and asdfg in SERS:
            print('ALAA is changes to SERS')
        elif asdf in ALAA and asdfg in TYRY:
            print('ALAA is changes to TYRY')
        elif asdf in ALAA and asdfg in STOP:
            print('ALAA is changes to STOP')
        elif asdf in ALAA and asdfg in CYSC:
            print('ALAA is changes to CYSC')
        elif asdf in ALAA and asdfg in PROP:
            print('ALAA is changes to PROP')
        elif asdf in ALAA and asdfg in HISH:
            print('ALAA is changes to HISH')
        elif asdf in ALAA and asdfg in GINQ:
            print('ALAA is changes to GINQ')
        elif asdf in ALAA and asdfg in ARGR:
            print('ALAA is changes to ARGR')
        elif asdf in ALAA and asdfg in IIEI:
            print('ALAA is changes to IIEI')
        elif asdf in ALAA and asdfg in THRT:
            print('ALAA is changes to THRT')
        elif asdf in ALAA and asdfg in ASNN:
            print('ALAA is changes to ASNN')
        elif asdf in ALAA and asdfg in LEUL:
            print('ALAA is changes to LEUL')
        elif asdf in ALAA and asdfg in LYSK:
            print('ALAA is changes to LYSK')
        elif asdf in ALAA and asdfg in VALV:
            print('ALAA is changes to VALV')
        elif asdf in ALAA and asdfg in ASPD:
            print('ALAA is changes to ASPD')
        elif asdf in ALAA and asdfg in GIUE:
            print('ALAA is changes to GIUE')
        elif asdf in ALAA and asdfg in GIYG:
            print('ALAA is changes to GIYG')
        elif asdf in ALAA and asdfg in TRPW:
            print('ALAA is changes to TRPW')
        elif asdf in ALAA and asdfg in METM:
            print('ALAA is changes to METM')

        elif asdf in ASPD and asdfg in PHEF:
            print('ASPD is changes to PHEF')
        elif asdf in ASPD and asdfg in SERS:
            print('ASPD is changes to SERS')
        elif asdf in ASPD and asdfg in TYRY:
            print('ASPD is changes to TYRY')
        elif asdf in ASPD and asdfg in STOP:
            print('ASPD is changes to STOP')
        elif asdf in ASPD and asdfg in CYSC:
            print('ASPD is changes to CYSC')
        elif asdf in ASPD and asdfg in PROP:
            print('ASPD is changes to PROP')
        elif asdf in ASPD and asdfg in HISH:
            print('ASPD is changes to HISH')
        elif asdf in ASPD and asdfg in GINQ:
            print('ASPD is changes to GINQ')
        elif asdf in ASPD and asdfg in ARGR:
            print('ASPD is changes to ARGR')
        elif asdf in ASPD and asdfg in IIEI:
            print('ASPD is changes to IIEI')
        elif asdf in ASPD and asdfg in THRT:
            print('ASPD is changes to THRT')
        elif asdf in ASPD and asdfg in ASNN:
            print('ASPD is changes to ASNN')
        elif asdf in ASPD and asdfg in LEUL:
            print('ASPD is changes to LEUL')
        elif asdf in ASPD and asdfg in LYSK:
            print('ASPD is changes to LYSK')
        elif asdf in ASPD and asdfg in VALV:
            print('ASPD is changes to VALV')
        elif asdf in ASPD and asdfg in ALAA:
            print('ASPD is changes to ALAA')
        elif asdf in ASPD and asdfg in GIUE:
            print('ASPD is changes to GIUE')
        elif asdf in ASPD and asdfg in GIYG:
            print('ASPD is changes to GIYG')
        elif asdf in ASPD and asdfg in TRPW:
            print('ASPD is changes to TRPW')
        elif asdf in ASPD and asdfg in METM:
            print('ASPD is changes to METM')

        elif asdf in GIUE and asdfg in PHEF:
            print('GIUE is changes to PHEF')
        elif asdf in GIUE and asdfg in SERS:
            print('GIUE is changes to SERS')
        elif asdf in GIUE and asdfg in TYRY:
            print('GIUE is changes to TYRY')
        elif asdf in GIUE and asdfg in STOP:
            print('GIUE is changes to STOP')
        elif asdf in GIUE and asdfg in CYSC:
            print('GIUE is changes to CYSC')
        elif asdf in GIUE and asdfg in PROP:
            print('GIUE is changes to PROP')
        elif asdf in GIUE and asdfg in HISH:
            print('GIUE is changes to HISH')
        elif asdf in GIUE and asdfg in GINQ:
            print('GIUE is changes to GINQ')
        elif asdf in GIUE and asdfg in ARGR:
            print('GIUE is changes to ARGR')
        elif asdf in GIUE and asdfg in IIEI:
            print('GIUE is changes to IIEI')
        elif asdf in GIUE and asdfg in THRT:
            print('GIUE is changes to THRT')
        elif asdf in GIUE and asdfg in ASNN:
            print('GIUE is changes to ASNN')
        elif asdf in GIUE and asdfg in LEUL:
            print('GIUE is changes to LEUL')
        elif asdf in GIUE and asdfg in LYSK:
            print('GIUE is changes to LYSK')
        elif asdf in GIUE and asdfg in VALV:
            print('GIUE is changes to VALV')
        elif asdf in GIUE and asdfg in ALAA:
            print('GIUE is changes to ALAA')
        elif asdf in GIUE and asdfg in ASPD:
            print('GIUE is changes to ASPD')
        elif asdf in GIUE and asdfg in GIYG:
            print('GIUE is changes to GIYG')
        elif asdf in GIUE and asdfg in TRPW:
            print('GIUE is changes to TRPW')
        elif asdf in GIUE and asdfg in METM:
            print('GIUE is changes to METM')

        elif asdf in GIYG and asdfg in PHEF:
            print('GIYG is changes to PHEF')
        elif asdf in GIYG and asdfg in SERS:
            print('GIYG is changes to SERS')
        elif asdf in GIYG and asdfg in TYRY:
            print('GIYG is changes to TYRY')
        elif asdf in GIYG and asdfg in STOP:
            print('GIYG is changes to STOP')
        elif asdf in GIYG and asdfg in CYSC:
            print('GIYG is changes to CYSC')
        elif asdf in GIYG and asdfg in PROP:
            print('GIYG is changes to PROP')
        elif asdf in GIYG and asdfg in HISH:
            print('GIYG is changes to HISH')
        elif asdf in GIYG and asdfg in GINQ:
            print('GIYG is changes to GINQ')
        elif asdf in GIYG and asdfg in ARGR:
            print('GIYG is changes to ARGR')
        elif asdf in GIYG and asdfg in IIEI:
            print('GIYG is changes to IIEI')
        elif asdf in GIYG and asdfg in THRT:
            print('GIYG is changes to THRT')
        elif asdf in GIYG and asdfg in ASNN:
            print('GIYG is changes to ASNN')
        elif asdf in GIYG and asdfg in LEUL:
            print('GIYG is changes to LEUL')
        elif asdf in GIYG and asdfg in LYSK:
            print('GIYG is changes to LYSK')
        elif asdf in GIYG and asdfg in VALV:
            print('GIYG is changes to VALV')
        elif asdf in GIYG and asdfg in ALAA:
            print('GIYG is changes to ALAA')
        elif asdf in GIYG and asdfg in ASPD:
            print('GIYG is changes to ASPD')
        elif asdf in GIYG and asdfg in GIUE:
            print('GIYG is changes to GIUE')
        elif asdf in GIYG and asdfg in TRPW:
            print('GIYG is changes to TRPW')
        elif asdf in GIYG and asdfg in METM:
            print('GIYG is changes to METM')

        elif asdf in TRPW and asdfg in PHEF:
            print('TRPW is changes to PHEF')
        elif asdf in TRPW and asdfg in SERS:
            print('TRPW is changes to SERS')
        elif asdf in TRPW and asdfg in TYRY:
            print('TRPW is changes to TYRY')
        elif asdf in TRPW and asdfg in STOP:
            print('TRPW is changes to STOP')
        elif asdf in TRPW and asdfg in CYSC:
            print('TRPW is changes to CYSC')
        elif asdf in TRPW and asdfg in PROP:
            print('TRPW is changes to PROP')
        elif asdf in TRPW and asdfg in HISH:
            print('TRPW is changes to HISH')
        elif asdf in TRPW and asdfg in GINQ:
            print('TRPW is changes to GINQ')
        elif asdf in TRPW and asdfg in ARGR:
            print('TRPW is changes to ARGR')
        elif asdf in TRPW and asdfg in IIEI:
            print('TRPW is changes to IIEI')
        elif asdf in TRPW and asdfg in THRT:
            print('TRPW is changes to THRT')
        elif asdf in TRPW and asdfg in ASNN:
            print('TRPW is changes to ASNN')
        elif asdf in TRPW and asdfg in LEUL:
            print('TRPW is changes to LEUL')
        elif asdf in TRPW and asdfg in LYSK:
            print('TRPW is changes to LYSK')
        elif asdf in TRPW and asdfg in VALV:
            print('TRPW is changes to VALV')
        elif asdf in TRPW and asdfg in ALAA:
            print('TRPW is changes to ALAA')
        elif asdf in TRPW and asdfg in ASPD:
            print('TRPW is changes to ASPD')
        elif asdf in TRPW and asdfg in GIUE:
            print('TRPW is changes to GIUE')
        elif asdf in TRPW and asdfg in GIYG:
            print('TRPW is changes to GIYG')
        elif asdf in TRPW and asdfg in METM:
            print('TRPW is changes to METM')

        elif asdf in METM and asdfg in PHEF:
            print('METM is changes to PHEF')
        elif asdf in METM and asdfg in SERS:
            print('METM is changes to SERS')
        elif asdf in METM and asdfg in TYRY:
            print('METM is changes to TYRY')
        elif asdf in METM and asdfg in STOP:
            print('METM is changes to STOP')
        elif asdf in METM and asdfg in CYSC:
            print('METM is changes to CYSC')
        elif asdf in METM and asdfg in PROP:
            print('METM is changes to PROP')
        elif asdf in METM and asdfg in HISH:
            print('METM is changes to HISH')
        elif asdf in METM and asdfg in GINQ:
            print('METM is changes to GINQ')
        elif asdf in METM and asdfg in ARGR:
            print('METM is changes to ARGR')
        elif asdf in METM and asdfg in IIEI:
            print('METM is changes to IIEI')
        elif asdf in METM and asdfg in THRT:
            print('METM is changes to THRT')
        elif asdf in METM and asdfg in ASNN:
            print('METM is changes to ASNN')
        elif asdf in METM and asdfg in LEUL:
            print('METM is changes to LEUL')
        elif asdf in METM and asdfg in LYSK:
            print('METM is changes to LYSK')
        elif asdf in METM and asdfg in VALV:
            print('METM is changes to VALV')
        elif asdf in METM and asdfg in ALAA:
            print('METM is changes to ALAA')
        elif asdf in METM and asdfg in ASPD:
            print('METM is changes to ASPD')
        elif asdf in METM and asdfg in GIUE:
            print('METM is changes to GIUE')
        elif asdf in METM and asdfg in GIYG:
            print('METM is changes to GIYG')
        elif asdf in METM and asdfg in TRPW:
            print('METM is changes to TRPW')

