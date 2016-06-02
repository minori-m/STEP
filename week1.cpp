#include <iostream>
#include <stdio.h>
#include <string.h>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

// sort function

int int_sort(const void *a,const void *b){
    return strcmp((char *)a,(char *)b);
}

int main()
{
    ifstream ifs("words");
    char str[30];
    char words[235886][30];
    
    char input[16];
    int i=0;
    int j;
    int k=0;
    
    /*file open error*/
    if (ifs.fail()) {
        cout    <<"failure"<<endl;
        return -1;
    }
    
    /*get words from dictionary to char words*/
    while (ifs.getline(str,29)) {
        for (j=0; j<30; j++) {
            words[i][j]=tolower(str[j]);
        }
        i=i+1;
    }
    
    /*sort each word from dictionary*/
    
    for (j=0; j<235886; j++) {
        qsort(words[j],strlen(words[j]),sizeof(char),int_sort);
    }

    /*get 16 words*/
    cout<<"Input 16 words."<<endl;
    cin>>input;
    
    /*input error*/
    if (strlen(input)<16) {
        cout<<"# of words is not enough."<<endl;
        return -1;
    }
    
    /*sort input*/
    qsort(input,16,sizeof(char),int_sort);
//    for (i=0; i<16; i++) {
//        cout<<input[i];
//    }
    cout<<endl;
    
    /*compare*/
    int m=0,l=0;
    char max[100][30];
    int num[100];
    for (i=0; i<235886; i++) {
        j=0;
        k=0;
        while ((strcmp(&words[i][j],&input[k])>=0||words[i][j]==input[k])&&j<strlen(words[i])+1&&k<16) {
            if (words[i][j]==input[k]) {
                j++;
                k++;
            }
            else{
                k++;
            }
        }
        if (j==strlen(words[i])) {
            if (strlen(words[i])>m) {
                m=strlen(words[i]);
                l=0;
                num[l]=i;
            }
            else if(strlen(words[i])==m){
                l=l+1;
                num[l]=i;
            }
        }
    }

    
    /*get unsorted words from dictionary to char words*/
    i=0;
    ifs.clear();
    ifs.seekg(0);
    while (ifs.getline(str,29)) {
        for (j=0; j<30; j++) {
            words[i][j]=str[j];
        }
        i=i+1;
    }
    
    /*display result*/
    cout<<"result ->"<<endl;
    for (i=0; i<sizeof(num)/sizeof(int); i++) {
        if (strlen(words[num[i]])==m) {
            cout<<words[num[i]]<<endl;
        }
    }
    
    
    return 0;
}

