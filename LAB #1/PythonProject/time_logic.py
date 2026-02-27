y =int(input())

x = y

hours = x // 3600
x %= 3600
print(hours)


minutes = x // 60
x %= 60
print(minutes)

seconds = x

print(seconds)

print(y," Seconds is " , hours," hours, ", minutes," minutes, and ", seconds," seconds " )

