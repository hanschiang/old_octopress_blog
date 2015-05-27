---
layout: post
title: "部落格同步測試3"
date: 2015-05-28 02:55:23 +0800
comments: true
categories: 
---

### 圖片測試

- 基本上剛剛測試過markdown。竟然算是還蠻好地同步過去了。
- 接下來測試貼圖和snippet。其實我很少用到snippet就是了，畢竟不是本業寫程式的。

圖片測試：

![測試圖片](https://c2.staticflickr.com/4/3922/14440553019_53a80f10d5.jpg)



### Snippet測試

很老套地貼一下費布那西數列：


```
r = raw_input("N=?")
a = int(r)

def f(n): # This function tells nth Fibonacci number
    if n == 1:
        return 0

    elif n == 2:
         return 1

    else:
        return f(n-1) + f(n-2)

print f(a)
```

