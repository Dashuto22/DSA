def unique_email_address(emails):
    unique = set()
    for e in emails:
        i,local =0, ""
        while e[i] not in ["@", "+"]:
            if e[i] != ".":
                local += e[i]
            i += 1

        while e[i]!="@":
            i += 1

        domain = e[i+1:]

        unique.add((local, domain))

    return len(unique)



if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    val = unique_email_address(emails)

    print(val)