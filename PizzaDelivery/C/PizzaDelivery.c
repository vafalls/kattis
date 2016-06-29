#include<stdio.h>
#include<stdlib.h>

struct coordinate {
    unsigned int x;
    unsigned int y;
    unsigned int val;
};

int main() {
    unsigned int nrOfTestCases, dist, nrOfColumns, nrOfRows, currShortWay, nrOfNum, nrOfNum2, TRYVERT=0;
    scanf("%d", &nrOfTestCases);

    for(unsigned int i=nrOfTestCases; i--;){//testcase
        
        scanf("%d %d", &nrOfColumns, &nrOfRows);
        nrOfNum2 = nrOfRows*nrOfColumns;
        nrOfNum = nrOfNum2-1;
        struct coordinate town[nrOfNum2];

        for(unsigned int x=nrOfRows; x--;){//creating town
            for(unsigned int y=nrOfColumns; y--;){
                scanf("%d", &town[nrOfNum].val);
                town[nrOfNum].x=x;
                town[nrOfNum].y=y;
                nrOfNum--;
            }
        }

        currShortWay = 2147483647;
        for(int i=nrOfNum2; i--;){//location
            dist=0;
            for(int j=nrOfNum2; j--;){//to be compared
                if(town[j].val != 0){
                    dist += town[j].val*(abs(town[j].x-town[i].x)+abs(town[j].y-town[i].y));
                }
            }
            
            if(dist < currShortWay){
                currShortWay = dist;
                TRYVERT = 0;
            } else if(i-nrOfColumns+2 >= 0 && TRYVERT==0){//try vertical instead
                i = i-nrOfColumns+2;
                TRYVERT = 1;
            } else {
                break;
            }
        }
        
        printf("%d blocks\n", currShortWay);
    }
}
