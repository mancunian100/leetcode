## Collections of techniques and templates of solving leetcode problems

### Java language templates

- priority queue
```

```
- reverse order sort a int array
```
int[] nums = {1, 2, 3};
Integer[] arr = new int[nums.length];
for (int i = 0; i <n; i ++) arr[i] = nums[i];
Arrays.sort(arr, Comparator<Integer>() {
    @Override
    public int compare(Integer n1, Integer n2) {
        return n2 - n1;
    }
});
```

### binary search
- bs template
```

```

### complex situations
- regular expression

### traverse the matrix
- use dx and dy
```
int[] dx = {0, 1, 0, -1};
int[] dy = {1, 0, -1, 0};
int dir = 0;
dir = (dir + 1) % 4;
```