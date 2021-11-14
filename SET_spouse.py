
def spouse(spouse_type ,partner_1, partner_2):
    spouse_type = spouse_type.lower()
    if spouse_type == 'wife':
        partner_1.wife = partner_2
    elif spouse_type == 'husband':
        partner_1.husband = partner_2
    