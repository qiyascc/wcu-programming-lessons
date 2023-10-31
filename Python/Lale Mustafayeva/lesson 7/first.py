# Funksiyaların məqsədi kod təkrarını aradan qaldırmaqdır. 
def sum(a, b): # Bu funksiyanın məqsədi parametr olaraq verilən iki ədədi toplamaqdır. 
    return a + b
  
x = float(input("First: ")) # Istifadəçidən birinci rəqəmi alır.  
y = float(input("Second: ")) # İstifadəçidən ikinci rəqəmi alır.
print(sum(x, y)) # Yaratdığıçmız sum() funksiyasına istifadəçinin yazdığı rəqəmləri parametr kimi daxil edirik və print edirik. Yazılan rəqəmlər sum() funksiyası daxilində işlənir və toplanır. 
print(sum(1, 3)) #  Burada da daha sadəsini görə bilərsiniz. 1 və 3 rəqəmləri funksiya daxilində toplanır və print edilir.
