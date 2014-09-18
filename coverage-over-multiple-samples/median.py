import numpy, scipy, sys

def make_dict(files_in):
    l1 = ['DR10', 'DR11', 'DR12', 'DR13', 'DR14', 'DR15', 'DR16', 'DR17', 'DR18', 'DR1', 'DR2', 'DR3', 'DR4', 'DR5', 'DR6', 'DR7', 'DR8', 'DR9', 'DR19', 'DR20', 'DR21', 'DR25', 'DR27', 'DR28', 'DR32', 'DR33', 'DR34', 'DR38', 'DR39', 'DR40', 'DR43', 'DR44', 'DR45', 'DR49', 'DR50', 'DR51', 'DR55', 'DR56', 'DR57', 'DR61', 'DR62', 'DR63', 'DR22', 'DR23', 'DR24', 'DR29', 'DR30', 'DR31', 'DR35', 'DR36', 'DR37', 'DR41', 'DR42', 'DR46', 'DR47', 'DR48', 'DR52', 'DR53', 'DR54', 'DR58', 'DR59', 'DR60', 'DR64', 'DR65', 'DR66']
    l2 = [4909072.5, 3899511.0, 1315021.0, 1724034.0, 4774299.0, 16976965.5, 906243.0, 589110.5, 2334771.5, 1425894.0, 2433858.0, 4113148.5, 1686976.5, 2691444.5, 920561.0, 717234.5, 556729.5, 3423861.0, 3277264.5, 1876815.5, 1962735.5, 2106381.0, 3770352.0, 1975875.0, 727017.5, 740482.0, 844796.0, 4796929.5, 2115645.5, 1710955.0, 829522.5, 876987.0, 796938.0, 837778.0, 336421.0, 1033502.5, 713067.0, 229106.5, 686383.5, 921155.5, 801289.0, 1182281.0, 2271955.5, 2794935.5, 2699946.0, 371886.5, 845510.0, 3370313.5, 2777855.0, 920081.0, 1690050.0, 2139216.0, 1259731.5, 2266955.5, 1214135.0, 190898.5, 282068.5, 744988.0, 2799246.0, 478188.0, 606365.5, 338945.0, 578793.5, 955764.0, 401314.5]
    d_norm = dict(zip(l1, l2))
    d2 = {}
    for f in files_in:
        d = {}
        norm = d_norm[f.split('_')[0]]
        for line in open(f):
            dat = line.rstrip().split(' ')
            id, index, count = dat
            index = int(index)
            if d.has_key(id):
                d[id].append(int(count))
            else:
                d[id] = [int(count)]
        for x in d:
            med = numpy.median(d[x])/norm
            if d2.has_key(x):
                d2[x].append(med)
            else:
                d2[x] = [med]
    return d2

def get_stats(dict):
    for x in dict.keys():
            print x, numpy.average(dict[x]), numpy.std(dict[x])


d = make_dict(sys.argv[1:])
get_stats(d)


