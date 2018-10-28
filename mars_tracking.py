from skyfield.api import load, Topos, Star
from skyfield.data import hipparcos


def print_constellation(constellation):
    for el in constellation:

        #print(el[0] , " and " , el[1])
        star = Star.from_dataframe(df.loc[el[0]])
        star_prev = Star.from_dataframe(df.loc[el[1] ])

        astrometric_star = earth.at(t).observe(star)
        ra_s, dec_s, distance_s = astrometric_star.radec()
        astrometric_star_p = earth.at(t).observe(star_prev)
        ra_s_p, dec_s_p, distance_s_p = astrometric_star_p.radec()

        hours_s = list()
        hours_s.append(ra_s.hours)
        hours_s.append(ra_s_p.hours)
        deg_s = list()
        deg_s.append(dec_s.degrees)
        deg_s.append(dec_s_p.degrees)
        #print(hours_s[0], " and " , deg_s[0])
        #print(hours_s[1], " and " , deg_s[1])

        plt.plot(hours_s, deg_s, 'bo-', linewidth=2)
        #plt.scatter(ra.hours, dec.degrees, 8 - df['magnitude'], 'k')


    plt.show()



planets = load('de421.bsp')
earth, mars = planets['earth'], planets['mars']

ts = load.timescale()
t = ts.now()
print("time ", t.utc)
position = earth.at(t).observe(mars)
ra, dec, distance = position.radec()

print(ra)
print(dec)
print(distance)

# Need to calculate the position from the GPS to the center of the earth (moon + earth gravitationnal system)

 # Altitude and azimuth in the sky of a
# specific geographic location

boston = earth + Topos('42.3583 N', '71.0603 W')
astro = boston.at(ts.utc(1980, 3, 1)).observe(mars)
app = astro.apparent()

alt, az, distance = app.altaz()
print(alt.dstr())
print(az.dstr())
print(distance)


# Measure a star


with load.open(hipparcos.URL) as f:
	df = hipparcos.load_dataframe(f)

barnards_star = Star.from_dataframe(df.loc[87937])

planets = load('de421.bsp')
earth = planets['earth'] 

ts = load.timescale()
t = ts.now()
astrometric = boston.at(t).observe(barnards_star)
app_b = astrometric.apparent()

alt_b, az_b, distance_b = app_b.altaz()
print("Bernard star")
print(alt_b.dstr())
print(az_b.dstr())
print(distance)


#print(df)


#df = df[df['magnitude'] <= 2.5]
#print('After filtering, there are {} stars'.format(len(df)))
#bright_stars = Star.from_dataframe(df)

t = ts.utc(2018, 9, 3)
#astrometric = earth.at(t).observe(bright_stars)
#ra, dec, distance = astrometric.radec()

#print('There are {} right ascensions'.format(len(ra.hours)))
#print('and {} declinations'.format(len(dec.degrees)))
from matplotlib import pyplot as plt
#plt.scatter(ra.hours, dec.degrees, 8 - df['magnitude'], 'k')
#plt.xlim(7.0, 4.0)
#plt.ylim(-20, 20)
#plt.savefig('bright_stars.png')


# Cassiope
Cas = list([(9598, 8886), (8886, 6686), (6686, 4427), (4427, 3179), (3179, 746)])
Leo = list([(57632, 54872), (54872, 54879), (54879, 55642), (55642, 55434), (54879, 51624), (54879, 49583), (49583, 49669), (49583, 47508), (49583, 50583), (50583, 53954), (53954, 54872), (50583, 50335), (50335, 48455), (48455, 46146), ( 46146, 46750), ( 46750, 47908), ( 47908, 48455), (47908, 49583)])

constellation = list()
constellation.append(Cas)
constellation.append(Leo)

for cons in constellation:
    print_constellation(cons)

#print("Key\n", df)
#print(df.loc[slice('magnitude')])



#mask = df[df['hip'].isin(Cas)]
#print(mask)
#for(el in Cas):
#	df

#cas_stars = Star.from_dataframe(df_cas)

