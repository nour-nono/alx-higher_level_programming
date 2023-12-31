#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ans = []
    for x in range(list_length):
        z = 0
        try:
            z = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            ans.append(z)
    return ans
