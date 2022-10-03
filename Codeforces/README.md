# Sublime Text Configuration for CP

![sublimeConfig](https://user-images.githubusercontent.com/99928036/193644598-1e417f45-6e1c-433c-84db-8f45e93b6d12.gif)

### C++11 on Windows
```JSON
{
"cmd": ["g++",  "-Wall", "-Wextra", "-Wshadow", "-Wpedantic", "-O2", "-std=c++11", "${file}", "-o", "test.exe", "&&" , "test.exe<inputf.in>outputf.in"],
"selector":"source.cpp",
"shell":true,
"working_dir":"$file_path"
}

```

### C++14 on Windows
```JSON
{
"cmd": ["g++",  "-Wall", "-Wextra", "-Wshadow", "-Wpedantic", "-O2", "-std=c++14", "${file}", "-o", "test.exe", "&&" , "test.exe<inputf.in>outputf.in"],
"selector":"source.cpp",
"shell":true,
"working_dir":"$file_path"
}

```

### C++11 on Mac
```JSON
{
"cmd": ["g++",  "-Wall", "-Wextra", "-Wshadow", "-Wpedantic", "-fsanitize=undefined", "-fsanitize=address","-O2", "-std=c++11", "${file}", "-o", "test.exe", "&&" , "test.exe<inputf.in>outputf.in"],
"selector":"source.cpp",
"shell":true,
"working_dir":"$file_path"
}

```
