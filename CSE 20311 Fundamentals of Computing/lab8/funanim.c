//Aaron Wang - Fund Comp - Lab 8 - Part 2 bounce.c
//Program plays with rotational motion, shapes and colors
//Right Click to change colors, left click to change shape.

#include "gfx.h"
#include <math.h>
#include <unistd.h>
#include <stdio.h>


int main(){
    int color = 1;
    int shape = 1;
    int rotation = 0;
    const int xsize = 1200, ysize = 720, SIZE = 100;
    int x = 600, y = 360;
    gfx_open(xsize,ysize,"Bounce");
    gfx_color(255,0,0);
    while(1){
        gfx_clear();
        int sides = shape+2;
        for (int i = 0; i < sides; i++){
            int y1 = y+SIZE/2*sin(2.*i*M_PI/sides+rotation/10/M_PI);
            int y2 = y+SIZE/2*sin(2.*(i+1)*M_PI/sides+rotation/10/M_PI);
            int x1 = x+SIZE/2*cos(2.*i*M_PI/sides+rotation/10/M_PI);
            int x2 = x+SIZE/2*cos(2.*(i+1)*M_PI/sides+rotation/10/M_PI);
            gfx_line(x1,y1,x2,y2);
        }
        gfx_flush();
        usleep(1000);
        rotation++;
        if(gfx_event_waiting()){
            char c = gfx_wait();
            if(c == 1){
                shape%=5;
                shape++;
            } else if (c == 3){
                color%=3;
                color++;
                if(color==1){
                    gfx_color(255,0,0);
                } else if(color==2){
                    gfx_color(0,255,0);
                } else if(color==3){
                    gfx_color(0,0,255);
                }
            } else if (c=='q'){
                break;
            }
        }

    }
}