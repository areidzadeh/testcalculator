print("ماشین حساب ساده")
print("----------------")

num1 = float(input("عدد اول را وارد کنید: "))
operator = input("عملگر را وارد کنید (+ - * /): ")
num2 = float(input("عدد دوم را وارد کنید: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "خطا! تقسیم بر صفر ممکن نیست."

else:
    result = "عملگر وارد شده صحیح نیست."

print("----------------")
print("نتیجه:", result)