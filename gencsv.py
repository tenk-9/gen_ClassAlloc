
def tosmall(bignum):
    smdict = {
        "０": "0",
        "１": "1",
        "２": "2",
        "３": "3",
        "４": "4",
        "５": "5",
        "６": "6",
        "７": "7",
        "８": "8",
        "９": "9",
        "Ａ": "A",
        "Ｖ": "V",
        "Ｃ": "C",
        "Ｌ": "L"
        }
    if (bignum in smdict.keys()):
        return smdict[bignum]
    else:
        return bignum

with open("class_alloc.csv", "a", encoding="utf-8") as out:
    # out.write("lecture_id,campus,building,room_id\n")
    while (True):
        lec_id = input("lecture_id:")
        campus = "日野"
        building = input("building:")
        room_id = input("room_id:")

        lec_id_after = ""
        building_after = ""
        room_id_after = ""
        for c in lec_id:
            lec_id_after += tosmall(c)
        for c in building:
            building_after += tosmall(c)
        for c in room_id:
            room_id_after += tosmall(c)
        building_after+="号"
        
        out.write("{},{},{},{}\n".format(lec_id_after,
                  campus, building_after, room_id_after))
