def change_case(identifier, target_case):
    backup = identifier
    if identifier == "": return ""
    if target_case not in ["snake", "camel", "kebab"]: return None
    elif "-" in identifier and "_" in identifier: return None
    elif "-" in identifier and [x for x in identifier if x == x.upper() and x.isalpha()] != []: return None
    elif "_" in identifier and [x for x in identifier if x == x.upper() and x.isalpha()] != []: return None
    if "_" in identifier: 
        ans =  identifier.split("_")
        case = "snake"
    elif "-" in identifier: 
        ans = identifier.split("-")
        case = "kebab"
    else:
        ans = []
        a = 0
        for i in range(len(identifier)):
            if identifier[i] == identifier[i].upper():
                ans.append(identifier[a:i])
                a = i
        ans.append(identifier[a:i+1])
        case = "camel"
    if case == target_case: return backup
    if target_case == "snake":
        return "_".join([x.lower() for x in ans])
    elif target_case == "camel":
        ans = ans[0] + "".join([x.capitalize() for x in ans if x != ans[0]])
        return ans
    elif target_case == "kebab":
        return "-".join([x.lower() for x in ans])

print(change_case('cdefghijklm_ghijklm_cdefghijklm_cdefghijklm_efghijklm', 'snake'))