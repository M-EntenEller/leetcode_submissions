// https://leetcode.com/problems/design-parking-system




typedef struct {
    int big;
    int medium;
    int small;    
} ParkingSystem;


ParkingSystem* parkingSystemCreate(int big, int medium, int small) {
    
    ParkingSystem* ps = (ParkingSystem*) malloc(sizeof(ParkingSystem));
    ps->big = big;
    ps->medium = medium;
    ps->small = small;
    return ps;

}

bool parkingSystemAddCar(ParkingSystem* obj, int carType) {
  
    switch (carType){
        case 1: 
            return --obj->big >= 0;
        case 2:
            return --obj->medium >= 0;
        case 3:
            return --obj->small >= 0;
    }

    return 0;

}

void parkingSystemFree(ParkingSystem* obj) {
    
    free(obj);

}

/**
 * Your ParkingSystem struct will be instantiated and called as such:
 * ParkingSystem* obj = parkingSystemCreate(big, medium, small);
 * bool param_1 = parkingSystemAddCar(obj, carType);
 
 * parkingSystemFree(obj);
*/