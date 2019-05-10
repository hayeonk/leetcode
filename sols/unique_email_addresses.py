class Solution(object):
    def numUniqueEmails(self, emails):
        count = set()
        
        for email in emails:
            local, domain = email.split("@")
            
            local = "".join(local.split("."))
            if "+" in local:
                local = local[:local.index("+")]
            
            count.add((local, domain))
        
        return len(count)