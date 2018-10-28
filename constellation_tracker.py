from skyfield.api import load, Topos, Star
from skyfield.data import hipparcos
import constellations
import motors

def main():
    
    motor_arm = motors.Motor()
    
    constellation = constellations.Constellations()
    #Sofie's flat
    constellation.set_position('59.253141 N', '15.234271 E')
    
    while(True):
        for cons in constellations.all_constellations:
            constellation.print_constellation(cons)
            az_alti = constellation.get_stars_azimut_altitude(cons)
            
            for el in az_alti:
                print(el)
                motor_arm.write_data(el[0], el[1])
            print("DONE ALL")
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
