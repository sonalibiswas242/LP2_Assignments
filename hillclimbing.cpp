#include <stdio.h>

#include<iostream>

#include<fstream>

#include<string.h>

using namespace std;

bool check(char **board,int i,int j,int st,int N){

if(st == 1){

if(board[i][j] == 'K'){

return false;

}

for(int k = 0;k<N;k++){

if(board[i][k] == 'Q'){

return false;

}

}

for(int k = 0;k<N;k++){

if(board[k][j] == 'Q'){

return false;

}

}

for(int k = i-1,s = j-1;k >= 0 && s >= 0;k--,s--){

if(board[k][s] == 'Q'){

return false;

}

}

for(int k=i+1,s=j+1;k<N && s<N;k++,s++){

if(board[k][s] == 'Q'){

return false;

}

}

for(int k=i-1,s=j+1;k>=0 && s<N;k--,s++){

if(board[k][s] == 'Q'){

return false;

}

}

for(int k = i+1,s = j-1;k<N && s >= 0;k++,s--){

if(board[k][s] == 'Q'){

return false;

}

}

int k = i;

int s = j;

if( k-2 >= 0){

if(s-1 >= 0){

if(board[k-2][s-1] == 'K'){

return false;

}

}

if(s+1 < N){

if(board[k-2][s+1] == 'K'){

return false;

}

}

}

if( k+2 < N){

if(s-1 >= 0){

if(board[k+2][s-1] == 'K'){

return false;

}

}

if(s+1 < N){

if(board[k+2][s+1] == 'K'){

return false;

}

}

}

if( s-2 >= 0){

if(k-1 >= 0){

if(board[k-1][s-2] == 'K'){

return false;

}

}

if(k+1 < N){

if(board[k+1][s-2] == 'K'){

return false;

}

}

}

if( s+2 < N){

if(k-1 >= 0){

if(board[k-1][s+2] == 'K'){

return false;

}

}

if(k+1 < N){

if(board[k+1][s+2] == 'K'){

return false;

}

}

}

}

if(st == 2){

if(board[i][j] == 'Q'){

return false;

}

int k = i;

int s = j;

if( k-2 >= 0){

if(s-1 >= 0){

if(board[k-2][s-1] == 'K'){

return false;

}

}

if(s+1 < N){

if(board[k-2][s+1] == 'K'){

return false;

}

}

}

if( k+2 < N){

if(s-1 >= 0){

if(board[k+2][s-1] == 'K'){

return false;

}

}

if(s+1 < N){

if(board[k+2][s+1] == 'K'){

return false;

}

}

}

if( s-2 >= 0){

if(k-1 >= 0){

if(board[k-1][s-2] == 'K'){

return false;

}

}

if(k+1 < N){

if(board[k+1][s-2] == 'K'){

return false;

}

}

}

if( s+2 < N){

if(k-1 >= 0){

if(board[k-1][s+2] == 'K'){

return false;

}

}

if(k+1 < N){

if(board[k+1][s+2] == 'K'){

return false;

}

}

}

}

return true;

}

void initializeBoard(char **board,int Q,int K,int N){

for(int i = 0;i<N;i++){

for(int j = 0;j<N;j++){

board[i][j] = ' ';

}

}

for(int i = 0;i<N;i++){

for(int j = 0;j<N;j++){

if(Q > 0){

if(check(board,i,j,1,N)){

board[i][j] = 'Q';

Q--;

}

}

if(K > 0){

if(check(board,i,j,2,N)){

board[i][j] = 'K';

K--;

}

}

if(Q == 0 && K == 0){

break;

}

}

}

}

void printBoard(char **Board,int N){

cout<<endl;

for(int i =0;i<N;i++){

for(int j = 0;j<N;j++){

cout<<"|"<<Board[i][j];

}

cout<<"|"<<endl;

}

}

int main(){

int N;

int Q;

int K;

int tmax;

std::cout << "Value of N: "; cin >> N; cout << endl;

if (cin.fail())

{

std::cout << "Please enter integer only & try again. Thanks!" << endl;

exit(0);

}

else if (N < 4)

{

std::cout << " No possible solution. Please try again for n > 4.";

exit(0);

}

std::cout << "Value of Q: "; cin >> Q; cout << endl;

if (cin.fail())

if (cin.fail())

{

std::cout << "Please enter integer only & try again. Thanks!" << endl;

exit(0);

}

else if (Q < 1)

{

std::cout << " No possible solution. Please try again for Q > 1.";

exit(0);

}

std::cout << "Value of K: "; cin >> K; cout << endl;

if (cin.fail())

if (cin.fail())

{

std::cout << "Please enter integer only & try again. Thanks!" << endl;

exit(0);

}

else if (K < 1)

{

std::cout << " No possible solution. Please try again for K > 1.";

exit(0);

}

char **board = new char*[N];

for(int i = 0;i<N;i++){

board[i] = new char[N];

}

initializeBoard(board,Q,K,N);

printBoard(board,N);

return 0;

}