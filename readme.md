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
String s1;
StringBuilder sb;

sb = new StringBuilder(s1);

sb.charAt(i);

sb.toString();

sb.append(s);
```

- determine two Strings are equal
```
s1.equals(s2);

```
- Arrays
```
// fill
int[] nums = new int[n];
Arrays.fill(nums, 1);

// sort, ascending order
Arrays.sort(nums);
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

for (Map.Entry<String, Integer> entry : map.entrySet()) {
    entry.getKey();
    entry.getValue();
}

for (String key : map.keySet()) {
    map.get(key);
}
```
- List and array convert
```
List<int[]> arr = new ArrayList<>();
int[][] n = (int[][]) arr.toArray(new int[arr.size()][]);

int[] nums = new int[n];
List<Integer> list = Arrays.asList(nums);
```


### binary search
- bs template
```
// in left part, find the right end if left part
while (l < r) {
    int mid = l + r >> 1;
    if (check(mid)) r = mid;
    else l = mid + 1;
}
// in right part, find the left end of right part
while (l < r) {
    int mid = l + r + 1 >> 1;
    if (check(mid)) l = mid;
    else r = mid - 1;
}
```

### bfs
- use queue to store the layer
```
LinkedList<Integer> q = new LinkedList<>();

// add
q.addLast();

// get
q.removeFirst();
```

### bfs & dfs
- bfs
1. large memory
2. without stack overflow
3. can solve shortest, smallest

- dfs
1. linear memory
2. maybe stack overflow
3. cannot solve shortest, smallest

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

// count the number of parts
public int count() {
    int res = 0;
    for (int i = 0; i < father.size(); i ++) {
        if (i == father.get(i)) res ++;
    }
    return res;
}

// initialize
father = new ArrayList<>();
for (int i = 0; i < n; i ++) {
    father.add(i);
}

```

### complex situations
- regular expression

- whether a string is a number

### traverse the matrix
- use dx and dy
```
int[] dx = {0, 1, 0, -1};
int[] dy = {1, 0, -1, 0};
int dir = 0;
dir = (dir + 1) % 4;
```

### pay attention
- while loop check boundary
```
while (l < r && check())

while (i < nums.length && check())
```
