def sum_nums(*nums): # Bu funksiyanın məqsədi verilən nə qədər rəqəm varsa hamısını toplayır.
    return sum(nums) # Pythonun verdiyi sum funksiyası ilə verilən rəqəmləri toplayırıq.

input_nums = input("Write numbers with ',': ") # İstifadəçidən rəqəmləri "," (vergül) ilə alırıq. Məsələn; 1,3,5,7,2
num_list = [float(num) for num in input_nums.split(',')] # Burada həmin yazıdaki rəqəmləri float`a çevirib vergüllərdən ayırırıq.
print(sum_nums(*num_list)) # Burada da həmin listdə olan rəqəmləri parametr olaraq sum_nums() funksiyasına daxil edirik və print edirik. 
