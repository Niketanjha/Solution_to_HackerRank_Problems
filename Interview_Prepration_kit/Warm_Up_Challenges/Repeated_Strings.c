long repeatedString(char* s, long n) {
    long int count_a=0,extra_a=0;
    for(int i=0;i<strlen(s);i++){
        if(s[i]=='a'){
            count_a++;
        }
        if(i<(n%strlen(s)) && s[i]=='a'){
            extra_a++;

        }
    }
    return count_a*(n/strlen(s))+extra_a ;



}
