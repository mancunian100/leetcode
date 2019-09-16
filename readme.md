## Collections of techniques and templates of solving leetcode problems

### Java String manipulation
- String and Integer
```
String s1;
Integer n1;

n1 = Integer.parseInt(s1);

s1 = String.valueOf(n1);
s1 = Integer.toString(n1);
```

- String StringBuilder
```

```

- determine two Strings are equal
```
s1.equals(s2);
```

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
- iterate a hashmap
```
Map<String, Integer> map = new HashMap<>();

for (Entry<String, Integer> entry : map.entrySet()) {
    entry.getKey();
    entry.getValue();
}

for (String key : map.keySet()) {
    map.get(key);
}
```

### binary search
- bs template
```

```

### union find
- union find template
```
List<Integer> father;

public int find(int i) {
    int res = father.get(i);
    if (i != res) {
        res = find(father.get(i));
        father.set(i, res);
    }
    return res;
}

public void connect(int a, int b) {
    if (find(a) != find(b)) {
        father.set(find(b), find(a));
    }
}

public boolean isConnected(int a ,int b) {
    return find(a) == find(b);
}

// initialize
father = new ArrayList<>();
for (int i = 0; i < n; i ++) {
    father.add(i);
}

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