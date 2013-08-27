from django.shortcuts import render_to_response
from django.template import Template, Context


class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def memb_reg(request):
    members = dict()
    members[2] = Member("Kurt", 64)
    members[5] = Member("Arne", 39)
    members[3] = Member("Bert", 15)
    members[8] = Member("Julius_Caesar", 2113)

    c = Context({
                    'NUMBER_OF_MEMBERS': len(members),
                    'MEMBER_INFO': members,  # Important, note the last ","!
                })

    return render_to_response('bobbin_lace/memb_reg.html', c)