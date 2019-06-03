#include <bits/stdc++.h>
double n = 3.14159;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	double raio;
	
	scanf("%lf", &raio);
	printf("A=%.4lf\n", pow(raio,2) * n);
	
	return 0;
}