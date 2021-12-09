#include<iostream>
#include<vector>
using namespace std;

void quickSort2(vector<int>& arr, int l, int r){
        if(l >= r) return;
        int i = l, j = r;
        while(i < j){
            while(i < j && arr[i] <= arr[l]) i++;
            while(i < j && arr[j] >= arr[l]) j--;
            swap(arr[i], arr[j]);
        }
        swap(arr[l], arr[i]);
        quickSort2(arr, l, i-1);
        quickSort2(arr, i+1, r);
    }
    
    int partition(vector<int> &nums, int left, int right){
        //if(nums.size() == 1) return 0;
        int temp = nums[left];
        while(left < right){
            while(nums[left] < temp) left++;
            while(nums[right] > temp) right--;
            swap(nums[left], nums[right]);
        }
        nums[left] = temp;
        return left;
    }
    void quickSort(vector<int>& arr, int l, int r) {
        // 子数组长度为 1 时终止递归
        if (l >= r) return;
        // 哨兵划分操作（以 arr[l] 作为基准数）
        int i = l, j = r;
        while (i < j) {
            while (i < j && arr[j] >= arr[l]) j--;
            while (i < j && arr[i] <= arr[l]) i++;
            swap(arr[i], arr[j]);
        }
        swap(arr[i], arr[l]);
        // 递归左（右）子数组执行哨兵划分
        quickSort(arr, l, i - 1);
        quickSort(arr, i + 1, r);
    }
        void quicksort(vector<int> &nums, int left, int right){
        if(left < right){
            int middle = partition(nums, left, right);
            quicksort(nums, left, middle - 1);
            quicksort(nums, middle + 1, right);
        }
    }
int main(){
    vector<int> arr(5,0);
    arr[0] = 2;
    arr[1] = 6;
    arr[2] = 9;
    arr[3] = 1;
    arr[4] = 8;
    quicksort(arr, 0, 4);
    for(int i = 0; i < 5; i++) cout<<arr[i]<<"";
    
}