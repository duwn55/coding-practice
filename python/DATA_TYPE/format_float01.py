output_a = "{:f}".format(52.273)        #기본
output_b = "{:15f}".format(52.273)      #15칸 지정
output_c = "{:+15f}".format(52.273)     #부호추가하고 15칸 지정
output_d = "{:+015f}".format(52.273)    #부호추가하고 15칸 지정하고 0으로 채우

print(output_a)
print(output_b)
print(output_c)
print(output_d)
