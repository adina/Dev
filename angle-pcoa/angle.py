import math, sys

def angle(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    inner_product = x1*x2 + y1*y2
    len1 = (x1**2 + y1**2)**.5
    len2 = (x2**2 + y2**2)**.5
    if len1 == 0 or len2 == 0:
        return float(0)
    else:
        dot = math.acos(inner_product/(len1*len2))
        return dot

def calculate(pt1, pt2):
    ang = angle(pt1, pt2)*180/math.pi
    return ang

def make_coord_dict(file):
    d = {}
    for n, line in enumerate(open(file)):
        if n > 0:
            dat = line.rstrip().split('\t')
            d[dat[0]] = (float(dat[1]), float(dat[2]))
    return d

env_file = sys.argv[1]
sites_file = sys.argv[2]
species_file = sys.argv[3]

d_env = make_coord_dict(env_file)
d_sites = make_coord_dict(sites_file)
d_species = make_coord_dict(species_file)

threshold = float(15)

f_outenv = open(sys.argv[2] + '.bestfit', 'w')
f_outspecies = open(sys.argv[3] + '.bestfit', 'w')

for key1 in d_env:
    p1 = d_env[key1]
    for key2 in d_species:
        p2 = d_species[key2]
        angle1 = calculate(p1, p2)
        angle2 = 180 - angle1
        if angle1 < threshold or angle2 < threshold:
            if angle1 != 0.0:
                l = [key1, key2, str(angle1)]
                f_outspecies.write('%s\n' % '\t'.join(l))

for key1 in d_env:
    p1 = d_env[key1]
    for key2 in d_sites:
        p2 = d_sites[key2]
        angle1 = calculate(p1, p2)
        angle2 = 180 - angle1
        if angle1 < threshold or angle2 < threshold:
            if angle1 != 0.0:
                l = [key1, key2, str(angle1)]
                f_outenv.write('%s\n' % '\t'.join(l))



