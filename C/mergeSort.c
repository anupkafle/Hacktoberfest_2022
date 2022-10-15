#include<stdio.h>

void merge(int arr[], int left, int mid, int right){
	int l_size = mid-left+1;
	int r_size = right-mid;
	
	int l[l_size], r[r_size];
	
	for (int i = 0; i < l_size; i++){
		l[i] = arr[left+i];
	}
	for (int i = 0; i < r_size; i++){
		r[i] = arr[mid+i+1];
	}
	
	int i = 0, j = 0, k = left;
	
	while (i < l_size && j < r_size){
		if (l[i] < r[j]){
			arr[k] = l[i];
			i++;
		}else{
			arr[k] = r[j];
			j++;
		}
		k++;
	}
	
	while (i < l_size){
		arr[k] = l[i];
		i++;
		k++;
	}
	
	while (j < r_size){
		arr[k] = r[j];
		j++;
		k++;
	}
}

void mergeSort(int arr[], int left, int right){
	if (left < right){
		int mid = (left+right)/2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid+1, right);
	
		merge(arr, left, mid, right);
	}
}

int main(){
	
	int size = 0;
	printf("Enter size of array: ");
	scanf("%d", &size);
	
	int arr[size];
	printf("Enter elements: \n");
	
	for (int i = 0; i < size; i++){
		scanf("%d", &arr[i]);
	}
	
	printf("Initial Array :-\n");
	
	for (int i = 0; i < size; i++){
		printf("%d ", arr[i]);
	}
	
	mergeSort(arr, 0, size-1);
	
	printf("\nSorted array:-\n");
	
	for (int i = 0; i < size; i++){
		printf("%d ", arr[i]);
	}
	return 0;
}

