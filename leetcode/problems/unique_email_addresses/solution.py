class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        receiveMails = []

        for email in emails:
            splitEmail = email.split("@")
            finalMail = splitEmail[0].split("+")[0].replace(".", "") + '@' + splitEmail[1]

            if finalMail not in receiveMails:
                receiveMails.append(finalMail)

        return len(receiveMails)