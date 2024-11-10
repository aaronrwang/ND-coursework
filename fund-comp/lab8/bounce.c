//Aaron Wang - Fund Comp - Lab 8 - Part 2 bounce.c
//Program includes a ball that can be moved and bounces off the walls

#include "gfx.h"
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <time.h>
#define PI 3.14
#define SIZE 20

int main(){
    srand(time(NULL));
    const int xsize = 1200, ysize = 720;
    double x = 600, y = 360;
    double dx = (rand()%200-100)/100.;
    double dy = (rand()%200-100)/100.;

    gfx_open(xsize,ysize,"Bounce");
    gfx_color(255,255,255);
    while(1){
        gfx_clear();
        gfx_circle((int)x,(int)y,SIZE);
        gfx_flush();
        usleep(500);

        //Check for hitting wall
        if (x+dx+SIZE>xsize || x+dx-SIZE<0){
            dx*=(-1);
        } else if (y+dy+SIZE>ysize || y+dy-SIZE<0){
            dy*=(-1);
        }
        x+=dx;
        y+=dy;

        //check for mouse click or q for quit
        if(gfx_event_waiting()){
            char c = gfx_wait();
            if(c==1){
                x = (double) gfx_xpos();
                y = (double) gfx_ypos();
                dx = (rand()%200-100)/100.;
                dy = (rand()%200-100)/100.;
            } else if (c == 'q'){
                break;
            }
        }
    }
}