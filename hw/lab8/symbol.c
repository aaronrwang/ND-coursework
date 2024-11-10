//Aaron Wang - Fund Comp - Lab 8 - Part 1 symbol.c
//Practice opening a gfx window, drawing lines and havine user input

#include "gfx.h"
#include <math.h>

#define SIZE 100
#define PI 3.14

void drawSquare(int, int);
void drawTriangle(int, int);
void drawPolygon(int, int, int);

int main(){
    const int xsize = 1200, ysize = 720;
    gfx_open(xsize, ysize, "Symbol");
    while(1){
        char c = gfx_wait();
        int x = gfx_xpos();
        int y = gfx_ypos();

        if(c == 1){
            gfx_color(0,0,255);
            drawSquare(x,y);
        } else if (c == 'c'){
            gfx_color(255,255,255);
            gfx_circle(x, y, SIZE/2);
        } else if (c == 't'){
            gfx_color(0,255,0);
            drawTriangle(x, y);
        } else if (c >= '3' && c <= '9'){
            int sides = c - '0';
            gfx_color(255,0,255);
            drawPolygon(x,y,sides);
        } else if(c == 27){
            gfx_clear();
        } else if(c=='q'){
            break;
        }
    }
}

void drawSquare(int x, int y){
    const int apothem = (SIZE / 2);
    gfx_line((x+apothem), (y+apothem), (x+apothem), (y-apothem));
    gfx_line((x-apothem), (y+apothem), (x-apothem), (y-apothem));
    gfx_line((x+apothem), (y+apothem), (x-apothem), (y+apothem));
    gfx_line((x+apothem), (y-apothem), (x-apothem), (y-apothem));
}

void drawTriangle(int x, int y){
    const int apothem = (SIZE / 2);
    gfx_line((x+apothem), (y+apothem), (x), (y-apothem));
    gfx_line((x-apothem), (y+apothem), (x), (y-apothem));
    gfx_line((x+apothem), (y+apothem), (x-apothem), (y+apothem));
}

void drawPolygon(int x, int y, int sides){
    for (int i = 0; i < sides; i++){
        int y1 = y+SIZE/2*sin(2.*i*PI/sides);
        int y2 = y+SIZE/2*sin(2.*(i+1)*PI/sides);
        int x1 = x+SIZE/2*cos(2.*i*PI/sides);
        int x2 = x+SIZE/2*cos(2.*(i+1)*PI/sides);
        gfx_line(x1,y1,x2,y2);
    }
}