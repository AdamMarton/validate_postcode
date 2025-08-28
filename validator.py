import re

def validate_post_code(post_code_str: str) -> tuple[bool, str]:
    '''
    Validation logic is based on the following Wikipedia page:
    https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation
    '''
    post_code = post_code_str.replace(' ', '').upper()
    pc_regex = re.compile(r'^([A-Z]{1,2}[0-9][A-Z0-9]?)\s?([0-9][A-Z]{2})$')
    matches = pc_regex.match(post_code)

    if not matches:
        return False, "Does not match general postcode format."

    outward_code, inward_code = matches.groups()

    # The letters Q, V and X are not used in the first position.
    if post_code[0] in 'QVX':
        return False, "Invalid first letter."

    # The letters I, J and Z are not used in the second position.
    if len(post_code) > 1 and post_code[1] in 'IJZ':
        return False, "Invalid second letter."

    # The final two letters do not use C, I, K, M, O or V, so as not to resemble digits or each other when hand-written.
    if inward_code[-2] in 'CIKMOV' or inward_code[-1] in 'CIKMOV':
        return False, "Invalid letters in the last two positions."

    # The following central London single-digit districts have been further divided by inserting a letter
    # after the digit and before the space: EC1–EC4 (but not EC50), SW1, W1, WC1, WC2
    # and parts of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
    #
    # The validation below is flaky as it's not passing `EC1A 1BB` which is an actual example on Wikipedia.
    central_london_codes = ['E1W', 'N1C', 'N1P', 'NW1W', 'SE1P', 'W1', 'EC1', 'EC1', 'EC2', 'EC3', 'EC4', 'SW1', 'WC1', 'WC2']
    if len(outward_code) > 2 and outward_code[0:2] in ['EC', 'SW', 'W', 'WC']:
        if outward_code not in central_london_codes:
            return False, "Invalid format for a Central London postcode."
            
    # Areas with only single-digit districts: BL, BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE
    # (although WC is always subdivided by a further letter, e.g. WC1A)
    single_digit_areas = ['BL', 'BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM', 'SR', 'WC', 'WN', 'ZE']
    if post_code[:2] in single_digit_areas and not post_code[2].isdigit():
        return False, "Area must have a single-digit district."
    
    # Areas with only double-digit districts: AB, LL, SO (for AB this arose from decoding of the original five districts
    # AB1-AB5 by adding a second digit, to enable additional postcodes to become available,
    # thus AB1 was divided into AB10-AB16).
    double_digit_areas = ['AB', 'LL', 'SO']
    if post_code[:2] in double_digit_areas and not (post_code[2].isdigit() and post_code[3].isdigit()):
        return False, "Area must have a double-digit district."

    # The post code seems valid, return results.
    return True, "Valid post code."
