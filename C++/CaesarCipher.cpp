#include <iostream>
#include <cctype>
#include <string>

using namespace std;

/*
    Caesar Cipher solution

    Sample Input:
    11
    middle-Outz
    2

    Sample Output
    okffng-Qwvb
*/

int main(){
	int T, k;
	string s;

	cin>>T>>s>>k;
	if((T >= 1 && T <= 100)&&(k >= 0 && k <= 100)){
		for(int i=0;i<T;i++){
		if(isalpha(s.at(i))){
			int c = (int)s.at(i);

			if(c >= 65 && c <= 90 ){
				c += k%26;
				if(c>90) cout<<(char)(c%90+64);
				else cout<<(char)c;
			}
			else if(c >= 97 && c <= 122){
				c+= k%26;
				if(c>122) cout<<(char)(c%122+96);
				else cout<<(char)c;
			}
		}
		else cout<<s.at(i);
		}
		cout <<endl;
	}

	return 0;
}