f_cost, v_cost, price = map(int, input().split()) # 고정 비용, 가변 비용, 판매 비용

break_even_point = 0	# 손익분기점

if v_cost < price:	# 손익분기점 존재
    break_even_point = f_cost // (price - v_cost)   
    print (break_even_point + 1)
else:	# 손익분기점 존재하지 않음
    print(-1)
