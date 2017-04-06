#include <iostream>
#include <iomanip>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
int ans1,ans2;
int q=0;
int w=0;
int u=0;
int x;
int y;
int n1,n2;

void bboard(char board[5][5]){//outputs screen board
 cout<<" ------------"<<endl;
        cout<<"| |1|2|3|4|5|";
        //cout<<"1";
            int linendernum=0;
      for(int y=0;y<5;y++){ //loops that outputs the first board
            cout<<endl;
            cout<<" ------------"<<endl;
             linendernum++;
             cout<<"|";
                cout<<linendernum;
                cout<<"|";
        for(int x=0;x<5;x++){
            cout<<board[x][y];
            cout<<"|";
        }//2nd for loop bracket
      }//for loop bracket
      cout<<endl;
      cout<<" ------------"<<endl;
}
void cboard(char mboard[5][5]){//outputs mboard
     int linendernum2=0;
        cout<<" ------------"<<endl;
        cout<<"| |1|2|3|4|5|";
        //cout<<"1";
      for(int q=0;q<5;q++){ //loops that outputs the board with the dollars
            cout<<endl;
            cout<<" ------------"<<endl;
             linendernum2++;
             cout<<"|";
                cout<<linendernum2;
                cout<<"|";
        for(int w=0;w<5;w++){
            if(mboard[w][q]!='$'){
                mboard[w][q]='#';
            }
            cout<<mboard[w][q];
            cout<<"|";
        }
        }
      cout<<endl;
      cout<<" ------------"<<endl;
}
void randomizer(char mboard[5][5]){//the randomizer for gold
    int gold=0;
    int n1,n2;
    while(gold<10){//-------------------------------------------------------------------------------end of the randomizer loop/beggining of the mboarsd loop
        int n1=rand()%5;
        int n2=rand()%5;
        if(mboard[n1][n2]!='$'){
            mboard[n1][n2]='$';
            gold++;
        }
        }
}
void guessing(char board[5][5],char mboard[5][5]){
    int win=0;
     do{
            cout<<"Enter first coordinate";
            cin>>ans1;
            cout<<"Second cord";
            cin>>ans2;
            if(mboard[ans1-1][ans2-1]=='$'){
                board[ans1-1][ans2-1]='$';
                cout<<"You gone one gold!"<<endl;
                win++;
            }
            else{
                 board[ans1-1][ans2-1]=' ';
                 cout<<"Better luck next time....."<<endl;
                       }
            bboard(board);
     }while(win!=10);
}

int main(){
    srand(time(NULL));
    char board[5][5]={'#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'};
    char mboard[5][5];

    cout<<"Hello, Welcome to TREASURE HUNT!!"<<endl;

    bboard(board);
    randomizer(mboard);
    cboard(mboard);
    guessing(board,mboard);

    cout<<"Nice Job!";

      return 0;
}


// # include<iostream>
//
// using namespace std;
//
// int main()
// {
//     int r=0;
//     int c=0;
//     int counter=0;
//     cin>>r>>c;
//     char a[r][c];
//     for(int i=0; i < r; i++)
//     {
//         for(int j=0; j < c; j++)
//         {
//             a[i][j]=0;
//             cin>>a[i][j];
//             // cout<<"Hi";
//         }
//     }
//     for(int i=0; i < r; i++)
//     {
//         for(int j=0; j < c; j++)
//         {
//             // cout<<a[i][j];
//             if (a[i][j]=='T')
//             {
//                 ++counter;
//                 cout<<counter;
//                 break;
//                 continue;
//             }
//             else if (a[i][j]=='N')
//             {
//                 --i;
//                 ++counter;
//                 continue;
//
//             }
//             else if (a[i][j]=='S')
//             {
//                 ++i;
//                 ++counter;
//                 continue;
//
//             }
//             else if (a[i][j]=='W')
//             {
//                 --j;
//                 ++counter;
//                 continue;
//
//             }
//             else if (a[i][j]=='S')
//             {
//                 ++j;
//                 ++counter;
//                 continue;
//
//             }
//             cout<<i<<j<<"\n";
//
//         }
//     }
//
//
// }
