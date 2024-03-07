# def star(wars):
#     hansolo = lambda: wars + 2
#     iteration = 1

#     while wars * hansolo() < 4000:
#         wars = hansolo() + 5
#         print(f"Iterasyon {iteration}: wars = {wars}, hansolo = {hansolo()}")
#         iteration += 1

#         if wars > 100:
#             return hansolo()

#     return wars

# luke = star(50)
# print("Son Değer:", luke)
def star(trek):
    riker=6
    print("",riker)
    print(spock)
    borg=trek(spock,riker)-5
    print(riker)
    return borg

spock,riker=3,8
def borg(riker,kirk):
    print(kirk)
    print(spock)
    riker=riker*kirk-spock
    print(riker)
    return riker

print(star(borg))