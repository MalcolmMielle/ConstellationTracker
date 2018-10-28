from skyfield.api import load, Topos, Star
from skyfield.data import hipparcos
from matplotlib import pyplot as plt


# Cassiope
Cas = list([(9598, 8886), (8886, 6686), (6686, 4427), (4427, 3179), (3179, 746)])
Leo = list([(57632, 54872), (54872, 54879), (54879, 55642), (55642, 55434), (54879, 51624), (54879, 49583), (49583, 49669), (49583, 47508), (49583, 50583), (50583, 53954), (53954, 54872), (50583, 50335), (50335, 48455), (48455, 46146), ( 46146, 46750), ( 46750, 47908), ( 47908, 48455), (47908, 49583)])
UrsaMajor = list([(67301, 65378), (65378, 62956), (62956, 59774), (59774, 54061), (54061, 53910), (53910, 58001), (58001, 59774), (54061, 46733), (46733, 41704), (41704, 44127), (44127, 44471), (44471, 50801), (50372, 46853), (46853, 48319), (48319, 46733)])

all_constellations = list()
all_constellations.append(Cas)
all_constellations.append(UrsaMajor)
all_constellations.append(Leo)

class Constellations:
    def __init__(self):
        with load.open(hipparcos.URL) as f:
            self.df = hipparcos.load_dataframe(f)
        
        self.planets = load('de421.bsp')
        self.earth = self.planets['earth']
        self.ts = load.timescale()
        self.position = self.earth
    


    def print_constellation(self, constellation):
        for el in constellation:
            
            t = self.ts.now()

            #print(el[0] , " and " , el[1])
            star = Star.from_dataframe(self.df.loc[el[0]])
            star_next = Star.from_dataframe(self.df.loc[el[1] ])

            astrometric_star = self.earth.at(t).observe(star)
            ra_s, dec_s, distance_s = astrometric_star.radec()
            astrometric_star_p = self.earth.at(t).observe(star_next)
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


    def set_position(self, N_gps, W_gps):
        
        self.position = self.earth + Topos(N_gps, W_gps)

    def get_stars_azimut_altitude(self, constellation):
        
        azimut_alt = list()
        
        for el in constellation:
            
            t = self.ts.now()

            #print(el[0] , " and " , el[1])
            star = Star.from_dataframe(self.df.loc[el[0]])
            star_next = Star.from_dataframe(self.df.loc[el[1] ])
            
            astro = self.position.at(t).observe(star)
            astro_next = self.position.at(t).observe(star_next)

            app = astro.apparent()
            app_next = astro_next.apparent()

            alt, az, distance = app.altaz()
            alt_next, az_next, distance_next = app_next.altaz()

            azimut_alt.append( ( (az.dstr().split("deg",1)[0], alt.dstr().split("deg",1)[0]), (az_next.dstr().split("deg",1)[0], alt_next.dstr().split("deg",1)[0]) ) )
            
        return azimut_alt



#print("Key\n", df)
#print(df.loc[slice('magnitude')])



#mask = df[df['hip'].isin(Cas)]
#print(mask)
#for(el in Cas):
#	df

#cas_stars = Star.from_dataframe(df_cas)


